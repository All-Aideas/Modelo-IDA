# Desplegar en Firebase

Objetivo: publicar el Modelo IDA en **`cesarriat.com/modelo-ida`**, dentro del sitio de Hosting que ya tenés, **sin tocar tu web actual**.

---

## Por qué esta opción y no un sitio separado

En Firebase, tener **varios sitios de Hosting en un mismo proyecto requiere plan Blaze**. En el plan gratuito hay un solo sitio por proyecto — por eso la consola no deja crear otro.

Y ojo con dos atajos que **no** sirven:

- **"Agregar app"** registra una app cliente y te devuelve el código de `initializeApp()` con las claves del SDK. Sirve para usar Analytics, Auth o Firestore desde JavaScript. **No crea sitios ni URLs.**
- **Un segundo sitio de Hosting** (si algún día pasás a Blaze) te daría un *dominio* distinto (`modelo-ida.web.app`), nunca una *ruta* de `cesarriat.com`. Las rutas pertenecen a un solo sitio.

Con la carpeta se consigue exactamente la URL que querías, en el plan gratis y sin configuración nueva.

---

## Los pasos

### 1. Copiar la carpeta

En tu repo `cesarriat-web`, dentro de `public/`:

```
cesarriat-web/
└── public/
    ├── index.html          ← tu web, no se toca
    ├── ...                 ← el resto de tu sitio, no se toca
    └── modelo-ida/         ← NUEVO
        ├── index.html
        └── assets/
```

Del repo del Modelo IDA copiá solo **`index.html` y `assets/`**. Los `.md` y el `LICENSE` no hacen falta para el sitio.

### 2. Desplegar

```bash
cd /ruta/a/cesarriat-web
firebase deploy --only hosting
```

No hay que tocar `firebase.json` ni `.firebaserc`. Tus headers de caché ya son correctos: un año para JS y CSS, sin caché para HTML.

---

## ⚠️ El único riesgo real

`firebase deploy` **reemplaza todo el contenido del sitio con lo que haya en tu carpeta local**. No hace un merge con lo que está publicado.

Es decir: **no pisa `cesarriat.com` por agregar una subcarpeta**, pero sí lo pisaría si desplegaras desde un `public/` incompleto. Mientras despliegues desde tu repo completo, no hay problema.

Antes de desplegar, confirmá que están las dos cosas:

```bash
ls public/index.html public/modelo-ida/index.html
```

Si alguna falta, no despliegues.

---

## Un detalle que ya está resuelto

Tu `firebase.json` tiene `trailingSlash: false`, así que la página se sirve en `cesarriat.com/modelo-ida` **sin barra final**. Con esa URL, el navegador resuelve las rutas relativas contra la raíz del dominio: un `assets/foo.gif` se buscaría en `cesarriat.com/assets/foo.gif` y no cargaría.

Por eso la única imagen que quedaba con ruta relativa ahora usa ruta absoluta (`/modelo-ida/assets/...`). Los otros dos gráficos se generan como SVG dentro del HTML, así que no dependen de rutas.

**Consecuencia:** para verlo en tu máquina ya no alcanza con abrir el archivo con doble clic; necesitás un servidor local:

```bash
cd public && python -m http.server 8080
# después: http://localhost:8080/modelo-ida/
```

---

## Si algún día pasás a Blaze

Con plan Blaze podés darle dominio propio:

1. Hosting → **Agregar otro sitio** → ID `modelo-ida` → te da `modelo-ida.web.app`
2. `firebase target:apply hosting modelo-ida modelo-ida`
3. En `firebase.json`, `hosting` pasa de objeto a array con un bloque por sitio (agregándole `"target": "web"` al que ya tenés)
4. `firebase deploy --only hosting:modelo-ida`

Al quedar el sitio en la raíz de su dominio, las rutas relativas volverían a funcionar y podrías revertir la ruta absoluta del GIF. Son 3 líneas en `index.html`, las marcadas con el comentario `EDITAR`.

---

## Antes de publicar

Desde la raíz del proyecto del artículo:

```bash
node .claude/skills/verificar-modelo/verificar.js
```

Y cuando publiques en Medium, reemplazá el `#` del botón "Leer el artículo" en `index.html` por la URL real.
