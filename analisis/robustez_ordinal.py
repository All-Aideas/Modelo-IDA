# -*- coding: utf-8 -*-
"""
Robustez ordinal del Modelo IDA
===============================

Pregunta que responde
---------------------
Los premios de riesgo rho son criterio experto, no dato medido. La objecion
obvia es: "entonces las conclusiones dependen de numeros que inventaste".

Este script contesta esa objecion SIN calibrar nada. No pregunta si los rho
son correctos: pregunta si las conclusiones del modelo sobreviven a que esten
mal. Tres pruebas:

  P1. La UBICACION del optimo de automatizacion, a* = 1 - P_min/P.
  P2. La EXISTENCIA de ese optimo (que el maximo sea interior, no en a=1).
  P3. El ORDEN de las arquitecturas por ahorro, bajo perturbacion de +/-50%
      en cada rho: en los 3^5 vertices extremos y en Monte Carlo.
  P4. A QUE MAGNITUD de perturbacion la inversion del orden se vuelve posible
      (la cota ajustada; sin esto, el 100% de P3 sobreestima el resultado).

Motor identico al de calc() en index.html. Si divergen, manda index.html.

Uso:  python analisis/robustez_ordinal.py
"""
import itertools
import math
import random

# ---------------------------------------------------------------- modelo
LAMBDA_MAX = 1.65


def modelo(P, N, hp, a, r, eta, Ct_hora, M, Hmin, lam, R=0):
    """Estado del modelo. Ct_hora = costo por hora automatizada (modo API)."""
    H = P * hp
    a_ef = a * (1 - r) * eta
    Pmin = math.ceil(Hmin / hp)
    Pecon = math.ceil(P * (1 - a_ef))
    Pf = max(Pecon, Pmin)
    horasIA = H * a_ef
    CtMes = Ct_hora * horasIA          # costo VARIABLE (API): el caso base
    S = (P - Pf) * (N / P) - CtMes * lam - M
    cob = 0 if Pmin == 0 else min(R / Pmin, 1)
    IDA = min(a_ef * lam * (1 - cob * 0.7) * 100, 100)
    return {"a_ef": a_ef, "Pmin": Pmin, "Pfinal": Pf, "S": S, "IDA": IDA}


def lam_de(rhos):
    return min(1 + sum(rhos), LAMBDA_MAX)


# ------------------------------------------------------- caso de referencia
BASE = dict(P=10, N=16000, hp=160, a=0.60, r=0.20, eta=0.80,
            Ct_hora=1229 / (10 * 160 * 0.60 * 0.80 * 0.80), M=500, Hmin=640)

# rho nominales, tal como estan en el sitio
RHO = {"local": 0.02, "multicloud": 0.10, "nube_unica": 0.30,
       "sin_plan": 0.20, "datos_sensibles": 0.15}

ARQ = ["local", "multicloud", "nube_unica"]


def configuraciones():
    """Las 12 arquitecturas que un usuario puede efectivamente elegir."""
    for base in ARQ:
        for sp in (False, True):
            for ds in (False, True):
                claves = [base]
                if sp:
                    claves.append("sin_plan")
                if ds:
                    claves.append("datos_sensibles")
                nombre = base + ("+sin_plan" if sp else "") + ("+datos_sens" if ds else "")
                yield nombre, claves


def orden_por_ahorro(rho):
    """Ranking de las 12 configuraciones por ahorro mensual, de mejor a peor."""
    filas = []
    for nombre, claves in configuraciones():
        lam = lam_de([rho[k] for k in claves])
        filas.append((nombre, modelo(**BASE, lam=lam)["S"], lam))
    filas.sort(key=lambda f: -f[1])
    return filas


# ================================================================ P1 y P2
def optimo_numerico(lam, paso=0.0005):
    """Busca por barrido el a_ef que maximiza S, para el lambda dado."""
    mejor, arg = -1e18, None
    x = 0.0
    while x <= 1.0 + 1e-9:
        # inyectamos a_ef directo: a=x, r=0, eta=1
        s = modelo(**{**BASE, "a": x, "r": 0.0, "eta": 1.0}, lam=lam)["S"]
        if s > mejor:
            mejor, arg = s, x
        x += paso
    return arg, mejor


