# Modelo IDA — ¿Cuánta gente necesita tu organización el día que la IA no esté?

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22070415.svg)](https://doi.org/10.5281/zenodo.22070415)

> Una fórmula para calcular tu **dotación mínima de continuidad** y un **Índice de Dependencia de IA (IDA)** para medir cuán expuesta está tu organización si la IA deja de estar disponible.

**No hace falta que sea una empresa.** El modelo pregunta por un área, unas horas de trabajo y una operación que no puede parar — eso existe en cualquier organización. Sirve para un call center, un banco, un retail o una transportadora de gas, y sirve igual para las que no venden nada:

| Organización | El área | Lo que no puede parar |
|---|---|---|
| **Una escuela** que automatiza corrección de exámenes, informes y comunicación con familias | El equipo docente y administrativo | Que las clases sigan y que las notas salgan aunque el sistema no esté |
| **Un hospital público** que automatiza triaje o turnos | Admisión y guardia | La atención de urgencias, que es obligación legal |
| **Un municipio** que automatiza atención al vecino | Mesa de entradas | Los trámites con plazo legal |

En la escuela, `P` son los docentes del área, `H_min` son las horas de clase y de corrección que hay que sostener sí o sí, y `r` es lo que un docente tiene que firmar personalmente por reglamento — una nota final, por ejemplo. La cuenta es la misma.

**Qué es y qué no es.** Se usa **antes de invertir**, para decidir. **No** es un tablero de monitoreo en tiempo real ni reemplaza la plataforma con la que operás: esas ejecutan la mitigación cuando algo falla, y este modelo es el que te dice cuánto vale la pena gastar en ellas.

**Contesta tres preguntas:**

| | Pregunta | Resultado |
|---|---|---|
| **Cuánta gente** | ¿Con cuántas personas seguís operando si la IA no está? | `P'` — el piso del que no podés bajar |
| **Si conviene** | ¿Cuánto ahorrás de verdad y en cuántos meses se paga? | `S` y `T` — más el techo de inversión |
| **Cuán expuesto** | ¿Qué tan rehén quedás de tu proveedor? | `IDA` — de 0 a 100 |

**[Probá la calculadora interactiva](https://modelo-ida.web.app)** · [Read this in English](https://modelo-ida.web.app/en) · Autor: [César Riat](https://cesarriat.com)

---

## 1. El problema

Hoy un call center se puede automatizar al 100% con IA. Técnicamente no queda ninguna tarea que un agente no pueda hacer —leer un email, responder por voz, por WhatsApp, contestar mensajes en redes sociales—: atender, resolver, escalar, registrar. La pregunta ya no es "¿se puede?".

La pregunta es otra: **¿qué pasa si de un día para otro no podés usar IA?**

Puede pasar por muchos caminos: se cae el proveedor de nube, el modelo que usás se discontinúa, el precio cambia 10 veces, una regulación nueva te prohíbe procesar datos afuera del país, o te cortan el servicio por una disputa comercial.

Y acá está el punto ciego: cuando una empresa automatiza, calcula cuánta gente puede reducir. **Nadie calcula cuánta gente tiene que conservar.** Son dos números distintos, y el segundo es el que te salva.

Los marcos que existen hoy —las normas de continuidad de negocio como ISO 22301, la nueva ISO/IEC 42001 de gestión de IA, los análisis de impacto y los mapas de dependencia— te ayudan a *identificar* el problema. Lo que no te dan es el número: cuántas personas, cuánta inversión tiene sentido, cuán expuesto estás. Este artículo propone esa cuenta.

Y aplica a cualquier industria, aunque pega distinto según la criticidad:

| Industria | Si la IA se cae... | Severidad |
|---|---|---|
| **Call center** | Perdés ventas y clientes se enojan | Recuperable |
| **Retail** | Góndolas vacías o precios absurdos en fecha pico | Alta |
| **Banco** | Evento regulatorio, no solo comercial | Crítica |
| **Transportadora de gas** | Falla de seguridad pública, no de negocio | Extrema |

Mismo modelo, distinta severidad. Por eso la fórmula es general y los parámetros los pone cada empresa.


---

## 2. Cómo se arma la cuenta

Los datos que cargás en la calculadora pasan por **cuatro módulos**, y de ahí salen las **tres respuestas** del modelo:

![Diagrama de flujo del Modelo IDA: los datos alimentan cuatro módulos — Humano, Automatización, Riesgo, Continuidad — y estos producen tres respuestas — Dotación, Ahorro y recupero, IDA](assets/g5_diagrama_flujo.svg)

Esta es una foto fija. **En el sitio es un diagrama interactivo**: hacés clic en un módulo y ves hacia dónde va, o en una respuesta y ves de qué se alimenta — [probalo acá](https://modelo-ida.web.app/diagrama).

En texto, el mismo recorrido — los cuatro módulos no son fórmulas sueltas, cada uno produce **un número intermedio**, y esos cuatro números alimentan **tres resultados**. El modelo es un embudo, no una ecuación única:

Ojo con un atajo mental frecuente: no se salta directo del % de automatización al ahorro en dólares. En el medio pasa por P' — el modelo primero decide **cuánta gente te queda de verdad**, y recién con ese número calcula la plata. Por eso hay una flecha extra en el diagrama:

```
Lo que cargás          Los cuatro módulos            Los tres resultados
─────────────          ──────────────────            ───────────────────
P, h_p, N        →     Humano        → C_h          ┐
a, r, η          →     Automatización→ a_ef         ├→   P'   ¿con cuánta gente me quedo?
ρ, C_mes         →     Riesgo        → λ            ├→   S, T ¿conviene y en cuánto se paga?
H_min, R         →     Continuidad   → P_min,       ┘→   IDA  ¿cuán expuesto quedo?
                                       cobertura
I, M             →     (entran directo en S y T)

                       ...y además:  P'  ──────────→  S
                       (solo ahorrás el sueldo de quien podés liberar)
```

---

## 3. Los cuatro módulos

> **El caso que se sigue hasta el final: una cadena de farmacias.** Para que los números no queden en el aire, de acá en adelante todo se calcula sobre el mismo caso. Una cadena de farmacias tiene un **área de atención al cliente de 10 personas** que reciben consultas por **email, teléfono y WhatsApp**: si un remedio está en stock, si una obra social lo cubre, en qué sucursal retirarlo, por qué se rechazó una receta electrónica, seguimiento de un pedido a domicilio. Cada una trabaja 160 h al mes y entre todas cuestan **$16.000** de nómina.
>
> Quieren automatizar esa atención: **60%** del trabajo es automatizable, **20%** de eso necesita intervención humana obligatoria —lo que toca dosis, interacciones o una receta que hay que validar—, la IA rinde al **80%**, corren sobre **una sola nube sin plan de contingencia**, necesitan cubrir **640 h mensuales** pase lo que pase, y el proyecto cuesta **$50.000** de inversión más **$500** por mes de mantenimiento.

### Módulo Humano
```
Costo hora humana (Ch) = Nómina mensual ÷ Horas totales
```
Ejemplo: $16.000/mes, 10 personas, 1.600 h → **$10/hora**.

### Módulo Automatización
```
Automatización efectiva = a × (1 − r) × η
```

**Los tres, con un solo ejemplo: una distribuidora de gas que automatiza los reclamos por email.**

- **`a` — ¿qué puede hacer la IA?** Mirás qué llega y ves que la mayoría son consultas repetidas: cuándo pasa el técnico, cómo se lee la factura, cómo se pide un cambio de titularidad. Eso lo redacta sin problema. Coordinar una cuadrilla o interpretar la foto de un medidor roto, no. Si son **6 de cada 10 horas**, `a = 60%`. La pregunta es *¿puede?*, no *¿conviene?*.
- **`r` — ¿qué no tiene permitido hacer?** De esos mismos emails, algunos no se contestan con un robot aunque técnicamente se pudiera: "siento olor a gas", un aviso de acción legal, un corte de servicio con deuda. Tiene que intervenir una persona habilitada y queda registro de quién respondió. **1 de cada 5** → `r = 20%`. En banca o salud esto no se estima: se lee de la normativa.
- **`η` — ¿cuánto sale listo sin retocar?** No es qué tan inteligente es la IA, es cuánto **trabajo terminado** entrega. Le pasás 10 reclamos, vuelve con 10 respuestas, pero **2 hay que rehacerlas** (una cita mal el número de cuenta, otra promete una visita que no corresponde). Rindió como 8 de cada 10 → `η = 80%`. Nunca es 100% porque siempre queda alguien revisando; si nadie revisa, η no subió — subió el riesgo de mandarle algo mal a un cliente.

Los tres juntos: `0,60 × (1 − 0,20) × 0,80 = 38,4%`. La gasífera arrancó creyendo que automatizaba el 60% y el número real con el que hay que hacer las cuentas es **38,4%**.
- **r** — lo regulado (firma de médico, escribano): queda afuera sí o sí
- **a** — lo técnicamente automatizable del resto
- **η** — eficiencia real de la IA (70%–90%, nunca 100%)

Ejemplo: 0,60 × (1 − 0,20) × 0,80 = **38,4%**, no 60%. Primer baño de realidad.

**Un caso concreto: los emails de la farmacia.** Técnicamente se pueden contestar **el 100%** con IA: leer, entender, redactar, responder. Ese es tu `a` = 100%. Pero hay correos que **tienen que pasar por una persona sí o sí**: los que preguntan por dosis o interacciones entre medicamentos, los que llegan con una receta que hay que validar, los reclamos que pueden derivar en defensa del consumidor, y los que piden datos personales o de una obra social. Si eso es 1 de cada 5, tu `r` = 20%. Y de los que sí automatizás, la IA no acierta siempre: hay que revisar, corregir y reenviar. Si rinde como 8 de cada 10 personas, tu `η` = 80%.

`1,00 × (1 − 0,20) × 0,80` = **64%**. Arrancaste creyendo que automatizabas todo y en la práctica sacás dos tercios de la carga. Ese 64% es el número con el que hay que hacer las cuentas.

### Módulo Riesgo
```
Costo real de la IA = λ × Gasto mensual de IA
```

Seguí con la misma pyme del ejemplo: automatizaste el 38,4% de la carga y elegiste un proveedor de IA en la nube —una sola nube, sin backup en otro proveedor— que te factura $1.229 por mes. Todavía no armaste un plan de contingencia para el día que se caiga.

Esas dos decisiones tienen precio, aunque no aparezcan en la factura. **Dónde corre la IA** — elegís *una sola* de estas tres, son excluyentes:

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

Tu caso: nube única (+30%) y sin plan de contingencia (+20%) → λ = 1 + 0,30 + 0,20 = **1,50**.

El costo real de tu proyecto, para decidir si conviene, no es $1.229: es 1,50 × $1.229 ≈ **$1.843 por mes** (el modelo trabaja con el valor exacto, $1.228,80, antes de redondear para mostrarlo). La factura no cambia —seguís pagando $1.229—, pero el modelo te cobra $614 extra en la evaluación: es lo que te cobra el multiplicador de riesgo por la arquitectura frágil que elegiste. Ese costo no aparece en ninguna factura mensual — aparece entero, una sola vez, el peor día. El multiplicador lo reparte en cuotas para que una arquitectura frágil se vea cara *cuando todavía estás a tiempo de cambiarla*.

Es la lógica del seguro del auto: manejar sin seguro no sale más barato, sale igual hasta que chocás.

No hay arquitectura gratis, hay que elegir qué precio pagar. Si corrieras esa misma IA en tus propios servidores, λ bajaría mucho —menos riesgo— pero tendrías que poner la inversión inicial de armar y mantener esos servidores. Si te quedás en la nube de un solo proveedor, la inversión inicial es baja —pagás por mes, nada más— pero el riesgo es mayor porque quedás atado a ese proveedor. ¿Cuál conviene? Depende de cuánto volumen proceses: con poco volumen la nube sale más barata aunque sea más riesgosa; con mucho volumen, tu propia infraestructura empieza a compensar el riesgo que evitás. Ese es exactamente el trade-off que ves en números reales en la sección 5 (Casos extremos) y en la 7.2.

### Módulo Continuidad
```
Piso de continuidad (P_min) = Horas mínimas para operar sin IA ÷ Horas por persona
```

Ahora la pregunta incómoda: si mañana la IA se cae, ¿con cuánta gente seguís? No es cero, aunque hoy automatices el 38,4%.

Pensalo en modo degradado y calculá a ojo, no hace falta un estudio: *"¿cuántas horas por mes tengo que cubrir sí o sí, aunque no tenga IA?"*. *"Si se cae todo tengo que atender 800 llamados al mes, y una persona atiende 2 por hora"* → 400 horas. *"Y alguien tiene que revisar pedidos 8 horas por día"* → 240 horas más. Total ≈ 640 h/mes: ese es tu `H_min`.

Piso de continuidad = 640 horas ÷ 160 horas por persona = **4 personas**

Esas 4 personas son tu P_min: no importa que automatices el 100%, nunca vas a bajar de 4 en este equipo. Son las horas de la operación crítica en modo degradado, y **no dependen de la arquitectura**: la fórmula es `⌈H_min ÷ h_p⌉` y ahí no entra ni el proveedor ni λ. Correr la IA en tus propios servidores baja λ y acorta la caída, pero **no baja el piso** — mientras dure, seguís necesitando esas 4 personas. La arquitectura cambia el riesgo y el costo; el piso, nunca. Ese es justamente el punto del modelo.

> **Ojo: esto NO es lo mismo que la firma del médico o del escribano.** Son dos preguntas distintas y es donde más se confunde la gente.
>
> `r`, en el módulo Automatización, pregunta: *del trabajo que la IA podría hacer, ¿cuánto no puede por norma?* Es la firma del médico, del escribano, del auditor. Eso pasa **aunque la IA funcione perfecto**: hay tareas que legalmente no se delegan.
>
> `P_min`, acá, pregunta otra cosa: *si mañana la IA no está, ¿con cuánta gente sostengo lo que no puede parar?* No importa la firma: importa la **capacidad operativa**.
>
> Puede pasar que las dos cosas coincidan —el médico que firma es también el que sostiene la guardia— pero son cuentas separadas.

**Y una pregunta más: ¿hay respaldo fuera del área? → produce R**

```
cobertura = MÍNIMO( R ÷ P_min , 1 )      y 0 si P_min = 0
```

La aclaración del `P_min = 0` no es un tecnicismo: si declarás que **no tenés operación crítica** —que si la IA se cae no pasa nada urgente—, no hay piso que cubrir y el respaldo externo no tiene nada que descontar. La cobertura vale 0 y el IDA queda sin tocar. Sin esa aclaración la fórmula dividiría por cero.

El piso `P_min` mira solo hacia adentro del área. Pero una operación de 5 personas dentro de una empresa donde otras 20 saben hacer esa misma tarea **no está tan expuesta** como un call center de 200 donde nadie más sabe. **R** es esa gente: las personas de **fuera del área** que podrían cubrir la operación crítica el día que la IA no esté.

> **El error que hay que evitar: R no es la plantilla de la organización.** Toyota tiene unos 200.000 empleados y eso **no significa que R sea 200.000**. Si la tarea que automatizás es atender reclamos de garantía, R son las personas que **hoy, sin capacitación previa**, podrían sentarse a atender esos reclamos: quizás 30 en otras sucursales. Las otras 199.970 no cuentan, por más que estén en la nómina.
>
> La regla es simple: **si primero tenés que enseñarle, no cuenta.** R es capacidad disponible el día de la caída, no capacidad potencial.
>
> **La cuenta, con números.** La farmacia tiene un piso de 4 personas. Si en las sucursales hay cuatro farmacéuticos que todavía saben atender estas consultas, cargás `R = 4`:
>
> ```
> cobertura = 4 ÷ 4 = 100%     →   IDA = 58 × (1 − 1,00 × 0,7) = 17
> cobertura = 2 ÷ 4 =  50%     →   IDA = 58 × (1 − 0,50 × 0,7) = 37
> ```
>
> Lo que entra son **personas**, no un porcentaje ni un puntaje, y media cobertura descuenta la mitad. Con más respaldo del que necesitás la cuenta se topea sola: 8 sobre un piso de 4 sigue dando 100% y el mismo IDA 17, porque cubrir dos veces el piso no te cubre el doble.
>
> **Lo que R NO hace: bajarte la dotación.** Tener respaldo externo no cambia `P_min` ni `P'`. En la farmacia seguís conservando 7 personas, tengas 0 o 4 de respaldo; lo único que se mueve es el IDA. La razón es que los de afuera tienen su propio trabajo: si recortás el área confiando en ellos, el día que la IA se caiga rompés dos áreas en vez de una. **R reduce cuán expuesto estás, no cuánta gente necesitás.** Por eso mismo el descuento se topea en 0,7 y nunca llega a cero.
>
> **Y cómo se carga:** en la calculadora, antes del campo hay tres casillas con las preguntas de abajo. **Esas casillas no aportan ningún valor**, son una condición de todo o nada: si falta una sola, `R = 0` aunque escribas un número. El valor de R son personas — cuántas hay afuera que puedan cubrir — y de ahí sale `cobertura = R ÷ P_min`.
>
> **Y es el número más fácil de inflar de todo el modelo,** porque es el único que *baja* el índice. Por eso el modelo nunca deja que el respaldo lleve el IDA a cero, y por eso este número es el primero que hay que auditar cuando alguien muestra un IDA sospechosamente bajo (ver §9.2).


---

## 3.bis El precio que pagás hoy no está atado a un costo

El precio del token es una decisión comercial de tu proveedor, es decir que no se mueve por lo que a él le cuesta atenderte sino por dónde quiere estar parado en el mercado.

Los números públicos alcanzan para verlo. Según lo reportado en la prensa financiera durante 2026, OpenAI proyecta cerrar el año con unos **US$ 25.000 millones de facturación** y una **pérdida del orden de US$ 14.000 millones**, es decir que gasta bastante más de lo que factura y la diferencia la ponen los inversores. Sin embargo Anthropic recorrió el camino inverso, de un margen bruto negativo en 2024 a terreno positivo en 2026 según los mismos reportes.

> **Qué dicen y qué no dicen esos números.** Esas cifras son del **resultado total de la empresa**, que incluye entrenar modelos nuevos, investigación, sueldos y construcción de infraestructura. **No son el costo de atender tu consulta.** Con lo publicado no se puede calcular cuánto le cuesta a un proveedor servirte un millón de tokens, y cualquiera que diga lo contrario está inventando.
>
> Lo que sí muestran, y alcanza de sobra, es que **ingresos, costo de infraestructura, inversión y estrategia comercial no se mueven juntos**. Es decir que el precio que ves hoy no es un piso técnico: es una posición comercial, y las posiciones comerciales cambian.
>
> Fuentes: reportes de prensa financiera de 2026 sobre resultados de [OpenAI](https://valueaddvc.com/blog/openai-revenue-2026-25b-arr-a-20-9b-leaked-loss-and-why-anthropic-just-passed-it) y sobre los [dos modelos de negocio](https://www.forbes.com/sites/paulocarvao/2026/05/21/anthropic-openai-enterprise-ai-profitability/). No son estados contables auditados y cambian rápido: tomalos como orden de magnitud.

**Qué le pasa a la farmacia si el precio se mueve.** Mismo proyecto, misma gente, misma automatización; se mueve **solo el precio**:

| Escenario | Gasto de IA | Ahorro | Recupero |
|---|---|---|---|
| Precio de hoy | $1.229/mes | $2.457 | **20 meses** |
| Si subiera 56% | $1.917/mes | $1.425 | **35 meses** |
| Si se duplicara | $2.458/mes | $613 | **82 meses** |

Pasa de aprobado a inviable por una decisión que toma otro, en otro país y sin avisarte. Sin embargo mirá qué no cambió: **el piso de continuidad sigue siendo 4 personas en los tres casos**, porque el piso no se calcula con el precio del token sino con las horas que la operación no puede dejar de cubrir.

> **La conclusión práctica: automatizá, pero no armes tu dotación sobre un precio que no controlás.** Si el número solo cierra con la tarifa de hoy no tenés un proyecto, tenés una apuesta a que esa tarifa no cambie. La dotación mínima es la parte de la decisión que **sobrevive a un cambio de precio**, y por eso es la que hay que calcular primero.

---

## 4. Cómo se unen: los resultados

### Resultado 1 — Cuánta gente conservar (P')
```
P' = MÁXIMO entre:
   (a) ⌈ Personas actuales × (1 − Automatización efectiva) ⌉   ← la cuenta económica
   (b) Piso de continuidad P_min                                ← la cuenta de supervivencia
```

Con esos dos números en la mano —38,4% de automatización efectiva y un piso de 4 personas—, el modelo hace **dos cuentas distintas y se queda con la más grande**:

1. **Cuenta económica:** si automatizás el 38,4%, te "sobra" ese 38,4% de la capacidad de trabajo → `10 × (1 − 0,384) = 6,16 → 7 personas` (redondeo hacia arriba: no existe 6,16 empleados).
2. **Cuenta de supervivencia:** el `P_min` que acabás de calcular en el módulo Continuidad → 4 personas.
3. **`MÁXIMO(7 , 4) = 7`.**

**¿Por qué la más grande?** Porque las dos son condiciones que tenés que cumplir *al mismo tiempo*: al menos 7 para el trabajo diario, al menos 4 para sobrevivir sin IA. Solo el mayor cumple las dos.

En este ejemplo manda la economía. Pero si automatizás al 90%, la cuenta económica da `⌈10 × 0,10⌉ = 1` y entonces `MÁXIMO(1 , 4) = 4`: **ahí el piso toma el control**. Por más que automatices el 100%, nunca bajás de 4. Esa diferencia es tu **reserva de capacidad humana**.

### Resultado 2 — Si conviene o no (S y T)
```
S = (P − P') × sueldo − λ × Gasto mensual de IA − Mantenimiento
T = Inversión ÷ S
```

Ya sabés que de tu equipo de 10 te quedan 7. Ahora la pregunta es cuánto ahorrás con eso — y acá importa el atajo que marcamos antes: fijate que S **arranca con P'**, el resultado anterior: solo ahorrás el sueldo de la gente que efectivamente podés liberar.

1. **Cuánta gente liberás de verdad:** `P − P' = 10 − 7 = 3 personas`. No son 3,84 (el 38,4% de 10): no se despiden fracciones de persona, y si el piso se activa liberás todavía menos.
2. **Ahorro en sueldos:** cada persona cuesta `N ÷ P = $1.600/mes` → `3 × $1.600 = $4.800`.
3. **Costo de la IA:** `1.600 × 0,384 × 1,5 × $2 = $1.843/mes`. Acá entra λ: la factura dice $2/h, el riesgo la convierte en $3/h.
4. **Ahorro:** `$4.800 − $1.843 − $500 = $2.457/mes`.
5. **Para qué sirve S:** es el semáforo y el divisor del recupero. Si S ≤ 0, automatizar cuesta más de lo que ahorra. Si S > 0, `T = $50.000 ÷ $2.457 = 20 meses`. Regla por defecto: **arriba de 18 meses, no avances** — este proyecto, con la cuenta honesta, no pasa. Ese plazo lo elegís en la calculadora: es política de inversión de cada empresa, no una constante del modelo.

> #### La trampa que esta fórmula evita
>
> La cuenta intuitiva es `horas automatizadas × costo hora humana`: 614,4 h × $10 = **$6.144** de ahorro en sueldos. Es falso: vos no pagás horas, pagás sueldos. Automatizar 3,84 personas-equivalente cuando solo podés echar 3 **no ahorra 3,84 sueldos, ahorra 3** — o sea **$4.800**, no $6.144. Esas dos cifras son ahorro *bruto*: todavía no restamos la IA ni el mantenimiento.
>
> Cuando el piso de continuidad se activa la brecha explota. Con automatización al 100% y piso de 4, esa misma cuenta ingenua —ahora ya neta de IA y mantenimiento, para poder compararla con el resultado final— promete **$10.700/mes**; el ahorro real es **$4.300/mes**. Los $6.400 de diferencia son los cuatro sueldos que seguís pagando por continuidad mientras la IA hace ese trabajo. **Esa es la prima de seguro operativo, y el modelo ahora te la cobra.**

> #### ↓ El corolario incómodo: existe un óptimo de automatización
>
> Una vez que chocaste el piso, cada punto extra de automatización **suma factura de IA pero no libera a nadie más**. Desde ahí, automatizar más te **baja** el ahorro y te **sube** el IDA: quedás más pobre y más dependiente a la vez.
>
> | Autom. efectiva | Ahorro "ingenuo" | Ahorro real | IDA |
> |---|---|---|---|
> | 60% (óptimo de este caso) | $6.220 | **$6.220** | 90 |
> | 80% | $8.460 | $5.260 | 100 |
> | 100% | $10.700 | $4.300 | 100 |
>
> El máximo de automatización nunca es el óptimo de automatización. **Con una salvedad, que vale para todo el modelo:** esto pasa así cuando la IA se paga por hora. Con costo fijo el ahorro no baja, se aplana — y el IDA sube igual (ver 7.1).

**Una aclaración honesta sobre λ:** S es el *ahorro ajustado por riesgo*, no el flujo de caja contable. λ no es un cheque que le firmás a tu proveedor: es el multiplicador de riesgo, un recargo implícito que el modelo aplica para castigar arquitecturas frágiles al decidir. Tu contador va a ver un ahorro mayor (el mismo número con λ=1); tu director de riesgo va a querer ver este.

### Resultado 3 — Índice de Dependencia de IA (IDA)
```
IDA = MÍNIMO( Automatización efectiva × λ × (1 − cobertura × 0,7) × 100 , 100 )
```
Con el ahorro ya resuelto —$2.457 por mes, se paga en 20 meses— falta la otra pregunta: ¿qué tan expuesto quedaste?

`0,384 × 1,50 × (1 − 0 × 0,7) × 100 = 58` → zona amarilla. En el ejemplo no hay respaldo externo declarado (R = 0), así que el tercer factor vale 1 y no cambia nada.

**Qué hace el tercer factor y por qué nunca llega a cero.** Sin este término el índice era **ciego al recorte**: una sola persona automatizada en una empresa donde otras veinte saben hacer la tarea daba *el mismo IDA* que un call center donde nadie más sabe. Son situaciones opuestas y el índice las leía igual. Todos estos casos corren sobre una sola nube sin plan de contingencia (λ = 1,50):

| Situación | a_ef | P_min | R | Cobertura | IDA |
|---|---|---|---|---|---|
| Área de 1 persona automatizada al 100%, nadie más sabe | 100% | 1 | 0 | 0% | **100** |
| La misma área, pero 20 personas afuera saben hacerlo | 100% | 1 | 20 | 100% | **45** |
| Call center de 200, 60% automatizado, nadie más sabe | 60% | 80 | 0 | 0% | **90** |
| El mismo call center, con 40 que pueden cubrir | 60% | 80 | 40 | 50% | **59** |

**El descuento se topea en 0,7 a propósito.** Aunque tengas respaldo de sobra, la caída igual te cuesta: esa gente **abandona su propio puesto** para venir a cubrir —así que la interrupción se propaga a otra área— y hace tiempo que no hace esta tarea todos los días. El respaldo externo puede bajarte el IDA hasta un 70%, nunca hasta cero. **Nadie queda inmune por tener gente de reserva.**

El `MÍNIMO` no es decorativo: con automatización alta y arquitectura frágil el producto se pasa de 100 (el techo teórico es 165: a_ef=1 con λ máximo de 1,65 — una sola nube, sin plan de contingencia y datos sensibles afuera). Todo lo que supere 100 ya es "máxima dependencia posible", así que el índice se topea para que la escala 0–100 signifique siempre lo mismo.

| IDA | Zona | Qué significa |
|---|---|---|
| **< 30** | Resiliente | Una caída de IA es una molestia |
| **30–60** | Vigilancia | Necesitás piso calculado y simulacros manuales |
| **> 60** | Crítico | Tu operación es rehén de tu proveedor |

**Por qué el IDA no incluye la plata.** Es deliberado: ahorrar y estar expuesto son cosas distintas. Podés tener un proyecto que ahorra bien y recupera rápido —excelente negocio— y estar igual en zona amarilla de dependencia. Si metieras el dinero adentro del IDA, un ahorro grande te *taparía* el riesgo y el índice te diría que estás bien justo cuando más frágil estás. El dinero ya tiene su fórmula: es S.

Dos empresas con la misma automatización pueden tener IDA muy distinto: 38,4% con nube única (λ=1,5) → **IDA 58**; la misma con IA local (λ=1,02) → **IDA 39**. **La dependencia no es cuánto automatizaste: es cuánto automatizaste por cuán frágil es lo que te sostiene.**

### Las fórmulas en una sola línea

Reemplazando cada módulo por su definición, cada resultado queda en función directa de lo que cargás:

```
P'  = MÁXIMO( ⌈P × (1 − a(1−r)η)⌉ , ⌈H_min ÷ h_p⌉ )

S   = [ P − MÁXIMO( ⌈P × (1 − a(1−r)η)⌉ , ⌈H_min ÷ h_p⌉ ) ] × N/P
      − (1+Σρ) × C_mes
      − M

IDA = MÍNIMO( a(1−r)η × (1+Σρ) × [1 − MÍN(R ÷ ⌈H_min÷h_p⌉ , 1) × 0,7] × 100 , 100 )
```

Con `⌈H_min÷h_p⌉ = 0` —sin operación crítica que sostener— el término de cobertura vale 0 y el IDA queda `MÍNIMO(a_ef × λ × 100, 100)`.

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
| $25.000 | $2.457 | 58 | 10 meses ✓ |
| $50.000 | $2.457 | 58 | 20 meses ✗ |
| $200.000 | $2.457 | 58 | 81 meses ✗ |

El ahorro no se mueve, el IDA no se mueve. Y está bien: la inversión es un gasto de una sola vez, no cambia cuánta plata te entra por mes ni cuán dependiente quedás.

> **La asimetría que importa:** un error en la **inversión** lo pagás una vez. Un error en el **costo operativo** te acompaña todos los meses para siempre. Si tenés poco tiempo para revisar supuestos, **revisá C_mes antes que I**.

#### El punto ciego: qué esconde el gasto mensual

La calculadora te pide el **gasto mensual** de IA porque es el número que conocés: sale de tu factura o de una proyección. Internamente guarda el **costo por hora automatizada**, para que si después cambiás cuánto automatizás, la factura escale sola. Eso importa porque la forma de esa curva es el hallazgo central del modelo, y **depende de qué tipo de costo tengas**: con API el gasto sube con la automatización y pasado el piso el ahorro empieza a bajar; con servidor propio el gasto no se mueve y el ahorro se aplana en lugar de caer. Las dos formas son correctas — son estructuras de costo distintas, no una bien y otra mal (ver 7.1).

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

Para el proyecto de 10 personas del ejemplo: con API DeepSeek el ahorro es **$4.168/mes** (12 meses); con servidor propio contando todo es **−$4.288/mes** y no recupera nunca. Las dos cifras usan el **mismo λ (1,02)** a propósito, para que la comparación aísle el costo y no mezcle el riesgo; si a la API le cargaras su λ real de nube única (1,50), su ahorro sería $4.106 y la conclusión no se mueve.

### Ejemplo completo
Pyme: 10 personas, $16.000 nómina, 160 h c/u (1.600 h/mes), a=60%, r=20%, η=80%, nube única sin contingencia (λ=1,5), IA $2/h, H_min 640 h, inversión $50.000, mant. $500/mes.
- Automatización efectiva: `0,60 × 0,80 × 0,80` = **38,4%**
- Dotación: `MÁXIMO(7 , 4)` = **7 personas** (el piso de 4 no se activa) → liberás **3**
- Ahorro: `3 × 1.600 − 1.843 − 500` = **$2.457/mes** → recupero **20 meses** ✗
- **IDA 58 — vigilancia.**

Este ejemplo es deliberado: con la cuenta ingenua el proyecto parecía cerrar en 13 meses y daba luz verde. Con la cuenta honesta —que solo acredita los sueldos realmente liberados— se va a 20 meses y **no pasa el filtro**. La respuesta correcta no es cancelar: es bajar λ (segundo proveedor, plan de contingencia) o bajar la inversión inicial, y volver a correr el número.


---

## 5. Aprendé los parámetros con casos extremos

Un buen modelo se reconoce en los bordes: cuando lo empujás al extremo, tiene que decir cosas sensatas. Y de paso, cada extremo te enseña una variable.

### Extremo A — "Automatizo el call center al 100%" → te enseña el piso **P_min**

La cuenta económica ingenua dice: si automatizás todo, necesitás cero personas. El modelo dice: no. La dotación cae con la automatización *hasta que choca con un piso* —el mínimo de gente para sostener la operación crítica sin IA— y ahí se planta, aunque automatices el 100%.

![Piso de continuidad](assets/g1_piso_continuidad.svg)

La diferencia entre lo que dice el Excel y lo que dice el piso es tu **prima de seguro operativo**: gente que parece "de más" hasta el martes que se cae la nube.

Y esa prima **tiene precio, no es gratis**: son sueldos que seguís pagando mientras la IA hace ese trabajo. El modelo se los cobra al proyecto en la fórmula de ahorro (ver §4), que es justamente lo que casi ningún business case de automatización hace.

### Extremo B — "Una sola nube y sin plan B" → te enseña el riesgo **λ**

Dos empresas automatizan lo mismo y pagan el mismo precio por token. Una corre todo sobre un solo proveedor, sin contingencia. La otra reparte entre dos y tiene procedimiento manual ensayado. ¿Pagan lo mismo? En la factura sí; en la realidad no. La primera "maneja sin seguro": el riesgo no aparece en la factura mensual, aparece todo junto el día del choque.

Ese riesgo se convierte en un recargo sobre el costo de la IA: el **multiplicador λ**. Si λ crece tanto que el costo real de la hora de IA alcanza al de la hora humana, la curva de ahorro se aplana. Si lo supera, **pagás por automatizar**.

![Ahorro mensual según cuánto automatices, para cuatro niveles de riesgo λ: todas las curvas alcanzan su máximo en el piso de continuidad y después bajan](assets/g4_riesgo_lambda.svg)

Fijate que **las cuatro curvas tienen su máximo en el mismo lugar**: el 60%, donde el piso toma el control. λ no mueve el óptimo, mueve *cuánto ganás* en ese óptimo — y con la hora de IA al precio de la hora humana, la curva se hunde y automatizar te cuesta plata.

### Extremo C — "Monto DeepSeek local para automatizar los mails" → te enseña la inversión **I**

> **Ojo, acá cambia el volumen a propósito: los extremos C y D no son la farmacia.** La farmacia automatiza unas 614 h por mes; estos dos muestran qué pasa mucho más abajo (una tarea de 60 h) y mucho más arriba (una operación a escala), que es donde la decisión se da vuelta.

El caso que más confunde, porque mezcla dos verdades. Y acá van números reales, verificados en agosto de 2026.

**Verdad 1:** correr la IA en tus propios servidores **casi elimina el riesgo**. Nadie te corta el servicio, no dependés de ninguna nube, tus datos no salen del edificio. λ baja a casi 1. El modelo abierto de referencia hoy es **DeepSeek V4-Flash** (284B parámetros, licencia MIT): necesita ~175 GB de VRAM y entra en **2× GPUs H200**. Alquilar ese servidor 24/7 cuesta del orden de **USD 5.170 por mes**, fijo, uses lo que uses.

**Verdad 2:** ese costo es fijo y brutal si tu volumen es chico. La pregunta que la fórmula responde: **¿para qué tarea lo montás?**

Comparemos las tres opciones para automatizar emails que consumen **15 horas por semana** (~60 h/mes), asumiendo ~1 millón de tokens por hora de trabajo:

| Opción | Costo mensual para la tarea de emails | Riesgo (λ) |
|---|---|---|
| **API DeepSeek V4-Flash** ($0,14 / $0,28 por millón) | **~$12,60/mes** | Alto (nube única) |
| **API Gemini 3.6 Flash** ($1,50 / $7,50 por millón) | **~$270/mes** | Alto (nube única) |
| **DeepSeek local** (2× H200) | **~$5.170/mes** | Casi nulo |

Esos ~$12,60 salen de 60 M de tokens al mes (60 h × 1 M) repartidos mitad entrada, mitad salida. Montar el servidor local para los emails cuesta **410 veces más** que usar la API de DeepSeek. Pagás $5.170 para reemplazar $12,60 de API. Absurdo, por más que el riesgo local sea casi cero: la tarea es demasiado chica para justificar el fierro.

> **Y el fierro no es el costo completo.** Esos $5.170 son solo el alquiler. Correr IA propia necesita además **electricidad** (~$250/mes con 2,1 kW constantes) y sobre todo **alguien que la mantenga**: un sysadmin o perfil de MLOps, del orden de $3.000/mes. Total real **$8.420/mes**, y la brecha contra la API salta de 410× a **668×**.
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

## 6. Para los más avanzados: Montecarlo

Todo lo de arriba usa números fijos: exactamente $1.229 por mes de IA, exactamente 640 horas de piso, exactamente 38,4% de automatización. Pero en la vida real esos números se mueven de mes a mes: el token cambió 10× en dos años y tu eficiencia real no la conocés hasta el tercer mes.

Montecarlo es, en el fondo, una idea simple: en vez de correr la cuenta una sola vez con el número "promedio", la **simulación de Montecarlo** la corre **10.000 veces**, moviendo un poco cada variable dentro de un rango razonable cada vez —como si probaras 10.000 futuros posibles para tu proyecto— y te quedás con el promedio de esos 10.000 resultados.

![Montecarlo](assets/g3_montecarlo.png)

El resultado deja de ser *"recuperás en 20 meses"* y pasa a ser *"25% de probabilidad de recuperar en menos de 18 meses; mediana 22 entre los que sí recuperan"*. Los porcentajes se calculan sobre las 10.000 corridas completas — incluyendo el ~7% de escenarios donde el ahorro es negativo o el recupero pasa de 60 meses, que serían fáciles de barrer bajo la alfombra. Montecarlo no reemplaza la fórmula: la alimenta.

Ese 25% es incómodo y por eso vale la pena: dice que con estos rangos el proyecto es más una apuesta que un plan. La palanca para moverlo casi nunca es automatizar más — es bajar λ o bajar la inversión inicial.

---

## 7. Conclusiones

**Dónde terminó la farmacia.** El área arrancó con **10 personas** atendiendo email, teléfono y WhatsApp, y el proyecto automatiza el 38,4% efectivo del trabajo: **se conservan 7 personas y el proyecto reemplaza a 3**.

Tres puestos, no 3,84: la automatización cubre el equivalente a 3,84 personas de trabajo, pero solo se dejan de pagar **3 sueldos**, porque no existe el 0,84 de un empleado. Esa fracción sigue costando plata y ya no ahorra nada. Y el piso de continuidad es de **4 personas**: como la cuenta económica dejó 7, el piso todavía no se activó, pero **el margen es de solo 3**. Si el año que viene automatizan un poco más y bajan de 4, el modelo deja de ser una calculadora de ahorro y pasa a ser un aviso.

Cuatro son las que importan (7.1 a 7.4): contraintuitivas, aparecen recién cuando hacés la cuenta honesta, y van en contra de lo que se recomienda hoy en casi cualquier presentación sobre IA. La quinta (7.5) es cómo llevar todo esto a un canal físico —una caja, una ventanilla, una guardia—, que es donde el modelo más sirve.

### 7.1 · El máximo de automatización no es el óptimo

La intuición dice que cuanto más automatices, más ahorrás. Es falso, y el modelo muestra exactamente dónde deja de serlo.

Hay una cantidad de gente que **no podés soltar**: el piso de continuidad. Una vez que llegás a ese piso, cada punto adicional de automatización **suma factura de IA pero ya no libera a nadie más**. Seguís pagando los mismos sueldos y encima pagás más IA.

| Automatización efectiva | Promesa ingenua | Ahorro real | Recupero | IDA |
|---|---|---|---|---|
| **60% — el óptimo de este caso** | $6.220 | **$6.220** | **8 meses** | 90 |
| 80% | $8.460 | $5.260 | 10 meses | 100 |
| 100% | $10.700 | $4.300 | 12 meses | 100 |

Leé la última fila con calma: al automatizar el 100%, la cuenta ingenua promete **$10.700/mes** y la realidad da **$4.300**. Los $6.400 que faltan son los cuatro sueldos del piso, que seguís pagando mientras la IA hace ese trabajo.

> **Si tu IA es de costo fijo, cambia una cosa.** Todo lo de arriba supone que pagás la IA por hora, que es lo que hacés con una API. Si tenés servidor propio la factura es la misma automatices 60% o 100%, así que pasado el piso el ahorro no baja: se queda quieto. Se comprueba en la calculadora poniendo el asistente de costo en servidor propio y moviendo el deslizador — el gasto mensual no se mueve y el ahorro se aplana. Eso no te deja sin consecuencia, solo cambia cuál es: automatizar de más ya no te empobrece, sin embargo el IDA sigue subiendo igual, de 90 a 100 en la misma tabla. Es decir que comprás dependencia a cambio de nada. Con API perdés plata y resiliencia juntas; con costo fijo perdés solo resiliencia, que es más difícil de ver en un balance y más caro de arreglar después.

> **Pasado el piso, automatizar de más te deja más pobre y más dependiente al mismo tiempo** —con costo por hora—: el ahorro baja de $6.220 a $4.300, el recupero se estira de 8 a 12 meses y el IDA sube de 90 a 100. Las tres cosas empeoran juntas — y se llega ahí haciendo exactamente lo que todos recomiendan hacer.

### 7.2 · Lo que salva un proyecto es la arquitectura, no despedir más gente

Cuando el número no cierra, el reflejo de cualquier gerente es **recortar más gente**. La conclusión anterior ya dijo que eso no funciona: no podés bajar del piso, y automatizar más te empeora las dos cosas. ¿Qué queda?

**Queda bajar λ.** Mirá el mismo proyecto —misma gente, misma automatización, misma inversión— cambiando *solamente* dónde corre la IA y si hay plan B:

| Arquitectura | λ | IDA | Ahorro | Recupero |
|---|---|---|---|---|
| Una sola nube, sin plan de contingencia | 1,50 | 58 | $2.457 | 20 meses ✗ |
| Una sola nube, con plan de contingencia | 1,30 | 50 | $2.703 | 19 meses ✗ |
| **Multi-cloud, con plan de contingencia** | **1,10** | **42** | **$2.948** | **17 meses** ✓ |
| IA local, con plan de contingencia | 1,02 | 39 | $3.047 | 16 meses ✓ |

No cambió **nada** del negocio entre la primera fila y la última. No se automatizó más, no se despidió a nadie extra, no se negoció mejor precio de tokens. Lo único que cambió es **dónde vive la IA y si hay plan B**. Con eso solo, el proyecto pasa de reprobar (20 meses) a aprobar, y el IDA cae de 58 a 39.

> **Leé la última fila con cuidado: es el piso teórico de λ, no una recomendación.** Esta tabla **aísla el efecto del riesgo**: mantiene fija la factura de IA ($1.229/mes) y mueve solo λ. Eso es exactamente lo que pasa cuando sumás un segundo proveedor o escribís el plan de contingencia — el riesgo baja y la factura casi no se mueve. Por eso la fila realista para esta empresa es **multi-cloud con plan**.
>
> Pero **mudarte a IA local no cambia solo λ: te cambia la factura entera**, de $1.229 a $8.420 por mes de costo fijo. Si esta misma empresa de 10 personas hiciera esa mudanza, su ahorro sería **−$4.288/mes** y no recuperaría nunca (§5, extremos C y D). La fila de IA local muestra hasta dónde *puede* bajar λ, no que convenga a este volumen: **local recién conviene cuando tu volumen supera el break-even**. Bajar λ es la palanca correcta; cuál de las tres opciones te sirve depende de tu escala.

> **Cuando el business case de automatización no cierra, la palanca correcta casi nunca es recortar más gente: es bajar el riesgo de la arquitectura.** Es la única decisión que mejora las tres cosas a la vez — sube el ahorro, acorta el recupero y baja la dependencia.

### 7.3 · Cuándo conviene comprar el fierro: hay dos umbrales, no uno

La conclusión anterior dice que bajes λ, y la IA local es la que más lo baja. Pero para una empresa de 10 personas el servidor propio da **−$4.288 por mes**. ¿Entonces IA local nunca sirve? No: **sirve a partir de cierta escala**, y el modelo permite calcular cuál. Lo interesante es que **no hay un umbral, hay dos**, y contestan preguntas distintas.

**Umbral 1 — Viabilidad: ¿el fierro se paga con los sueldos que liberás?** El servidor cuesta **$8.420/mes fijo** (con luz y sysadmin), uses 2 horas o 2.000. La única pregunta es cuántos sueldos liberás contra él:

| Personas que liberás | Ahorro mensual con servidor propio | |
|---|---|---|
| 3 (el ejemplo de 10 personas) | −$4.288 | ✕ pérdida |
| 5 | −$1.088 | ✕ pérdida |
| **6** | **+$512** | ✓ punto de quiebre |
| 10 | +$6.912 | ✓ |
| 20 | +$22.912 | ✓ |

**Por debajo de ~6 personas liberadas, comprar el fierro es pérdida segura**, no importa qué hagas con el resto de las variables: el costo fijo se come todo el ahorro. Por eso automatizar 2 horas de trabajo con servidor propio es un disparate y automatizar el trabajo de 20 personas es un buen negocio. La misma máquina, el mismo precio.

**Umbral 2 — Conveniencia: ¿el fierro le gana a alquilar la API?** Que el servidor deje de dar pérdida no significa que convenga: primero tiene que ganarle a alquilar. Y ese umbral **depende por completo de qué API estarías usando si no comprases**:

```
horas de IA para empatar = costo fijo mensual del fierro ÷ costo por hora de la API
```

| Si tu alternativa fuera… | Costo por hora automatizada | Local conviene a partir de |
|---|---|---|
| **API DeepSeek V4-Flash** (el más barato) | $0,21 | 40.100 h/mes = **251 personas-equivalente** |
| **API Gemini 3.6 Flash** (20× más caro) | $4,50 | 1.871 h/mes = **12 personas-equivalente** |

Mismo servidor, mismo precio, y el umbral se movió **20 veces** — de 251 personas a 12. Lo único que cambió es contra qué lo comparás. Por eso la pregunta "¿me conviene IA local?" está mal formulada si no decís *contra qué* y *a qué escala*.

> **Las tres zonas, para decidir en dos minutos.** Menos de ~6 personas liberadas: el fierro es pérdida segura, alquilá. Entre eso y el break-even de tu API: el servidor propio funciona, pero la API funciona mejor — alquilá igual, salvo que la soberanía del dato pese más que la plata. Arriba del break-even: local gana en costo *y* en λ al mismo tiempo, el único punto del modelo donde no hay que elegir entre ahorro y riesgo.

> **La frase para llevarse:** no preguntes si conviene la IA local. Preguntá **contra qué la comparás y a qué escala**: el mismo servidor es un disparate para tres personas y la mejor decisión posible para trescientas. **El costo fijo no se discute, se supera con volumen** — y el modelo te dice desde qué volumen exacto.

### 7.4 · La cifra con la que se negocia: hasta cuánto podés invertir

Todo el modelo se usa para decidir, y hay una sola cuenta que se puede llevar a una reunión con un proveedor. No es el IDA ni el ahorro: es **el techo de inversión**. La fórmula del recupero es `T = I ÷ S`; despejada al revés, contra el plazo con el que tu organización aprueba inversiones:

```
inversión máxima = S × plazo de recupero
```

El plazo por defecto es **18 meses** —en IA, dos años es una eternidad— pero **es un campo de la calculadora, no una ley del modelo**. Un banco evaluando infraestructura crítica trabaja con 36 meses; una startup quemando caja no aguanta 12. Movelo y se recalculan tres cosas a la vez: el techo de inversión, el semáforo del recupero y el porcentaje de éxito del Montecarlo. Los números que siguen usan 18.

> **Por qué el autor no recomienda aprobar arriba de los 18 meses.** Es una postura, no un teorema, y conviene decir de dónde sale: **no es un criterio financiero, es tecnológico**.
>
> Un recupero a 30 o 36 meses es normal en una inversión industrial: comprás una máquina, sigue siendo la misma máquina tres años después y el ahorro que prometía lo sigue dando. **Con IA eso no pasa.** En dos años cambia el precio del token, cambia el modelo que usabas —a veces lo discontinúan—, aparece uno que hace lo mismo por una fracción, cambian las condiciones de uso, y a veces cambia hasta quién puede usarlo.
>
> Es decir: **estás calculando el recupero de algo que probablemente no exista igual cuando termine de pagarse.** Si tu proyecto necesita 36 meses, en el mes 20 vas a estar sosteniendo una integración vieja con un modelo viejo mientras alguien te muestra que eso hoy se hace por la mitad. El ahorro que justificaba el proyecto se evapora antes de completarse.
>
> Por eso 18: no porque el dinero valga distinto, sino porque es el plazo dentro del cual los supuestos tecnológicos todavía se parecen a los de hoy. Si tu número solo cierra estirando el horizonte, no estás mejorando el proyecto — estás apostando a que nada cambie en un rubro donde todo cambia.

En el ejemplo, con un ahorro de $2.457/mes, el techo es **$44.222** — y la inversión evaluada era $50.000. Ahí está la razón exacta por la que el proyecto no cierra, dicha de la forma más accionable: no *"el payback da 20 meses"*, sino **"este proyecto vale $44.222, no $50.000"**.

> **Por qué la vuelta importa.** Las dos frases dicen lo mismo pero abren conversaciones distintas. *"El recupero da 20 meses"* es un veredicto: aprobás o cancelás. *"Este proyecto vale hasta $44.222"* es una posición de negociación — te sentás con un número propio, calculado con tu ahorro y tu riesgo, en vez de discutir contra el presupuesto que te trajeron. Cambia quién pone el precio de referencia. Y funciona en las dos direcciones: si el presupuesto entra cómodo debajo del techo, tenés margen para pedir más alcance por la misma plata.

> **La trampa de subir el techo.** El techo sube si sube S, y aparece la tentación de automatizar más. Ya sabés cómo termina: pasado el piso, automatizar de más baja el ahorro si pagás la IA por hora, así que el techo *baja*. Con costo fijo el techo no baja, solamente deja de subir. Al 60% el techo llega a $111.960; al 100% se derrumba a $77.400 con un IDA de 100. La forma sana es la misma de siempre: **bajar λ**. Con multi-cloud y plan de contingencia el ahorro sube a $2.948 y el techo pasa a **$53.070** — de golpe los $50.000 entran.

### 7.5 · Cómo se aplica fuera de una oficina: banco y retail

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

#### La trampa al aplicarlo: el factor de cobertura

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

## 8. Qué existe afuera — y qué hueco llena esto (benchmark)

Antes de confiar en una calculadora nueva, la pregunta correcta es: **¿por qué no existía?** Alrededor de la IA hay muchísimo software de retorno, de riesgo y de cumplimiento. Lo honesto es mostrar qué hace cada categoría, qué pregunta no contesta, y dónde queda el hueco que este modelo intenta llenar.

| Qué hay hoy | Qué resuelve bien | La pregunta que no contesta |
|---|---|---|
| **Calculadoras de ROI de IA** | Cuánto ahorrás automatizando: horas por costo, payback simple. | Asumen riesgo cero y continuidad gratis. Te dicen a cuánta gente podés *bajar*; nunca cuánta tenés que *conservar*. |
| **Índices académicos de dependencia de IA** | Miden cuánto depende de la IA una economía o un sector, a nivel macro. | No bajan al gerente: no te dicen cuántas personas necesita tu área el lunes si el proveedor no responde. |
| **Normas de gestión (ISO/IEC 42001, ISO 22301)** | Te exigen plan de contingencia y evaluación de riesgos: definen el *qué*. | Son marcos, no calculadoras: piden el plan pero no dan el número — ni la dotación mínima, ni el costo del riesgo, ni el tope de inversión. |
| **Marcos de riesgo y seguridad de IA** (NIST AI RMF, MITRE ATLAS) | Cubren el riesgo del sistema: inyección de prompts, fuga de datos, sesgo algorítmico, pérdida de propiedad intelectual. | Cuidan a la IA de que la ataquen o se comporte mal. No cuidan a tu operación de quedarse *sin* IA, ni te dicen con cuánta gente seguís funcionando. |
| **Plataformas de IAOps y GRC corporativo** | Operan en producción: monitorean, desvían tráfico entre proveedores y ejecutan el failover en tiempo real sobre datos reales. | Te dicen *cómo* reaccionar cuando falla. No te dicen **si convenía invertir** ni cuánta gente conservar — llegan después de la decisión que este modelo ayuda a tomar. |

La última fila merece una aclaración, porque es donde más se confunde: **este modelo no compite con esas plataformas, va antes.** Ellas ejecutan la mitigación; el modelo te dice cuánto vale la pena gastar en ellas. Un failover automático entre nubes es exactamente lo que baja tu λ — y el modelo es lo que te permite defender ese gasto ante finanzas con un número.

**Se usa de tres maneras distintas:**

| Modo | Cuándo | Qué datos | Qué te llevás |
|---|---|---|---|
| **Diagnóstico** (2 min) | La primera vez, o en una reunión | Números a ojo | Una primera alerta: si tu piso ya supera tu dotación, hay un problema hoy |
| **Decisión** | Antes de aprobar una inversión o un recorte | Datos reales + Montecarlo con tus rangos | Techo de inversión, dotación a conservar, IDA — con CSV para auditar |
| **Auditoría** (trimestral) | Después, como control recurrente | Los mismos, actualizados | Si el IDA se movió sin que nadie lo note |

Cada pieza existe por separado. Lo que no existía es la **unión**: personas + arquitectura técnica + riesgo de negocio en una sola cuenta que se pueda auditar.

**Qué pasa hoy porque esta cuenta no se hace.** Se despide con el Excel del ROI y el piso de continuidad se descubre el día de la primera caída — como en el apagón global de CrowdStrike, cuando el "plan manual" de muchas organizaciones resultó no tener gente suficiente que supiera ejecutarlo.

Y **no hace falta que se caiga nada**: el 12 de junio de 2026 una orden del gobierno de Estados Unidos obligó a Anthropic a prohibir el acceso a dos de sus modelos más avanzados a cualquier ciudadano extranjero, dentro o fuera del país; como no había forma de verificar la nacionalidad en tiempo real, terminó apagándolos para todos los clientes del mundo hasta el 30 de junio. Los servidores nunca dejaron de funcionar — simplemente, durante casi tres semanas, nadie pudo usar el modelo sobre el que había montado su operación. Ese caso es incómodo porque **la redundancia de infraestructura no lo cubre**: podés tener multi-cloud, failover automático y todos los backups del mundo, que si la decisión es regulatoria o geopolítica conmutar de nube no te salva, porque el problema no era la nube. Los otros modelos del proveedor siguieron disponibles, pero **eso no es una contingencia**: si el modelo está fijo en el código, cambiarlo exige que alguien se entere —monitoreo—, que alguien toque el código —un developer— y que ese cambio ya esté ensayado. **Nada de eso pasa solo.** Sin esas tres cosas la caída ocurre igual y dura lo que tarde una persona en arreglarla. Y ahí volvés al mismo lugar: lo que te sostiene mientras tanto son horas de gente, que es lo que este modelo te obliga a contar. El plan de contingencia que exige la norma se escribe sin número: promete "volver a operación manual" con una dotación que ya no alcanza para operar manualmente. El directorio discute cuánto ahorra la IA, nunca cuán rehén queda del proveedor. Y la inversión se aprueba con el escenario promedio: "recuperás en 20 meses" suena a plan, hasta que lo corrés 10.000 veces y solo el 25% de los futuros recupera en menos de 18.

**Qué hace distinto este modelo.** Tres cosas: cuantifica la dotación mínima de continuidad (P') que ningún software de RRHH ni de ROI calcula; traduce la fragilidad de arquitectura a plata (λ), convirtiendo "una sola nube sin plan B" en un costo económico directo; y es preventivo y probabilístico — avisa antes de la caída, con porcentajes calculados sobre las 10.000 corridas completas, incluyendo los escenarios donde el proyecto no cierra.

### El regulador ya lo está midiendo

Esto dejó de ser una preocupación teórica, y conviene decirlo con la fuente en la mano.

En la **encuesta de 2024 del Banco de Inglaterra y la FCA** sobre servicios financieros británicos, un tercio de los casos de uso de IA ya eran implementaciones de terceros, contra el 17% de dos años antes. Y los tres principales proveedores concentraban el **73%, 44% y 33%** de todos los proveedores informados de nube, modelo y datos.

**El dato que más importa es la tendencia, no el nivel:** la concentración de nube *bajó* respecto de 2022, mientras que la de modelo subió **del 18% al 44%**. La concentración se está mudando de la capa de infraestructura a la capa de modelo — que es exactamente la capa que λ todavía no cobra.

En **abril de 2025**, catorce meses antes del episodio de junio, el Comité de Política Financiera ya había planteado el escenario textual: *"una caída generalizada de uno o varios modelos clave podría dejar a muchas firmas sin poder entregar servicios vitales como los pagos con plazos críticos"*. Y en enero de 2026 el comité del Tesoro británico recomendó designar a los grandes proveedores de IA como terceros críticos antes de fin de 2026.

**Ninguno de esos instrumentos dice cuánta gente hay que conservar** para operar a través de ese escenario. Ese es el hueco.

| Fuente | Qué aporta |
|---|---|
| [BoE/FCA, *AI in UK financial services 2024*](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024) | los 73/44/33 y el salto de 18% a 44% en modelo |
| [BoE FPC, *Financial Stability in Focus*, 9/4/2025](https://www.bankofengland.co.uk/financial-stability-in-focus/2025/april-2025) | el escenario de caída de modelos clave |
| House of Commons Treasury Committee, *AI in Financial Services*, HC 684, 20/1/2026 | designar proveedores de IA como terceros críticos |

---

**Lo que este modelo todavía no tiene.** Los coeficientes de λ salen de criterio experto e incidentes públicos, no de un dataset calibrado por sector: son un punto de partida razonable, no una verdad revelada. Y todavía no publica casos reales con métricas de antes y después. Las dos cosas están en la hoja de ruta; mientras tanto, todas las fórmulas están a la vista y podés desafiarlas con tus propios números.

---

## 9. Los límites del modelo

Ningún modelo es honesto si no dice qué *no* hace.

**1 · Supone que la gente que conservás todavía sabe hacerlo.** El piso asume que pueden ejecutar el proceso manual el día que haga falta. Si hace ocho meses que la IA hace todo y ellos solo revisan, no van a poder: son **guardia pasiva**, y la guardia pasiva se oxida. Mantener la capacidad exige **simulacros periódicos de operación manual** —como un simulacro de incendio— y eso cuesta horas que no están en ninguna fórmula. Un P_min de papel no salva a nadie.

> **Se podría modelar y no está.** Una versión futura podría pedirte cada cuánto hacés simulacros y penalizar la eficiencia de tu gente de contingencia con el tiempo, empujando el piso hacia arriba mes a mes sin simulacros. No está por decisión: el modelo ya arrastra coeficientes basados en criterio (ver límite 6) y agregar una tasa de degradación inventada sumaría precisión aparente, no confiabilidad. Prefiero que quede declarado como límite y no escondido dentro de una fórmula.

**2 · Supone que el know-how sigue adentro.** No alcanza con tener gente disponible: tiene que quedar quién sepa **cómo se trabajaba antes**. Si en el camino se fueron los que conocían el proceso viejo, el piso existe en la planilla y no en la realidad. Documentar el proceso manual es parte del seguro.

Y **acá es donde este límite muerde más fuerte: en R, el respaldo externo.** El piso `P_min` al menos habla de gente que está en el área todos los días. R habla de gente que *supuestamente* sabe hacer la tarea pero **hace tiempo que no la hace** —o que quizás nunca la hizo en esta versión del proceso—. El modelo **no tiene forma de verificarlo**: R es una declaración, y es el único número que **baja** el riesgo en lugar de subirlo. Todos los demás castigan; este premia.

> **Cómo auditar un R antes de creerle.** Estas tres preguntas están en la calculadora como casillas, y **no son un consejo: son un candado**. Mientras falte alguna, el campo de R queda bloqueado en 0 y el IDA se calcula sin descuento.
> 1. **¿Lo hicieron alguna vez, con este proceso?** No "algo parecido en otra sucursal hace cinco años". Este proceso, esta versión.
> 2. **¿Está documentado el modo manual?** Si la única forma de aprenderlo era mirando a alguien que ya no está, R es cero por más gente que figure.
> 3. **¿Se probó alguna vez que puedan venir?** Tienen su propio trabajo. Si nadie ensayó el traspaso, no sabés cuántas horas tardan en estar operativos — y las primeras horas de una caída son las que cuentan.
>
> **Si las tres no son un sí claro, el modelo no te deja usar R.** Un respaldo declarado y no probado es el mismo papelito que un plan de contingencia que nadie ensayó: tranquiliza al directorio y no sirve el día que hace falta.

**3 · Mide costo y continuidad, no ingresos.** Para operaciones críticas eso es lo correcto: en una guardia de gas o energía no hay ingreso que justificar, hay una obligación legal de tener gente 24/7 — y el modelo sirve justamente para calcular cuánta. Pero si tu caso es comercial y automatizar genera ventas nuevas (atención 24/7, más capacidad en pico), ese ingreso **no entra acá** y hay que sumarlo por afuera.

**4 · Modela la convivencia permanente, no la degradación temporal.** La convivencia humano-IA **sí está**, y vive en **r**: si de 1.000 horas hay 200 que necesitan la firma de un abogado, un ingeniero o un arquitecto, cargás `r = 20%` y el modelo entiende que esas 200 nunca se automatizan —la IA hace el trabajo, el profesional firma—. Lo que **no** sabe representar es que la IA no se caiga del todo pero funcione peor dos semanas: más lenta, con más errores, con límite de consultas. El modelo es binario, la realidad no.

**5 · El recupero es payback simple, no valor presente.** `T = I ÷ S` divide y listo: **no descuenta el dinero en el tiempo**. No hay tasa, no hay inflación, no hay costo de oportunidad — un dólar del mes 20 vale lo mismo que uno de hoy. Es distinto del VPN o la TIR que va a pedirte un CFO. Es deliberado (el payback simple se entiende sin explicación y sirve para *descartar* proyectos), pero tiene un sesgo: al no descontar, **el recupero se ve mejor de lo que es**. Tratá los 18 meses como filtro grueso, no como aprobación financiera.

**6 · Los coeficientes de riesgo son criterio experto, no un dataset.** Los recargos de λ —+30% nube única, +20% sin plan de contingencia, +15% datos sensibles afuera— **salen de experiencia profesional, no de un estudio estadístico**. Lo que sí tienen es un orden defendible: depender de un solo proveedor es la fragilidad más grave porque es la única sin salida; no tener plan viene después (no te cae el servicio, te deja sin respuesta ensayada); y los datos sensibles afuera pesan menos en continuidad porque no interrumpen la operación, agregan exposición regulatoria. Calibrarlos de verdad exigiría una base de incidentes por sector con frecuencia, duración y costo — el próximo paso natural del modelo. Mientras tanto **el orden de magnitud sirve para comparar dos arquitecturas entre sí**, que es para lo que se usa λ.

> **Dos preguntas incómodas sobre λ, contestadas de antemano.**
>
> *¿Por qué λ no toca el mantenimiento (M)?* Crítica válida: una arquitectura frágil consume más horas de apagar incendios, así que M también debería subir con el riesgo. No lo hace, y el efecto es que **el modelo subestima el costo de una arquitectura mala**. Preferimos ese error al inverso: si el número ya no cierra con λ tocando solo la factura de IA, con M ajustado cerraría todavía menos.
>
> *¿Por qué λ multiplica el gasto en IA y no el daño de la caída?* Porque el gasto es un dato que tenés y el daño no. La consecuencia rara hay que decirla: comparando arquitecturas de costo muy distinto, el recargo en dólares puede quedar al revés — correr local, que es más seguro, tiene una factura mucho mayor, así que su 2% de recargo puede superar en pesos al 50% de una API barata. **Dentro de una misma arquitectura la comparación es válida**, que es como se usa; cruzando arquitecturas hay que mirar el IDA, no el recargo en plata. Anclar el multiplicador al costo por hora de no-operación es la mejora pendiente más importante.

**7 · Convierte horas liberadas en puestos eliminables.** Este es el supuesto más fuerte de todo el modelo. Cuando la cuenta económica hace `⌈P × (1 − a_ef)⌉` está asumiendo que **las horas que la IA te saca de encima se traducen en gente que dejás de necesitar**: en la farmacia, 38,4% sobre 10 personas da 7, y las 3 de diferencia se cuentan como sueldos que dejás de pagar.

En una organización real eso **no es automático**. Con el mismo 38,4% de horas liberadas podés reasignar a esas personas a tareas postergadas, dejar de pagar horas extra en vez de sueldos, absorber el crecimiento del año que viene sin contratar, o directamente no despedir a nadie. En todos esos casos el ahorro existe, sin embargo no tiene la forma que el modelo le da.

> **Cómo leer el resultado, entonces.** `P'` es **capacidad laboral que dejás de necesitar, no una orden de despido**. El modelo te dice cuántas personas de trabajo te sobran; qué hacés con ellas es una decisión de gestión que el modelo no toma ni debería tomar.
>
> Y tiene una consecuencia práctica: **si no vas a reducir dotación, el ahorro que muestra la calculadora no va a aparecer en tu balance.** Va a aparecer como más capacidad con la misma gente, que es igual de valioso pero no se contabiliza igual. Si tu caso es ese, mirá `P'` y el IDA, y tomá `S` como el techo teórico de lo que *podrías* ahorrar si decidieras reducir.
>
> Lo que **no cambia** en ninguno de esos escenarios es el piso de continuidad: aunque no eches a nadie, si automatizaste el 38,4% y mañana la IA no está, seguís necesitando gente que sepa hacerlo a mano.
>
> Y conviene leerlo junto a **7.1**, el óptimo de automatización: ese óptimo existe justamente porque el ahorro se mide en personas liberadas. Si en tu caso las horas no se convierten en puestos, el punto donde la curva deja de mejorar sigue siendo el mismo — lo que cambia es que lo que ganás ahí es capacidad, no plata.

**8 · λ mira la infraestructura, no el modelo que usás.** Los agravantes preguntan **dónde corre** la IA: una nube, varias, tus servidores. Eso cubre que se caiga la infraestructura. Pero en 2026 el riesgo ya no es solo ese: es que **el modelo en sí cambie debajo tuyo**. Un proveedor de frontera puede degradar la calidad entre versiones sin avisar, cambiar políticas de uso o privacidad, subir el precio de golpe, discontinuar el modelo sobre el que armaste todo, o quedar bloqueado por una decisión regulatoria ajena a vos. Nada de eso es una caída de infraestructura —el servicio sigue en línea— y te rompe la operación igual. **El modelo no lo mide.** Y no es hipotético: el 12 de junio de 2026 una orden de Estados Unidos obligó a Anthropic a prohibir el acceso a dos de sus modelos más avanzados a cualquier ciudadano extranjero, dentro o fuera del país; como no podía verificar la nacionalidad en tiempo real, los apagó para todo el mundo hasta el 30 de junio. Para quien tenía la operación montada sobre uno de ellos el efecto fue el de una caída total, con el agravante de que ningún plan de contingencia de **infraestructura** lo cubría: no había a qué nube conmutar, porque el problema no era la nube. Los demás modelos de Anthropic no se vieron afectados, así que **tener ensayada la conmutación a otro modelo** habría servido. Pero no es una salida barata: conmutar de modelo no es automático. Hace falta **monitoreo** que avise, un **developer** que toque el código si el modelo está fijo ahí, y que el cambio esté **ensayado** antes. Si falta cualquiera de las tres, la caída sucede igual y se mide otra vez en horas de gente. Esa capacidad de conmutación es la dimensión que λ no mide. Podría agregarse como un agravante más y probablemente sea el próximo; no está todavía por la misma razón del límite 6, y porque **no hay con qué calibrar su valor**: los datos del Banco de Inglaterra acotan su orden de magnitud, no su tamaño. Mientras tanto tratalo como un riesgo **real y no contemplado**: si dependés de un solo modelo de un solo proveedor de frontera, tu exposición es mayor que la que muestra el IDA.

> **Cómo leer estos límites:** ninguno de los ocho invalida el modelo, y los primeros cuatro empujan en la misma dirección — **hacia arriba**. Un piso que no se entrena, un know-how que se fue y una degradación no contemplada hacen que necesites **más** gente, no menos. Si el modelo te da un número, tratalo como el **mínimo del mínimo**.

---

## 10. Cierre: la conjetura

Los bancos no eligen cuánto capital de reserva tienen: **Basilea** se los exige. Mi conjetura es que vamos hacia lo mismo con la IA: las empresas de servicios críticos van a tener que demostrar una **reserva mínima de capacidad humana** —un P_min auditado y un IDA declarado— igual que hoy declaran capital. En Europa, **DORA** ya obliga al sector financiero a gestionar el riesgo de dependencia de proveedores tecnológicos; extenderlo de "sistemas" a "personas" y de finanzas a toda industria crítica es el paso natural.

Las dos preguntas para llevarte:
1. **¿Cuál es tu piso?** ¿Con cuánta gente operás mañana sin IA?
2. **¿Cuál es tu IDA?** ¿Cuán rehén sos de tu arquitectura?

---

## Calculadora

[**Abrí la calculadora interactiva**](https://modelo-ida.web.app) para cargar los números de tu organización y obtener tu dotación mínima, tu IDA y tu payback en tiempo real. Todo corre en tu navegador: no se envía ningún dato.

Qué trae:

- **Costo de la IA por mes** como dato de entrada, que es el número que realmente conocés (tu factura), con un asistente que lo arma componente por componente si usás API o servidor propio.
- **Diagrama de flujo interactivo** en la pestaña *Fórmulas*: hacés clic en un módulo y ves hacia dónde va, o clic en una respuesta y ves todo lo que la construye.
- **Asistente de horas mínimas** que traduce "necesito 2 puestos cubiertos" a la cantidad real de personas según el horario de tu operación.
- **Simulación de Montecarlo** con 10.000 escenarios, que toma los datos firmes de la calculadora y te deja definir el rango solo de lo incierto.
- **Comparador local vs nube** e **informe descargable en PDF** con resumen ejecutivo, análisis de ROI, Montecarlo y gráficos.
- **Export a CSV** con todos los supuestos, los resultados y la corrida de Montecarlo, para auditar en planilla. Usa `;` y coma decimal: Excel en español lo abre sin asistente de importación.

## Verificación

Una calculadora que no se puede comprobar no sirve para decidir. El repo trae una **batería de 24 casos de borde** que corre contra el sitio real y compara el motor contra las fórmulas publicadas: piso mayor que la plantilla, una persona, mil personas, división por cero en la cobertura, hora de IA más cara que la humana, los extremos de λ y del plazo de recupero, y las dos estructuras de costo de la IA.

Se corre pegando [`pruebas/casos-borde.js`](pruebas/casos-borde.js) en la consola del navegador. Detalle completo en [**PRUEBAS.md**](PRUEBAS.md).

Lo que verifica es que **el código haga lo que dicen las fórmulas**. Lo que no puede verificar —y conviene decirlo— es si las fórmulas describen bien la realidad: eso depende de los coeficientes, que son criterio experto declarado en la sección de límites.

### Robustez de los coeficientes

Los coeficientes ρ no están calibrados, y eso es la objeción principal al modelo. No se puede responder acá con datos, pero sí **acotar**: [`analisis/robustez_ordinal.py`](analisis/robustez_ordinal.py) perturba cada ρ un ±50% —en los 243 vértices extremos y sobre 20.000 sorteos— y mide qué conclusiones se caen y cuáles no.

| Propiedad | Resultado |
|---|---|
| Ubicación del óptimo `a* = 1 − P_min/P` | **invariante** — no contiene ningún ρ |
| Existencia del óptimo | vale hasta `λ < C_h/c = 5`, o sea 3× el máximo alcanzable |
| Orden de las arquitecturas | **100,0%** de los sorteos, pero ±50% es el umbral exacto donde la inversión se vuelve posible |
| Orden completo de las 12 configuraciones | idéntico en solo el **2,9%** — y se informa igual |

**La conclusión honesta es partida:** lo estructural —dónde está el óptimo, qué arquitectura conviene— es robusto; el veredicto sobre un proyecto concreto **no lo es**, y por eso el techo de inversión debería leerse como banda y no como punto. Resultados completos en [`analisis/RESULTADOS.md`](analisis/RESULTADOS.md).

### El Montecarlo tiene semilla

Desde el 01/09/2026 el generador usa **semilla fija (`MC_SEMILLA = 7`)**. Antes era `Math.random()`: el número cambiaba entre corridas y un resultado publicado no se podía verificar, solo volver a correr. El valor real es **25,4%** y caía justo en el borde del redondeo —corridas distintas devolvían 25 o 26—. Ahora cualquiera que abra el sitio con los mismos rangos obtiene **exactamente 25%**.

## El paper

El modelo está descrito en un preprint abierto, con las fórmulas, el caso de referencia y las limitaciones declaradas:

> **The AI Dependency Index (IDA): Quantifying Minimum Workforce Continuity in AI-Dependent Organizations**
> César Riat (2026) · SSRN · [ssrn.com/abstract=7341479](https://ssrn.com/abstract=7341479) · DOI [10.2139/ssrn.7341479](https://doi.org/10.2139/ssrn.7341479) · licencia CC BY 4.0

**Hay una segunda versión, todavía no depositada en SSRN.** La v2 agrega:

- el **óptimo como proposición** con demostración: `a* = 1 − P_min/P`, una expresión que no contiene ningún coeficiente de riesgo
- el techo de inversión **como banda con su umbral** (`λ < 1,24`) en lugar de como veredicto
- el análisis de robustez de arriba, con su resultado negativo incluido
- el Montecarlo **especificado por completo y con semilla**
- **siete límites** en lugar de cuatro — entre ellos que el episodio de junio fue **de un modelo y no de un proveedor**, algo que la Tabla 2 todavía no cobra
- la distinción entre **incertidumbre de parámetro e incertidumbre de forma funcional**: perturbar los ρ no demuestra que la composición multiplicativa sea la correcta
- el **margen de continuidad** `CM = (P′ − P_min)/P′` como la dimensión que falta, propuesta pero **no implementada** — el índice publicado no cambia
- de 8 a **15 referencias**, con la evidencia de concentración del Banco de Inglaterra

Los PDF de las cuatro ediciones están en [`paper/`](paper/), depositados junto al código para que el archivo de Zenodo los cubra:

| Archivo | Edición |
|---|---|
| `IDA-preprint-v1.pdf` | inglés, **la depositada en SSRN** |
| `IDA-preprint-v1-es.pdf` | castellano |
| `IDA-preprint-v2.pdf` | inglés, revisada — pendiente de subir |
| `IDA-preprint-v2-es.pdf` | castellano, revisada |

## Cómo citar

**Hay dos cosas distintas que se pueden citar, y no son intercambiables.** Si citás el trabajo y su argumento, va el paper. Si citás la herramienta, las fórmulas o la batería de pruebas —por ejemplo porque reprodujiste un resultado—, va el depósito de Zenodo.

```
Riat, C. (2026). The AI Dependency Index (IDA): Quantifying Minimum Workforce
Continuity in AI-Dependent Organizations. SSRN. https://doi.org/10.2139/ssrn.7341479
```

```bibtex
@article{riat_ida_paper_2026,
  author = {Riat, César},
  title  = {The AI Dependency Index (IDA): Quantifying Minimum Workforce Continuity in AI-Dependent Organizations},
  year   = {2026},
  doi    = {10.2139/ssrn.7341479},
  note   = {SSRN preprint}
}
```

### Citar el modelo y el código

Cada versión publicada queda depositada en Zenodo con su propio DOI, así que el modelo se puede citar por un identificador permanente y no por un enlace que mañana puede cambiar.

```
Riat, C. (2026). Modelo IDA — Índice de Dependencia de IA (v1.0.0).
All AIdeas SAS. https://doi.org/10.5281/zenodo.22070415
```

```bibtex
@software{riat_modelo_ida_2026,
  author    = {Riat, César},
  title     = {Modelo IDA — Índice de Dependencia de IA},
  version   = {1.0.0},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22070415},
  url       = {https://modelo-ida.web.app}
}
```

> **Hay dos DOI y conviene saber cuál usar.** El de arriba, `10.5281/zenodo.22070415`, es el **DOI de concepto**: siempre resuelve a la última versión publicada, y es el que hay que citar cuando se cita *el modelo*. Cada versión tiene además el suyo propio —esta es `10.5281/zenodo.22070416`— y ese se usa cuando hace falta reproducir exactamente esta versión y ninguna otra.
>
> El archivo `CITATION.cff` de este repositorio tiene los mismos datos en formato legible por máquina: GitHub lo usa para mostrar el botón **Cite this repository**.

**Qué se está citando.** El depósito incluye el modelo completo, las fórmulas publicadas, la batería de 24 casos de borde y el código que las corre. Todo se ejecuta en el navegador, en JavaScript, sin servidor: cualquiera puede reproducir los resultados abriendo el archivo, sin instalar nada ni pedir credenciales.

## Licencia
MIT — usalo, adaptalo, citá la fuente. Si lo aplicás en un caso real, me encantaría saberlo.

## Autor
**César Riat** — Consultor en IA · [cesarriat.com](https://cesarriat.com) · [All AIdeas](https://allaideas.com)
