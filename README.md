# 🤖 Modelo IDA — ¿Cuánta gente necesita tu empresa el día que la IA no esté?

> Una fórmula para calcular tu **dotación mínima de continuidad** y un **Índice de Dependencia de IA (IDA)** para medir cuán expuesta está tu organización si la IA deja de estar disponible. Sirve igual para un call center, un banco, un retail o una transportadora de gas.

**[Probá la calculadora interactiva](https://cesarriat.com/modelo-ida)** · [Leer el artículo en Medium](#) · Autor: [César Riat](https://cesarriat.com)

---

## 1. El problema

Hoy un call center se puede automatizar al 100% con IA. Técnicamente no queda ninguna tarea que un agente de voz no pueda hacer: atender, resolver, escalar, registrar. La pregunta ya no es "¿se puede?".

La pregunta es otra: **¿qué pasa si de un día para otro no podés usar IA?**

No es paranoia. Puede pasar por muchos caminos: se cae el proveedor de nube, el modelo que usás se discontinúa, el precio cambia 10 veces, una regulación nueva te prohíbe procesar datos afuera del país, o te cortan el servicio por una disputa comercial. El 20 de abril de 2026, ChatGPT, Claude y Gemini —las tres plataformas que la mayoría trata como respaldo una de otra— se cayeron al mismo tiempo. Los que tenían "multi-modelo" como plan B descubrieron que el plan B se caía junto con el plan A.

Y acá está el punto ciego: cuando una empresa automatiza, calcula cuánta gente puede reducir. **Nadie calcula cuánta gente tiene que conservar.** Son dos números distintos, y el segundo es el que te salva.

Los marcos que existen hoy —las normas de continuidad de negocio como ISO 22301, la nueva ISO/IEC 42001 de gestión de IA, los análisis de impacto y los mapas de dependencia— te ayudan a *identificar* el problema: te muestran que dependés de la IA y dónde está el punto único de falla. Lo que no te dan es el número: cuántas personas, cuánta inversión tiene sentido, cuán expuesto estás. Este proyecto propone esa cuenta.

Y aplica a cualquier industria, aunque pega distinto según la criticidad:

| Industria | Si la IA se cae... | Severidad |
|---|---|---|
| **Call center** | Perdés ventas y clientes se enojan | Recuperable |
| **Retail** | Góndolas vacías o precios absurdos en fecha pico | Alta |
| **Banco** | Evento regulatorio, no solo comercial | Crítica |
| **Transportadora de gas** | Falla de seguridad pública, no de negocio | Extrema |

Mismo modelo, distinta severidad. Por eso la fórmula es general y los parámetros los pone cada empresa.

---

## 2. Aprendé los parámetros con casos extremos

Un buen modelo se reconoce en los bordes: cuando lo empujás al extremo, tiene que decir cosas sensatas. Y de paso, cada extremo te enseña una variable.

### Extremo A — "Automatizo el call center al 100%" → te enseña el piso **P_min**

La cuenta económica ingenua dice: si automatizás todo, necesitás cero personas. El modelo dice: no. La dotación cae con la automatización *hasta que choca con un piso* —el mínimo de gente para sostener la operación crítica sin IA— y ahí se planta, aunque automatices el 100%.

![Piso de continuidad](assets/g1_piso_continuidad.svg)

La diferencia entre lo que dice el Excel y lo que dice el piso es tu **prima de seguro operativo**: gente que parece "de más" hasta el martes que se cae la nube.

Y esa prima **tiene precio, no es gratis**: son sueldos que seguís pagando mientras la IA hace ese trabajo. El modelo se los cobra al proyecto en la fórmula de ahorro (ver §4), que es justamente lo que casi ningún business case de automatización hace.

### Extremo B — "Una sola nube y sin plan B" → te enseña el riesgo **λ**

Dos empresas automatizan lo mismo y pagan el mismo precio por token. Una corre todo sobre un solo proveedor, sin contingencia. La otra reparte entre dos y tiene procedimiento manual ensayado. ¿Pagan lo mismo? En la factura sí; en la realidad no. La primera "maneja sin seguro": el riesgo no aparece en la factura mensual, aparece todo junto el día del choque.

Ese riesgo se convierte en un recargo sobre el costo de la IA: el **multiplicador λ**. Si λ crece tanto que el costo real de la hora de IA alcanza al de la hora humana, la curva de ahorro se aplana. Si lo supera, **pagás por automatizar**.

![Riesgo animado](assets/g4_riesgo_animado.gif)

### Extremo C — "Monto DeepSeek local para automatizar los mails" → te enseña la inversión **I**

El caso que más confunde, porque mezcla dos verdades. Y acá van números reales, verificados en agosto de 2026.

**Verdad 1:** correr la IA en tus propios servidores **casi elimina el riesgo**. Nadie te corta el servicio, no dependés de ninguna nube, tus datos no salen del edificio. λ baja a casi 1. El modelo abierto de referencia hoy es **DeepSeek V4-Flash** (284B parámetros, licencia MIT): necesita ~175 GB de VRAM y entra en **2× GPUs H200**. Alquilar ese servidor 24/7 cuesta del orden de **USD 5.170 por mes**, fijo, uses lo que uses.

**Verdad 2:** ese costo es fijo y brutal si tu volumen es chico. La pregunta que la fórmula responde: **¿para qué tarea lo montás?**

Comparemos las tres opciones para automatizar emails que consumen **15 horas por semana** (~60 h/mes), asumiendo ~1 millón de tokens por hora de trabajo:

| Opción | Costo mensual para la tarea de emails | Riesgo (λ) |
|---|---|---|
| **API DeepSeek V4-Flash** ($0,14 / $0,28 por millón) | **~$13/mes** | Alto (nube única) |
| **API Gemini 3.6 Flash** ($1,50 / $7,50 por millón) | **~$270/mes** | Alto (nube única) |
| **DeepSeek local** (2× H200) | **~$5.170/mes** | Casi nulo |

Montar el servidor local para los emails cuesta **410 veces más** que usar la API de DeepSeek. Pagás $5.170 para reemplazar $13 de API. Absurdo, por más que el riesgo local sea casi cero: la tarea es demasiado chica para justificar el fierro.

> **⚠️ Y el fierro no es el costo completo.** Esos $5.170 son solo el alquiler. Correr IA propia necesita además **electricidad** (~$250/mes con 2,1 kW constantes) y sobre todo **alguien que la mantenga**: un sysadmin o perfil de MLOps, del orden de $3.000/mes. Total real **$8.420/mes**, y la brecha contra la API salta de 410× a **668×**.
>
> La ironía vale decirla: ese sysadmin cuesta **casi el doble** que la persona administrativa que estabas reemplazando. Automatizaste para no pagar un puesto y contrataste uno más caro.
>
> **Puede ser cero**, ojo: si ya tenés a alguien que lo absorbe o si un líder técnico se hace cargo. Lo que no es válido es no haberlo evaluado — ver §4 y el asistente de costo real de la calculadora.

![Local vs API](assets/g2_local_vs_api.svg)

**Misma tarea, tres arquitecturas, conclusiones opuestas.** Fijate también la brecha entre modelos de nube: Gemini 3.6 Flash sale ~20× más caro que DeepSeek Flash para el mismo trabajo. La fórmula no dice "local bueno / nube malo" ni "modelo caro malo": dice cuál conviene *para tu volumen y tu nivel de riesgo tolerable*.

### Extremo D — "El mismo DeepSeek local, pero a escala" → te enseña el volumen **H**

Ahora tomá el mismo servidor y ponelo en una operación que automatiza atención, back office y procesamiento a gran escala. El punto de equilibrio contra la API de DeepSeek depende de qué costos cuentes:

| Qué contás | Costo fijo/mes | Break-even | Equivale a |
|---|---|---|---|
| Solo el servidor | $5.170 | 24.600 millones de tokens/mes | 154 personas-equivalente |
| **Servidor + luz + sysadmin** | **$8.420** | **40.100 millones de tokens/mes** | **251 personas-equivalente** |

A 1M tokens por hora de trabajo, esas son 154 o 251 personas operando a tiempo completo sobre IA.

Por debajo de ese volumen, la API es más barata y sin dolores de cabeza de infraestructura. Por encima, el servidor propio empieza a ganar **y encima te baja λ al mínimo** — lo cual, para un banco, una empresa de salud o energía, puede ser decisivo aunque los números de costo estuvieran empatados: la **soberanía del dato** vuelve irrelevante el cálculo de tokens.

El mismo hardware que era un disparate para los emails es la **mejor decisión posible** a escala. No cambió la tecnología ni el precio: cambió el volumen (H) y la criticidad del dato.

> **La regla que se lleva el lector:** la IA local no se justifica por moda ni por miedo. Se justifica cuando tu volumen supera el break-even **o** cuando la criticidad del dato hace que λ importe más que el costo. Nunca antes.

> **Resumen:** el piso te frena por supervivencia, **λ** por riesgo, **I** por plata, y **H** es la palanca que puede dar vuelta cualquiera de las tres cuentas.

---

## 3. Los cuatro módulos

### 🧑 Módulo Humano
```
Costo hora humana (Ch) = Nómina mensual ÷ Horas totales
```
Ejemplo: $16.000/mes, 10 personas, 1.600 h → **$10/hora**.

### ⚙️ Módulo Automatización
```
Automatización efectiva = a × (1 − r) × η
```
- **r** — lo regulado (firma de médico, escribano): queda afuera sí o sí
- **a** — lo técnicamente automatizable del resto
- **η** — eficiencia real de la IA (70%–90%, nunca 100%)

Ejemplo: 0,60 × (1 − 0,20) × 0,80 = **38,4%**, no 60%. Primer baño de realidad.

**Un caso concreto: los emails de un retail.** Técnicamente se pueden contestar **el 100%** con IA: leer, entender, redactar, responder. Ese es tu `a` = 100%. Pero por regla de negocio hay correos que **tienen que pasar por una persona sí o sí**: los que mencionan temas legales, los reclamos que pueden derivar en defensa del consumidor, y los que piden datos personales. Si eso es 1 de cada 5, tu `r` = 20%. Y de los que sí automatizás, la IA no acierta siempre: hay que revisar, corregir y reenviar. Si rinde como 8 de cada 10 personas, tu `η` = 80%.

`1,00 × (1 − 0,20) × 0,80` = **64%**. Arrancaste creyendo que automatizabas todo y en la práctica sacás dos tercios de la carga. Ese 64% es el número con el que hay que hacer las cuentas.

### ⚠️ Módulo Riesgo
```
Costo real de la IA = λ × Gasto mensual de IA
```

**Qué significa ese multiplicador.** Si tu proveedor te factura $1.229 por mes, eso es lo que sale de tu cuenta bancaria: ese número no cambia. Lo que el modelo hace es **cobrarte un extra al momento de decidir** — con λ=1,50 anota $1.844 en la evaluación del proyecto.

¿Por qué? Porque además de la factura estás corriendo un riesgo que hoy no pagás pero que algún día se cobra solo: el día que la nube única se cae sin plan B perdés operación, ventas y credibilidad de golpe. Ese costo no aparece en ninguna factura mensual — aparece entero, una sola vez, el peor día. El multiplicador lo reparte en cuotas para que una arquitectura frágil se vea cara *cuando todavía estás a tiempo de cambiarla*.

Es la lógica del seguro del auto: manejar sin seguro no sale más barato, sale igual hasta que chocás.

**Dónde corre la IA** — elegís *una sola* de estas tres, son excluyentes:

| Arquitectura | Recargo a λ |
|---|---|
| Una sola nube | +30% |
| Multi-cloud (2+ proveedores) | +10% |
| IA local (en tus servidores) | +2% |

**Agravantes** — se suman los que apliquen:

| Condición | Recargo a λ |
|---|---|
| Sin plan de contingencia | +20% |
| Datos sensibles en nube externa | +15% |

**El trade-off central:** la IA local desploma λ pero infla I. La nube achica I pero infla λ. No hay opción gratis — la fórmula te dice cuál precio te conviene pagar según tu volumen H.

### 🛟 Módulo Continuidad
```
Piso de continuidad (P_min) = Horas mínimas para operar sin IA ÷ Horas por persona
```
Las horas mínimas son las de la operación crítica en modo degradado. La IA local baja P_min; la nube única lo sube.

> **Ojo: esto NO es lo mismo que la firma del médico o del escribano.** Son dos preguntas distintas y es donde más se confunde la gente.
>
> `r`, en el módulo Automatización, pregunta: *del trabajo que la IA podría hacer, ¿cuánto no puede por norma?* Es la firma del médico, del escribano, del auditor. Eso pasa **aunque la IA funcione perfecto**: hay tareas que legalmente no se delegan.
>
> `P_min`, acá, pregunta otra cosa: *si mañana la IA no está, ¿con cuánta gente sostengo lo que no puede parar?* No importa la firma: importa la **capacidad operativa**.
>
> **Cómo estimarlo.** No hace falta un estudio: pensalo en modo degradado y calculá a ojo. *"Si se cae todo tengo que atender 400 llamados al mes, y una persona atiende 2 por hora"* → 200 horas. *"Y alguien tiene que revisar pedidos 4 horas por día"* → 88 horas más. Total ≈ 290 h/mes: ese es tu `H_min`. Puede pasar que las dos cosas coincidan —el médico que firma es también el que sostiene la guardia— pero son cuentas separadas.

---

## 4. Cómo se unen los módulos

Los cuatro módulos no son fórmulas sueltas: cada uno produce **un número intermedio**, y esos cuatro números alimentan **tres resultados**. El modelo es un embudo, no una ecuación única:

```
Lo que cargás          Los cuatro módulos            Los tres resultados
─────────────          ──────────────────            ───────────────────
P, h_p, N        →     Humano        → C_h      ┐
a, r, η          →     Automatización→ a_ef     ├→   P'   ¿con cuánta gente me quedo?
ρ, C_mes         →     Riesgo        → λ        ├→   S, T ¿conviene y en cuánto se paga?
H_min            →     Continuidad   → P_min    ┘→   IDA  ¿cuán expuesto quedo?
I, M             →     (entran directo en S y T)

                       ...y además:  P'  ──────────→  S
                       (solo ahorrás el sueldo de quien podés liberar)
```

### Resultado 1 — Cuánta gente conservar (P')
```
P' = MÁXIMO entre:
   (a) ⌈ Personas actuales × (1 − Automatización efectiva) ⌉   ← la cuenta económica
   (b) Piso de continuidad P_min                                ← la cuenta de supervivencia
```

Hace **dos cuentas distintas y se queda con la más grande**:

1. **Cuenta económica:** si automatizás el 38,4%, te sobra ese 38,4% de la gente → `10 × (1 − 0,384) = 6,16 → 7 personas` (redondeo hacia arriba: no existe 6,16 empleados).
2. **Cuenta de supervivencia:** el `P_min` del módulo Continuidad → `640 ÷ 160 = 4 personas`. No sale de automatizar: sale de preguntarte cuánta gente necesitás el día que la IA no está.
3. **`MÁXIMO(7 , 4) = 7`.**

**¿Por qué la más grande?** Porque las dos son condiciones que tenés que cumplir *al mismo tiempo*: al menos 7 para el trabajo diario, al menos 4 para sobrevivir sin IA. Solo el mayor cumple las dos.

En este ejemplo manda la economía. Pero si automatizás al 90%, la cuenta económica da `⌈10 × 0,10⌉ = 1` y entonces `MÁXIMO(1 , 4) = 4`: **ahí el piso toma el control**. Por más que automatices el 100%, nunca bajás de 4. Esa diferencia es tu **reserva de capacidad humana**.

### Resultado 2 — Si conviene o no (S y T)
```
S = (P − P') × sueldo − λ × Gasto mensual de IA − Mantenimiento
T = Inversión ÷ S
```

Fijate que S **arranca con P'**, el resultado anterior: solo ahorrás el sueldo de la gente que efectivamente podés liberar.

1. **Cuánta gente liberás de verdad:** `P − P' = 10 − 7 = 3 personas`. No son 3,84 (el 38,4% de 10): no se despiden fracciones de persona, y si el piso se activa liberás todavía menos.
2. **Ahorro en sueldos:** cada persona cuesta `N ÷ P = $1.600/mes` → `3 × $1.600 = $4.800`.
3. **Costo de la IA:** `1.600 × 0,384 × 1,5 × $2 = $1.843/mes`. Acá entra λ: la factura dice $2/h, el riesgo la convierte en $3/h.
4. **Ahorro:** `$4.800 − $1.843 − $500 = $2.457/mes`.
5. **Para qué sirve S:** es el semáforo y el divisor del recupero. Si S ≤ 0, automatizar cuesta más de lo que ahorra. Si S > 0, `T = $50.000 ÷ $2.457 = 20 meses`. Regla práctica: **arriba de 18 meses, no avances** — este proyecto, con la cuenta honesta, no pasa.

> #### ⚠️ La trampa que esta fórmula evita
>
> La cuenta intuitiva es `horas automatizadas × costo hora humana`: 614,4 h × $10 = **$6.144**. Es falso: vos no pagás horas, pagás sueldos. Automatizar 3,84 personas-equivalente cuando solo podés echar 3 **no ahorra 3,84 sueldos, ahorra 3**.
>
> Cuando el piso de continuidad se activa la brecha explota. Con automatización al 100% y piso de 4, la cuenta ingenua promete **$10.700/mes**; el ahorro real es **$4.300/mes**. Los $6.400 de diferencia son los cuatro sueldos que seguís pagando por continuidad mientras la IA hace ese trabajo. **Esa es la prima de seguro operativo, y el modelo ahora te la cobra.**

> #### ↓ El corolario incómodo: existe un óptimo de automatización
>
> Una vez que chocaste el piso, cada punto extra de automatización **suma factura de IA pero no libera a nadie más**. Desde ahí, automatizar más te **baja** el ahorro y te **sube** el IDA: quedás más pobre y más dependiente a la vez.
>
> | Autom. efectiva | Ahorro "ingenuo" | Ahorro real | IDA |
> |---|---|---|---|
> | 60% (óptimo) | $6.220 | **$6.220** | 90 |
> | 80% | $8.460 | $5.260 | 100 |
> | 100% | $10.700 | $4.300 | 100 |
>
> El máximo de automatización nunca es el óptimo de automatización.

**Una aclaración honesta sobre λ:** S es el *ahorro ajustado por riesgo*, no el flujo de caja contable. λ no es un cheque que le firmás a tu proveedor: es una prima de riesgo implícita que el modelo cobra para castigar arquitecturas frágiles al decidir. Tu contador va a ver un ahorro mayor (el mismo número con λ=1); tu director de riesgo va a querer ver este.

### Resultado 3 — Índice de Dependencia de IA (IDA)
```
IDA = MÍNIMO( Automatización efectiva × λ × 100 , 100 )
```
`0,384 × 1,50 × 100 = 58` → zona amarilla.

El `MÍNIMO` no es decorativo: con automatización alta y arquitectura frágil el producto se pasa de 100 (el techo teórico es 177). Todo lo que supere 100 ya es "máxima dependencia posible", así que el índice se topea para que la escala 0–100 signifique siempre lo mismo.

| IDA | Zona | Qué significa |
|---|---|---|
| **< 30** | 🟢 Resiliente | Una caída de IA es una molestia |
| **30–60** | 🟡 Vigilancia | Necesitás piso calculado y simulacros manuales |
| **> 60** | 🔴 Crítico | Tu operación es rehén de tu proveedor |

**Por qué el IDA no incluye la plata.** Es deliberado: ahorrar y estar expuesto son cosas distintas. Podés tener un proyecto que ahorra bien y recupera rápido —excelente negocio— y estar igual en zona amarilla de dependencia. Si metieras el dinero adentro del IDA, un ahorro grande te *taparía* el riesgo y el índice te diría que estás bien justo cuando más frágil estás. El dinero ya tiene su fórmula: es S.

Dos empresas con la misma automatización pueden tener IDA muy distinto: 38,4% con nube única (λ=1,5) → **IDA 58**; la misma con IA local (λ=1,02) → **IDA 39**. **La dependencia no es cuánto automatizaste: es cuánto automatizaste por cuán frágil es lo que te sostiene.**

### Las fórmulas en una sola línea

Reemplazando cada módulo por su definición, cada resultado queda en función directa de lo que cargás:

```
P'  = MÁXIMO( ⌈P × (1 − a(1−r)η)⌉ , ⌈H_min ÷ h_p⌉ )

S   = [ P − MÁXIMO( ⌈P × (1 − a(1−r)η)⌉ , ⌈H_min ÷ h_p⌉ ) ] × N/P
      − (1+Σρ) × C_mes
      − M

IDA = MÍNIMO( a(1−r)η × (1+Σρ) × 100 , 100 )
```

S se lee en dos mitades: *los sueldos que dejás de pagar*, menos *lo que cuesta la IA ajustada por riesgo*, menos mantenimiento.

**¿Y una sola mega fórmula que junte los tres resultados?** No, y no por falta de ganas: vienen en unidades distintas —**personas**, **dólares por mes** y un **índice de 0 a 100**—. Sumarlos daría un número sin significado. Pero sí hay un **orden obligatorio**: `P'` se calcula primero porque **S depende de él**. Esa dependencia es lo que hace honesto al modelo — es la que le cobra a la empresa el costo de su propio piso de continuidad.

### La plata: inversión (una vez) vs costo operativo (todos los meses)

Confundir estos dos bolsillos es el error más caro que se puede cometer con el modelo.

| Inversión (I) — una sola vez | Costo operativo — todos los meses |
|---|---|
| Honorarios de proveedor o consultora | Tokens / API, o alquiler del servidor (**C_mes**) |
| **Horas de tus propios programadores** | Electricidad y conectividad |
| Integración con sistemas actuales | **SysAdmin o servicio gestionado** |
| Migración y limpieza de datos | Mantenimiento del software (**M**) |
| Licencias iniciales | Reentrenamiento al cambiar de modelo |
| **Horas de tu gente definiendo reglas y revisando salidas** | Monitoreo y auditoría de salidas |
| Hardware, *solo si lo comprás* | |

Las líneas en negrita son las que todo presupuesto olvida: **las horas internas no son gratis por ser internas**. Suelen ser el 20–30% de la inversión real. Si las contás en cero, el payback es ficción.

**Para evitar doble conteo:** si el servidor lo *alquilás*, es costo operativo y va en C_mes. Si lo *comprás*, es inversión y va en I. Nunca en los dos lados.

#### Dónde vive la inversión: en un solo lugar

La inversión **no aparece en ninguna fórmula de los módulos**. Solo en la división final `T = I ÷ S`:

| Inversión | Ahorro mensual | IDA | Recupero |
|---|---|---|---|
| $25.000 | $2.457 | 58 | 10 meses ✅ |
| $50.000 | $2.457 | 58 | 20 meses ❌ |
| $200.000 | $2.457 | 58 | 81 meses ❌ |

El ahorro no se mueve, el IDA no se mueve. Y está bien: la inversión es un gasto de una sola vez, no cambia cuánta plata te entra por mes ni cuán dependiente quedás.

> **La asimetría que importa:** un error en la **inversión** lo pagás una vez. Un error en el **costo operativo** te acompaña todos los meses para siempre. Si tenés poco tiempo para revisar supuestos, **revisá C_mes antes que I**.

#### El punto ciego: qué esconde el gasto mensual

La calculadora te pide el **gasto mensual** de IA porque es el número que conocés: sale de tu factura o de una proyección. Internamente guarda el **costo por hora automatizada**, para que si después cambiás cuánto automatizás, la factura escale sola. Sin eso el gasto quedaría plano y se perdería el hallazgo central del modelo — que pasado el piso, automatizar de más baja el ahorro.

Pero ojo con lo que ese número esconde: con **API** el gasto **sube y baja con el uso** —si automatizás menos, pagás menos—; con **servidor propio** el gasto es **fijo** y no baja aunque no lo uses. Con API el costo es una *diagonal*; con local, una *recta horizontal*. Por eso, si corrés local y automatizás menos de lo previsto, tu costo por hora se dispara sin que hayas tocado el contrato.

#### Cuánto cuesta de verdad correr local

Correr IA en tus servidores **no es solo el fierro**:

| Concepto | Costo mensual |
|---|---|
| Alquiler 2× H200, 24/7 | $5.170 |
| Electricidad (~2,1 kW constantes) | $250 |
| **SysAdmin / MLOps que lo mantenga** | **$3.000** |
| **Total real** | **$8.420** |

> **Estos números son un ejemplo, no un dogma.** La calculadora trae un **asistente de costo real**: elegís "pago por uso (API)" o "servidor propio" y te va pidiendo cada componente por separado —servidor, electricidad, sysadmin, otros—, suma el fijo mensual, lo divide por tus horas de IA y te devuelve el costo por hora listo para usar.
>
> El sysadmin puede ser **cero** con toda legitimidad: si ya tenés a alguien, si un líder técnico absorbe la tarea, o si lo contratás por hora solo cuando hace falta. Lo que el asistente busca no es imponerte un número: es que **ningún costo quede sin evaluar**. Poner 0 después de haberlo pensado es una respuesta válida; no haberlo pensado, no.

> **La ironía que hay que decir en voz alta:** ese sysadmin cuesta **1,88 veces el sueldo de la persona que estabas reemplazando** ($3.000 contra $1.600). Automatizaste para no pagar un puesto administrativo y contrataste uno técnico que sale casi el doble.

Y mueve el break-even de forma dramática:

| Qué contás | Break-even vs API DeepSeek |
|---|---|
| Solo el servidor | 154 personas-equivalente |
| Servidor + luz | 161 personas-equivalente |
| **Servidor + luz + sysadmin** | **251 personas-equivalente** |

Si no tenés esa escala, la alternativa honesta no es "no automatizar": es **API**, o un **servicio gestionado tercerizado** donde el sysadmin es problema del proveedor y entra como cuota mensual previsible.

Para el proyecto de 10 personas del ejemplo: con API DeepSeek el ahorro es **$4.168/mes** (12 meses); con servidor propio contando todo es **−$4.288/mes** y no recupera nunca.

### Ejemplo completo
Pyme: 10 personas, $16.000 nómina, 160 h c/u (1.600 h/mes), a=60%, r=20%, η=80%, nube única sin contingencia (λ=1,5), IA $2/h, H_min 640 h, inversión $50.000, mant. $500/mes.
- Automatización efectiva: `0,60 × 0,80 × 0,80` = **38,4%**
- Dotación: `MÁXIMO(7 , 4)` = **7 personas** (el piso de 4 no se activa) → liberás **3**
- Ahorro: `3 × 1.600 − 1.843 − 500` = **$2.457/mes** → recupero **20 meses** ❌
- **IDA 58 — vigilancia.**

Este ejemplo es deliberado: con la cuenta ingenua el proyecto parecía cerrar en 13 meses y daba luz verde. Con la cuenta honesta —que solo acredita los sueldos realmente liberados— se va a 20 meses y **no pasa el filtro**. La respuesta correcta no es cancelar: es bajar λ (segundo proveedor, plan de contingencia) o bajar la inversión inicial, y volver a correr el número.

---

## 5. Para los más avanzados: Montecarlo

Todo lo de arriba usa números fijos. La realidad no: el token cambió 10× en dos años y tu eficiencia real no la conocés hasta el tercer mes. La **simulación de Montecarlo** corre la misma fórmula 10.000 veces con rangos en vez de números fijos.

![Montecarlo](assets/g3_montecarlo.png)

El resultado deja de ser *"recuperás en 20 meses"* y pasa a ser *"31% de probabilidad de recuperar en menos de 18 meses; mediana 21"*. Montecarlo no reemplaza la fórmula: la alimenta.

Ese 31% es incómodo y por eso vale la pena: dice que con estos rangos el proyecto es más una apuesta que un plan. La palanca para moverlo casi nunca es automatizar más — es bajar λ o bajar la inversión inicial.

---

## 6. Conclusiones

Dos son las que importan (6.1 y 6.2): contraintuitivas, aparecen recién cuando hacés la cuenta honesta, y van en contra de lo que se recomienda hoy en casi cualquier presentación sobre IA. La tercera (6.3) es cómo llevar todo esto a un canal físico —una caja, una ventanilla, una guardia—, que es donde el modelo más sirve.

### 6.1 · El máximo de automatización no es el óptimo

La intuición dice que cuanto más automatices, más ahorrás. Es falso, y el modelo muestra exactamente dónde deja de serlo.

Hay una cantidad de gente que **no podés soltar**: el piso de continuidad. Una vez que llegás a ese piso, cada punto adicional de automatización **suma factura de IA pero ya no libera a nadie más**. Seguís pagando los mismos sueldos y encima pagás más IA.

| Automatización efectiva | Promesa ingenua | Ahorro real | Recupero | IDA |
|---|---|---|---|---|
| **60% — el óptimo** | $6.220 | **$6.220** | **8 meses** | 90 |
| 80% | $8.460 | $5.260 | 10 meses | 100 |
| 100% | $10.700 | $4.300 | 12 meses | 100 |

Leé la última fila con calma: al automatizar el 100%, la cuenta ingenua promete **$10.700/mes** y la realidad da **$4.300**. Los $6.400 que faltan son los cuatro sueldos del piso, que seguís pagando mientras la IA hace ese trabajo.

> **Pasado el piso, automatizar de más te deja más pobre y más dependiente al mismo tiempo:** el ahorro baja de $6.220 a $4.300, el recupero se estira de 8 a 12 meses y el IDA sube de 90 a 100. Las tres cosas empeoran juntas — y se llega ahí haciendo exactamente lo que todos recomiendan hacer.

### 6.2 · Lo que salva un proyecto es la arquitectura, no despedir más gente

Cuando el número no cierra, el reflejo de cualquier gerente es **recortar más gente**. La conclusión anterior ya dijo que eso no funciona: no podés bajar del piso, y automatizar más te empeora las dos cosas. ¿Qué queda?

**Queda bajar λ.** Mirá el mismo proyecto —misma gente, misma automatización, misma inversión— cambiando *solamente* dónde corre la IA y si hay plan B:

| Arquitectura | λ | IDA | Ahorro | Recupero |
|---|---|---|---|---|
| Una sola nube, sin plan de contingencia | 1,50 | 58 | $2.457 | 20 meses ❌ |
| Una sola nube, con plan de contingencia | 1,30 | 50 | $2.703 | 19 meses ❌ |
| Multi-cloud, con plan de contingencia | 1,10 | 42 | $2.948 | 17 meses ✅ |
| **IA local, con plan de contingencia** | **1,02** | **39** | **$3.047** | **16 meses** ✅ |

No cambió **nada** del negocio entre la primera fila y la última. No se automatizó más, no se despidió a nadie extra, no se negoció mejor precio de tokens. Lo único que cambió es **dónde vive la IA y si hay plan B**. Con eso solo, el proyecto pasa de reprobar (20 meses) a aprobar (16), y el IDA cae de 58 a 39.

> **Cuando el business case de automatización no cierra, la palanca correcta casi nunca es recortar más gente: es bajar el riesgo de la arquitectura.** Es la única decisión que mejora las tres cosas a la vez — sube el ahorro, acorta el recupero y baja la dependencia.

### 6.3 · Cómo se aplica fuera de una oficina: banco y retail

El modelo se explica con horas de oficina, pero donde más falta hace es donde hay **puestos físicos de atención**.

**Retail — cajas automáticas vs cajas con persona**

| Variable | Qué es en una caja de supermercado |
|---|---|
| **a** | % de transacciones que la caja automática procesa sola |
| **r** | Las que exigen humano sí o sí: verificación de edad (alcohol, tabaco), devoluciones, productos sin código, accesibilidad |
| **η** | El autoservicio es más lento que un cajero entrenado y genera más merma por errores y hurto |
| **λ** | Si se cae el software de punto de venta, ¿podés seguir vendiendo? |
| **P_min** | **Cuántas cajas con persona necesitás para sostener la venta en hora pico si el autoservicio no funciona** |

**Banco — cajeros automáticos y app vs ventanilla**

| Variable | Qué es en una sucursal |
|---|---|
| **a** | % de operaciones que se resuelven por cajero automático o app |
| **r** | Apertura de cuenta presencial, reclamos, efectivo sobre umbrales, atención obligatoria por accesibilidad |
| **λ** | Si se cae el core bancario o la app, ¿tenés ventanilla? Para un banco no es comercial: es un evento regulatorio |
| **P_min** | **Cuántas ventanillas humanas necesitás para no incumplir la normativa** |

En banca el modelo funciona incluso mejor, porque **r deja de ser una estimación**: no lo adivinás, lo leés de la normativa del regulador. Es el único parámetro que puede tener respaldo legal en lugar de criterio.

#### ⚠️ La trampa al aplicarlo: el factor de cobertura

**H_min se mide en horas de trabajo, no en puestos simultáneos.**

Si alguien dice *"necesito 3 cajas siempre abiertas"* y carga `H_min = 3 × 160 = 480 h`, el modelo devuelve **3 personas**. Está mal por más del doble: el local abre **360 horas al mes** (12 h × 30 días) pero **una persona trabaja 160**. Tres puestos cubiertos 360 horas son 1.080 horas de trabajo.

```
factor de cobertura = horas de operación del canal ÷ horas que trabaja una persona
P_min = puestos simultáneos × factor de cobertura
```

| Canal | Horas operación/mes | Factor | 3 puestos simultáneos = |
|---|---|---|---|
| Retail, 12 h × 30 días | 360 | 2,25 | **7 personas** |
| Sucursal de banco, 8 h × 22 días | 176 | 1,10 | **4 personas** |
| Guardia 24/7 (gas, energía, salud) | 720 | 4,50 | **14 personas** |

> **Tres puestos no son tres personas. En un canal 24/7 son catorce.** Ese factor de 4,5 es la razón por la que las guardias de servicios críticos parecen sobredimensionadas y no lo están: cubrir un puesto las 24 horas requiere cuatro turnos y medio de gente distinta.

Si la demanda no es pareja, calculá H_min franja por franja: `(puestos en pico × horas de pico + puestos fuera de pico × horas fuera de pico) × días`, más un margen por granularidad de turnos.

---

## 7. Los límites del modelo

Ningún modelo es honesto si no dice qué *no* hace.

**1 · Supone que la gente que conservás todavía sabe hacerlo.** El piso asume que pueden ejecutar el proceso manual el día que haga falta. Si hace ocho meses que la IA hace todo y ellos solo revisan, no van a poder: son **guardia pasiva**, y la guardia pasiva se oxida. Mantener la capacidad exige **simulacros periódicos de operación manual** —como un simulacro de incendio— y eso cuesta horas que no están en ninguna fórmula. Un P_min de papel no salva a nadie.

**2 · Supone que el know-how sigue adentro.** No alcanza con tener gente disponible: tiene que quedar quién sepa **cómo se trabajaba antes**. Si en el camino se fueron los que conocían el proceso viejo, el piso existe en la planilla y no en la realidad. Documentar el proceso manual es parte del seguro.

**3 · Mide costo y continuidad, no ingresos.** Para operaciones críticas eso es lo correcto: en una guardia de gas o energía no hay ingreso que justificar, hay una obligación legal de tener gente 24/7 — y el modelo sirve justamente para calcular cuánta. Pero si tu caso es comercial y automatizar genera ventas nuevas (atención 24/7, más capacidad en pico), ese ingreso **no entra acá** y hay que sumarlo por afuera.

**4 · Modela la convivencia permanente, no la degradación temporal.** La convivencia humano-IA **sí está**, y vive en **r**: si de 1.000 horas hay 200 que necesitan la firma de un abogado, un ingeniero o un arquitecto, cargás `r = 20%` y el modelo entiende que esas 200 nunca se automatizan —la IA hace el trabajo, el profesional firma—. Lo que **no** sabe representar es que la IA no se caiga del todo pero funcione peor dos semanas: más lenta, con más errores, con límite de consultas. El modelo es binario, la realidad no.

> **Cómo leer estos límites:** ninguno invalida el modelo, y los cuatro empujan en la misma dirección — **hacia arriba**. Un piso que no se entrena, un know-how que se fue y una degradación no contemplada hacen que necesites **más** gente, no menos. Si el modelo te da un número, tratalo como el **mínimo del mínimo**.

---

## 8. Cierre: la conjetura

Los bancos no eligen cuánto capital de reserva tienen: **Basilea** se los exige. Mi conjetura es que vamos hacia lo mismo con la IA: las empresas de servicios críticos van a tener que demostrar una **reserva mínima de capacidad humana** —un P_min auditado y un IDA declarado— igual que hoy declaran capital. En Europa, **DORA** ya obliga al sector financiero a gestionar el riesgo de dependencia de proveedores tecnológicos; extenderlo de "sistemas" a "personas" y de finanzas a toda industria crítica es el paso natural.

Las dos preguntas para llevarte:
1. **¿Cuál es tu piso?** ¿Con cuánta gente operás mañana sin IA?
2. **¿Cuál es tu IDA?** ¿Cuán rehén sos de tu arquitectura?

---

## 🧮 Calculadora

[**Abrí la calculadora interactiva**](https://cesarriat.com/modelo-ida) para cargar los números de tu empresa y obtener tu dotación mínima, tu IDA y tu payback en tiempo real. Todo corre en tu navegador: no se envía ningún dato.

Qué trae:

- **Costo de la IA por mes** como dato de entrada, que es el número que realmente conocés (tu factura), con un asistente que lo arma componente por componente si usás API o servidor propio.
- **Diagrama de flujo interactivo** en la pestaña *Fórmulas*: hacés clic en un módulo y ves hacia dónde va, o clic en una respuesta y ves todo lo que la construye.
- **Asistente de horas mínimas** que traduce "necesito 2 puestos cubiertos" a la cantidad real de personas según el horario de tu operación.
- **Simulación de Montecarlo** con 10.000 escenarios, **comparador local vs nube** e **informe descargable en PDF** con resumen ejecutivo, análisis de ROI y gráficos.

## 📄 Licencia
MIT — usalo, adaptalo, citá la fuente. Si lo aplicás en un caso real, me encantaría saberlo.

## 🙋 Autor
**César Riat** — Consultor en IA · [cesarriat.com](https://cesarriat.com)

*Cuando publiques el artículo en Medium, reemplazá el `#` del link de arriba por la URL real.*