def p1_p2():
    P, Hmin, hp = BASE["P"], BASE["Hmin"], BASE["hp"]
    Pmin = math.ceil(Hmin / hp)
    a_teo = 1 - Pmin / P
    print("P1 - UBICACION DEL OPTIMO")
    print("  Analitico:  a* = 1 - P_min/P = 1 - {}/{} = {:.4f}".format(Pmin, P, a_teo))
    print("  En la formula de a* NO aparece lambda ni ningun rho.")
    print("  Verificacion numerica barriendo a_ef en [0,1] para cada lambda posible:")
    ubic = set()
    for lam in [1.00, 1.02, 1.10, 1.22, 1.30, 1.45, 1.50, 1.65]:
        arg, _ = optimo_numerico(lam)
        ubic.add(round(arg, 3))
        print("    lambda={:.2f}  ->  a* = {:.4f}".format(lam, arg))
    print("  Ubicaciones distintas encontradas: {}  ->  {}".format(
        len(ubic), "INVARIANTE" if len(ubic) == 1 else "CAMBIA"))

    print("")
    print("P2 - EXISTENCIA DEL OPTIMO (interior, no en a=1)")
    # El maximo es interior mientras el sueldo marginal supere al costo marginal:
    #   N > Ct_hora * P * hp * lambda   ->   lambda < N / (Ct_hora*P*hp)
    # C_h = costo de la hora humana; c = costo de la hora automatizada.
    # Ojo: usar Ct_hora derivado del gasto REDONDEADO (1229) da 4.999 y sugiere
    # una precision que no existe. El valor exacto es C_h/c = 10/2 = 5.
    C_h = BASE["N"] / (BASE["P"] * BASE["hp"])
    c = round(BASE["Ct_hora"], 2)
    umbral = C_h / c
    print("  Condicion: lambda < C_h/c = {:g}/{:g} = {:g}".format(C_h, c, umbral))
    print("  Lambda maximo que el modelo admite: {}".format(LAMBDA_MAX))
    print("  Margen: el optimo sigue existiendo hasta {:.1f}x el peor lambda posible.".format(
        umbral / LAMBDA_MAX))
    return a_teo, umbral


