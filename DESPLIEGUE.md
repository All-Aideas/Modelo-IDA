# Desplegar en Firebase con URL propia

Objetivo: que el Modelo IDA viva en **`modelo-ida.web.app`**, separado de `cesarriat.com`, dentro del mismo proyecto de Firebase (`cesarriat-web`). Sin tocar el sitio que ya tenés funcionando.

> **Nota:** en la consola es **Hosting → "Agregar otro sitio"**. *No* es "Agregar app": eso registra una app cliente para darte claves del SDK y no crea URLs.

---

## 1. Crear el sitio en la consola

Firebase Console → proyecto `cesarriat-web` → **Hosting** → **Agregar otro sitio**.

ID del sitio: `modelo-ida`

Ese ID es **único a nivel global de Firebase**, así que puede estar tomado. Si te lo rechaza, usá una variante (`modelo-ida-riat`, `cesarriat-modelo-ida`) y **acordate del ID que quedó**: hay que usarlo en el paso 2 y cambiarlo en 3 líneas del `index.html` (las que dicen `modelo-ida.web.app`).

Al crearlo te quedan dos URLs equivalentes:

- `https://modelo-ida.web.app`
- `https://modelo-ida.firebaseapp.com`

## 2. Enlazar el sitio a un *target* local

Desde la raíz del repo `cesarriat-web`:

```bash
firebase target:apply hosting modelo-ida modelo-ida
```

El primer `modelo-ida` es el nombre del target (local, lo elegís vos); el segundo es el **ID del sitio** que creaste. Esto escribe solo el `.firebaserc`.

## 3. Copiar los archivos

Copiá el contenido de este repo a una carpeta `modelo-ida/` en la raíz de `cesarriat-web` (al lado de `public/`, **no adentro**):

```
cesarriat-web/
├── public/          ← tu sitio actual, no se toca
├── modelo-ida/      ← index.html + assets/
├── firebase.json
└── .firebaserc
```

## 4. Declarar los dos sitios en `firebase.json`

El `hosting` pasa de ser un objeto a un **array**, con un bloque por sitio. Tu configuración actual queda igual, solo se le agrega `"target": "web"`:

```json
{
  "hosting": [
    {
      "target": "web",
      "public": "public",
      "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
      "cleanUrls": false,
      "trailingSlash": false,
      "headers": [
        { "source": "**/*.@(js|css)", "headers": [{ "key": "Cache-Control", "value": "max-age=31536000" }] },
        { "source": "**/*.html", "headers": [{ "key": "Cache-Control", "value": "no-cache" }] }
      ]
    },
    {
      "target": "modelo-ida",
      "public": "modelo-ida",
      "ignore": ["firebase.json", "**/.*", "**/node_modules/**", "**/*.md", "LICENSE"],
      "headers": [
        { "source": "**/*.@(png|gif|svg)", "headers": [{ "key": "Cache-Control", "value": "max-age=2592000" }] },
        { "source": "**/*.html", "headers": [{ "key": "Cache-Control", "value": "no-cache" }] }
      ]
    }
  ]
}
```

También hay que agregarle `"target": "web"` al bloque que ya tenías, si no Firebase no sabe a cuál de los dos sitios mandarlo.

## 5. Desplegar

```bash
firebase deploy --only hosting:modelo-ida
```

Solo publica el sitio nuevo. Tu `cesarriat.com` no se toca. Para publicar los dos: `firebase deploy --only hosting`.

---

## Por qué esta opción es más simple de lo que parece

Al quedar el sitio **en la raíz de su propio dominio**, todas las rutas relativas funcionan sin tocar nada. Con la alternativa de carpeta (`cesarriat.com/modelo-ida`) había que reescribir rutas, porque tu `trailingSlash: false` hace que el navegador resuelva `assets/...` contra la raíz del dominio.

## Si después querés un subdominio propio

En Hosting → el sitio `modelo-ida` → **Agregar dominio personalizado** → `modelo-ida.cesarriat.com`. Firebase te da un registro DNS para cargar donde tengas el dominio. Las URLs `.web.app` siguen funcionando en paralelo.

## Antes de publicar

Corré la verificación desde la raíz del proyecto del artículo:

```bash
node .claude/skills/verificar-modelo/verificar.js
```

Y si el ID del sitio te quedó distinto de `modelo-ida`, cambiá el dominio en las 3 líneas de `index.html` marcadas con el comentario `EDITAR` (son las etiquetas `og:url`, `og:image` y `twitter:image`, las que hacen la vista previa al compartir el enlace).
