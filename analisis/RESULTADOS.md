# Robustez ordinal — resultados

**Corrido el 01/09/2026** con `analisis/robustez_ordinal.py` sobre el caso de
referencia (`P=10 · N=$16.000 · h_p=160 · a=60% · r=20% · η=80% · H_min=640 ·
Ct=$1.229/mes · M=$500`). Control: `P'=7`, `S=$2.456,5`, `IDA=57,6` — idéntico
a `calc()` en `index.html`.

## Qué pregunta se contesta acá

Los premios de riesgo **ρ** del modelo son criterio experto, no dato medido, y
está declarado como tal en el sitio y en el paper. La objeción inmediata es:
*«entonces las conclusiones dependen de números que inventaste»*.

Este análisis **no calibra los ρ**. Pregunta otra cosa: **¿las conclusiones
sobreviven a que los ρ estén mal?** Se perturba cada ρ ±50% y se mira qué se
rompe. Es una prueba ordinal: no importa el valor del resultado, importa si
cambia la decisión.

---

## P1 · La ubicación del óptimo es invariante ✅

Con costo por API, el ahorro `S` se maximiza en

```
a_ef* = 1 − P_min / P
```

En esa expresión **no aparece λ ni ningún ρ**. Verificado por barrido numérico
de `a_ef` en [0, 1] para los ocho valores de λ que el modelo puede tomar
(1,00 · 1,02 · 1,10 · 1,22 · 1,30 · 1,45 · 1,50 · 1,65):

| λ | a* hallado |
|---|---|
| todos | **0,6005** (analítico: 0,6000) |

**Una sola ubicación para los ocho λ.** El punto donde conviene dejar de
automatizar no depende de los coeficientes de riesgo: lo fija el piso de
continuidad contra la dotación, y nada más.

## P2 · La existencia del óptimo aguanta 3× ✅

El máximo es interior mientras el sueldo marginal liberado supere al costo
marginal de IA:

```
λ < C_h / c = 10 / 2 = 5
```

El λ máximo que el modelo admite es **1,65** (tope por diseño). El óptimo
sigue existiendo hasta **3,0×** ese peor caso. Para que el hallazgo central
desapareciera, los ρ tendrían que estar subestimados en un factor de tres,
no en un 50%.

## P3 · El orden de las arquitecturas — resultado partido ⚠️

Acá el resultado **no es limpio y conviene decirlo así.**

**El ranking completo de las 12 configuraciones NO es robusto:**

| Prueba | Orden idéntico al nominal |
|---|---|
| 243 vértices extremos (cada ρ a −50% / nominal / +50%) | **2,9%** (7/243) |
| Monte Carlo, 20.000 sorteos, ρ ~ U(±50%), semilla 7 | **7,1%** |

**Pero el desorden es local, no global:**

| Inversiones sobre 66 pares posibles | |
|---|---|
| mediana | 4/66 (6%) |
| p95 | 9/66 (14%) |
| peor vértice | 14/66 (21%) |

**Y la decisión que de verdad se toma es completamente estable:**

> A igual par de flags, ¿se mantiene `local ≤ multi-cloud ≤ nube única`?
> **100,0% de 20.000 sorteos.**

### P4 · A qué perturbación la inversión se vuelve posible

**Corregido el 01/09 tras una revisión externa.** Reportar «100% de los sorteos»
a ±50% **sobreestimaba el resultado**: a esa magnitud los intervalos de dos
premios no se solapan, así que la inversión es imposible por construcción, no
improbable. Lo informativo es el umbral.

Dos primas ρᵢ > ρⱼ pueden invertirse solo cuando `f > (ρᵢ − ρⱼ)/(ρᵢ + ρⱼ)`:

| Par | ρ | Umbral |
|---|---|---|
| nube única / multi-cloud | 0,30 vs 0,10 | **f > 50,0%** |
| multi-cloud / local | 0,10 vs 0,02 | f > 66,7% |
| nube única / local | 0,30 vs 0,02 | f > 87,5% |

**±50% es exactamente el borde, no un margen holgado.** Pero el barrido matiza
en la otra dirección: la inversión se vuelve *posible* en f = 0,50 y recién es
*material* mucho después, porque exige la esquina extrema de dos sorteos a la vez.

| f | orden intacto |
|---|---|
| ±40% | 100,0% |
| ±50% | 100,0% |
| ±51% | 100,0% |
| ±60% | 97,7% |
| ±75% | 91,7% |
| ±100% | 73,9% |

**El enunciado correcto:** la elección de arquitectura es robusta a cualquier
error de estimación menor a **un factor de tres** entre nube única y
multi-cloud, que es su cociente nominal.

### Una afirmación de la Tabla 2 que conviene decir en voz alta

`ρ(nube única) − ρ(multi-cloud) = 0,20 = ρ(sin plan de contingencia)`

**El modelo sostiene que un plan de contingencia ensayado vale exactamente lo
mismo que un segundo proveedor.** Eso es una elección de coeficiente, no un
hallazgo, y es de las primeras cosas que el panel de calibración debería
someter a prueba.

### Por qué el ranking completo se desarma

No es inestabilidad: **son empates.** En el orden nominal hay dos pares con λ
exactamente igual —`multicloud+sin_plan` y `nube_unica` ambos en 1,300;
`multicloud+sin_plan+datos_sens` y `nube_unica+datos_sens` ambos en 1,450—.
Cualquier perturbación rompe el empate en una dirección u otra y eso ya cuenta
como «orden distinto», sin que haya cambiado nada sustantivo.

El tope `λ ≤ 1,65` agrega compresión en el extremo superior: varias
configuraciones colapsan al mismo valor y quedan indistinguibles.

---

## Qué habilita decir esto, y qué no

**Sí se puede afirmar:**

- La ubicación del óptimo de automatización **no depende de los coeficientes**.
- La existencia del óptimo aguanta que los ρ estén subestimados hasta 3×.
- La elección de arquitectura —el uso principal del modelo— **resiste ±50% en
  cada ρ**, y ese margen equivale a un error de estimación de hasta un factor
  de tres entre nube única y multi-cloud (ver P4).

**No se puede afirmar:**

- Que el ranking fino entre configuraciones cercanas sea confiable. No lo es, y
  el modelo no debería usarse para distinguir dos arquitecturas separadas por
  menos de ~0,05 de λ.
- Que los ρ sean correctos. Esto no los calibra. Sigue haciendo falta el panel
  de elicitación.

**Lo que cambia respecto de la crítica original:** la objeción no queda
respondida, queda *acotada*. Los coeficientes siguen sin calibrar, pero ahora
está medido qué conclusiones dependen de ellos —el ranking fino— y cuáles no
—el óptimo y la decisión de arquitectura—.

## Reproducir

```bash
python analisis/robustez_ordinal.py
```

Las cuatro pruebas (P1 a P4) corren juntas. P4 se agrega llamando a `p4()`.

Determinista: semilla fija 7. Cualquier cambio en `calc()` de `index.html`
debe replicarse en `modelo()` del script, o los dos motores divergen.
