# Pruebas del modelo

Este archivo existe por una razón concreta: **una calculadora que no se puede verificar no sirve para decidir nada.** Si el modelo va a usarse para justificar una inversión o una dotación, quien lo lea tiene que poder comprobar que hace lo que dice — sin creerle al autor.

Acá está cómo hacerlo.

---

## Qué se verifica, y qué no

Hay dos preguntas distintas y conviene no mezclarlas:

| Pregunta | Qué la responde |
|---|---|
| **¿El código hace lo que dicen las fórmulas?** | Estas pruebas. Es verificable y está verificado. |
| **¿Las fórmulas describen bien la realidad?** | Ninguna prueba puede responder esto. Depende de los coeficientes, y esos son **criterio experto declarado** — ver la sección *Los límites del modelo* en el sitio, puntos 6 al 8. |

Estas pruebas responden **la primera**. La segunda se responde con casos reales, y está pendiente.

---

## Cómo correrlas

1. Abrí la [calculadora](https://modelo-ida.web.app).
2. Abrí la consola del navegador (`F12` → *Console*).
3. Pegá el contenido de [`pruebas/casos-borde.js`](pruebas/casos-borde.js) y dale Enter.

Devuelve:

```
{ casos: 21, fallas: "ninguna" }
```

y una tabla con el resultado de cada caso. Si alguna fila no coincide con las fórmulas publicadas, aparece en `fallas` con el valor del motor y el de la fórmula, para que se vea cuál es cuál.

**Corre contra el sitio real, no contra una copia.** El motor vive dentro de `index.html`; reimplementarlo aparte para probarlo sería probar la copia y no el original.

---

## De dónde salen los valores esperados

La función `esperado()` del archivo de pruebas **no copia el código del motor**. Aplica las fórmulas tal como están publicadas en la pestaña *Fórmulas* y en este README:

```
a_ef  = a × (1 − r) × η
P_min = ⌈H_min ÷ h_p⌉
P'    = máx( ⌈P × (1 − a_ef)⌉ , P_min )
S     = (P − P') × (N ÷ P) − C_mes × λ − M
T     = I ÷ S
IDA   = mín( a_ef × λ × (1 − cobertura × 0,7) × 100 , 100 )
```

Si el motor y las fórmulas se separan, la prueba falla. Ese es el punto.

---

## Los 21 casos

No son variaciones cosméticas: son los bordes donde los modelos se rompen.

| # | Caso | Qué pone a prueba |
|---|---|---|
| 00 | Valores por defecto | Que el caso documentado siga dando lo publicado |
| 01 | Sin automatización (`a = 0`) | Que sin IA no haya ahorro y el IDA sea 0 |
| 02 | Todo requiere firma humana (`r = 100%`) | Que `r` pueda anular por completo la automatización |
| 03 | Automatización total sin piso | El techo del IDA y el caso de dotación cero |
| 04 | Piso igual a la plantilla | Que el piso bloquee toda liberación |
| 05 | **Piso mayor que la plantilla** | Dotación insuficiente: el modelo tiene que decirlo, no romperse |
| 06 | Una sola persona | La división por `P` con el mínimo posible |
| 07 | Mil personas | Que no haya desbordes ni redondeos raros a escala |
| 08 | Hora de IA más cara que la humana | Ahorro negativo por costo, no por piso |
| 09 | Respaldo externo cubre el piso | Cobertura = 100% y el tope del descuento |
| 10 | Respaldo externo desbordado (`R = 999`) | Que la cobertura no pase de 1 |
| 11 | Respaldo con piso cero | **División por cero**: sin piso no hay nada que cubrir |
| 11b | Respaldo declarado pero sin avalar | Que el candado de las tres condiciones lo fuerce a 0 |
| 12 | Sin inversión inicial | `T = 0` sin romper |
| 13 | Sin costo de IA ni mantenimiento | El ahorro bruto puro |
| 14 | Arquitectura más robusta (`λ = 1,02`) | Extremo inferior de λ |
| 15 | Arquitectura más frágil (`λ = 1,65`) | Extremo superior alcanzable |
| 16 | Eficiencia mínima (`η = 50%`) | Extremo inferior del slider |
| 17 | Plazo de recupero mínimo (1 mes) | El techo de inversión con el horizonte más corto |
| 18 | Plazo de recupero largo (120 meses) | Y con el más largo |
| 19 | Jornada doble (320 h) | Que el piso baje al subir las horas por persona |

---

## Qué encontró esta batería

Se escribió para buscar errores, y encontró uno.

**Caso 05 — piso mayor que la plantilla.** Con `H_min` por encima de lo que la dotación puede cubrir, `P − P'` da negativo y el sitio mostraba **"−10 personas liberadas"**, que no significa nada. El número no estaba mal: significa que **faltan 10 personas para poder operar sin IA**. Ahora lo dice así.

El resto de los casos coincide con las fórmulas.

---

## Lo que estas pruebas no prueban

Vale decirlo con la misma claridad:

- **No validan los coeficientes.** Que `λ` sume +30% por nube única es criterio del autor, no un dato medido. Está declarado en los límites del modelo.
- **No validan el 0,7** del descuento por respaldo externo, por lo mismo.
- **No validan los supuestos de negocio** — sobre todo el más fuerte, que las horas liberadas se conviertan en puestos eliminables. Ese está declarado en el límite 7.

Lo que sí prueban es que **el código no le agrega errores propios a un modelo cuyos supuestos están a la vista.** Que es todo lo que un test puede hacer.
