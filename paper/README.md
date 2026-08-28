# El preprint

Las dos ediciones del trabajo que describe el modelo. Están acá para que el
depósito de Zenodo las archive junto con el código: así el DOI cubre también el
paper, y queda una copia permanente que no depende de que ningún repositorio
externo siga existiendo.

| Archivo | Edición |
|---|---|
| `IDA-preprint-v1.pdf` | inglés — **es la versión de referencia** |
| `IDA-preprint-v1-es.pdf` | castellano |

## Dónde vive públicamente

**The AI Dependency Index (IDA): Quantifying Minimum Workforce Continuity in AI-Dependent Organizations**
César Riat (2026) · SSRN · <https://ssrn.com/abstract=7341479>
DOI [10.2139/ssrn.7341479](https://doi.org/10.2139/ssrn.7341479) · licencia **CC BY 4.0**

## Qué se cita, y con cuál de los dos identificadores

Son dos cosas distintas y no son intercambiables:

- **El trabajo y su argumento** → DOI de SSRN, `10.2139/ssrn.7341479`
- **El modelo, las fórmulas y la batería de 24 casos** → DOI de concepto de
  Zenodo, `10.5281/zenodo.22070415`, que siempre resuelve a la última versión

Si alguien reprodujo un resultado corriendo la calculadora, lo que corresponde
citar es el segundo.

## Nota sobre las versiones

Las dos ediciones dicen lo mismo: el caso de referencia devuelve `P'=7`,
`S=$2.457`, `IDA=58` y 20 meses de recupero en ambas. Si alguna vez divergen,
**manda la inglesa**, que es la que está depositada en SSRN.

El PDF se verifica antes de publicarse con la skill `verificar-pdf` del
proyecto: lee el archivo generado —no el código que lo genera— y comprueba que
diga lo que tiene que decir y que no sobreviva ninguna frase ya corregida.