# ==================================================================== P3
def p3(factor=0.5, n_mc=20000, semilla=7):
    base_orden = [f[0] for f in orden_por_ahorro(RHO)]
    print("")
    print("P3 - ORDEN DE LAS ARQUITECTURAS BAJO PERTURBACION DE +/-50%")
    print("  Orden nominal (mejor -> peor ahorro):")
    for i, (n, s, l) in enumerate(orden_por_ahorro(RHO), 1):
        print("    {:2d}. {:<32} S=${:8,.0f}  lambda={:.3f}".format(i, n, s, l))

    n_pares = 12 * 11 // 2

    # --- vertices extremos: cada rho a -50%, nominal, o +50% (3^5 = 243)
    iguales = distintos = 0
    peor = None
    for combo in itertools.product([-1, 0, 1], repeat=len(RHO)):
        rho = {k: RHO[k] * (1 + factor * m) for k, m in zip(RHO, combo)}
        o = [f[0] for f in orden_por_ahorro(rho)]
        if o == base_orden:
            iguales += 1
        else:
            distintos += 1
            inv = sum(1 for i in range(len(o)) for j in range(i + 1, len(o))
                      if base_orden.index(o[i]) > base_orden.index(o[j]))
            if peor is None or inv > peor[0]:
                peor = (inv, combo, o)
    tot = iguales + distintos
    print("")
    print("  Vertices extremos (3^{} = {} combinaciones):".format(len(RHO), tot))
    print("    orden identico:  {}/{}  ({:.1f}%)".format(iguales, tot, 100 * iguales / tot))
    if peor:
        print("    peor caso: {} inversiones sobre {} pares ({:.1f}%)".format(
            peor[0], n_pares, 100 * peor[0] / n_pares))

    # --- Monte Carlo: cada rho uniforme en +/-50%
    random.seed(semilla)
    ok = 0
    inversiones = []
    for _ in range(n_mc):
        rho = {k: v * (1 + random.uniform(-factor, factor)) for k, v in RHO.items()}
        o = [f[0] for f in orden_por_ahorro(rho)]
        if o == base_orden:
            ok += 1
        inversiones.append(sum(1 for i in range(len(o)) for j in range(i + 1, len(o))
                               if base_orden.index(o[i]) > base_orden.index(o[j])))
    inversiones.sort()
    print("")
    print("  Monte Carlo ({:,} sorteos, semilla {}):".format(n_mc, semilla))
    print("    orden identico:      {:.1f}%".format(100 * ok / n_mc))
    print("    inversiones mediana: {}/{}".format(inversiones[n_mc // 2], n_pares))
    print("    inversiones p95:     {}/{}".format(inversiones[int(n_mc * 0.95)], n_pares))

    # --- la pregunta que de verdad importa para decidir
    print("")
    print("  Decision practica: a igual par de flags, se mantiene el orden")
    print("  local < multicloud < nube unica?")
    random.seed(semilla)
    firme = 0
    for _ in range(n_mc):
        rho = {k: v * (1 + random.uniform(-factor, factor)) for k, v in RHO.items()}
        bien = True
        for sp in (False, True):
            for ds in (False, True):
                extra = []
                if sp:
                    extra.append(rho["sin_plan"])
                if ds:
                    extra.append(rho["datos_sensibles"])
                ss = [lam_de([rho[a]] + extra) for a in ARQ]
                if not (ss[0] <= ss[1] <= ss[2]):
                    bien = False
        firme += bien
    print("    se mantiene en {:.1f}% de los sorteos".format(100 * firme / n_mc))
    return 100 * ok / n_mc, 100 * firme / n_mc


# ==================================================================== P4
def p4(n_mc=20000, semilla=7):
    """A que magnitud de perturbacion la inversion se vuelve POSIBLE.

    Reportar "100% de los sorteos" a +/-50% sobreestima el resultado: a esa
    magnitud los intervalos de dos premios no se solapan, asi que la inversion
    es imposible por construccion, no improbable. Lo informativo es el umbral.

    Dos premios rho_i > rho_j se pueden invertir cuando
        rho_i (1 - f) < rho_j (1 + f)   =>   f > (rho_i - rho_j) / (rho_i + rho_j)
    """
    print("")
    print("P4 - UMBRAL DE PERTURBACION AL QUE LA INVERSION SE VUELVE POSIBLE")
    pares = [("nube_unica", "multicloud"), ("multicloud", "local"), ("nube_unica", "local")]
    umbrales = []
    for hi, lo in pares:
        a, b = RHO[hi], RHO[lo]
        f = (a - b) / (a + b)
        umbrales.append((f, hi, lo))
        print("  {:<12} vs {:<12} rho {:.2f} vs {:.2f}  ->  se invierte solo si f > {:.1%}".format(
            hi, lo, a, b, f))
    fmin = min(umbrales)
    print("  Cota ajustada: el orden de arquitecturas resiste hasta f = {:.1%},".format(fmin[0]))
    print("  y el par que primero cede es {} / {}.".format(fmin[1], fmin[2]))
    print("  => el 100% a +/-50% NO es holgura: +/-50% es exactamente el borde.")

    print("")
    print("  Verificacion por barrido de f:")
    random.seed(semilla)
    for f in [0.40, 0.49, 0.50, 0.51, 0.60, 0.75, 1.00]:
        ok = 0
        for _ in range(n_mc // 4):
            rho = {k: v * (1 + random.uniform(-f, f)) for k, v in RHO.items()}
            bien = all(rho["local"] <= rho["multicloud"] <= rho["nube_unica"]
                       for _ in (0,))
            ok += bien
        print("    f = {:>5.0%}  ->  orden de arquitecturas intacto en {:5.1f}% de los sorteos".format(
            f, 100 * ok / (n_mc // 4)))

    print("")
    print("  Consecuencia de la Tabla 2 que conviene decir en voz alta:")
    print("    rho(nube_unica) - rho(multicloud) = {:.2f} = rho(sin_plan) = {:.2f}".format(
        RHO["nube_unica"] - RHO["multicloud"], RHO["sin_plan"]))
    print("    El modelo afirma que un plan de contingencia vale exactamente")
    print("    lo mismo que pasar de una nube a dos. Es una afirmacion, no un hecho.")
    return fmin[0]


if __name__ == "__main__":
    print("=" * 72)
    print("ROBUSTEZ ORDINAL DEL MODELO IDA - caso de referencia")
    print("=" * 72)
    ref = modelo(**BASE, lam=lam_de([RHO["nube_unica"], RHO["sin_plan"]]))
    print("Control: P'={}  S=${:,.1f}  IDA={:.1f}   (esperado: 7 / 2.456,5 / 57,6)".format(
        ref["Pfinal"], ref["S"], ref["IDA"]))
    print("")
    a_teo, umbral = p1_p2()
    ok, firme = p3()
    p4()
    print("")
    print("=" * 72)
