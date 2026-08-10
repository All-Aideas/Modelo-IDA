# Desplegar en Firebase

El Modelo IDA vive en su **propio proyecto de Firebase** (`modelo-ida`), separado de `cesarriat-web`. URL final:

- **https://modelo-ida.web.app**
- https://modelo-ida.firebaseapp.com (la misma, alias)

`cesarriat.com` no se toca en ningún momento: son proyectos distintos.

---

## Los comandos

Desde esta carpeta (`modelo-ida/`), en CMD o PowerShell:

```bash
npm install -g firebase-tools
```

Solo la primera vez, para instalar la herramienta.

```bash
firebase login
```

Abre el navegador para que entres con tu cuenta de Google. También una sola vez.

```bash
firebase deploy --only hosting
```

Y listo. Al terminar te imprime la URL.

---

## Por qué NO hay que correr `firebase init`

Ya están en el repo los dos archivos que ese comando genera:

- **`firebase.json`** — qué publicar y con qué caché
- **`.firebaserc`** — a qué proyecto (`modelo-ida`)

Correr `firebase init hosting` te preguntaría cosas y, en el paso "¿sobrescribo `index.html`?", un Enter de más te reemplaza el sitio por la página de bienvenida de Firebase. Con la config ya puesta, ese riesgo no existe.

Si aun así lo corrés por curiosidad: cuando pregunte por `index.html`, respondé **No**.

## Qué se publica y qué no

`firebase.json` usa `"public": "."` (esta misma carpeta) e ignora lo que no va al sitio:

| Se publica | Se ignora |
|---|---|
| `index.html` | `*.md` (README, esta guía) |
| `assets/` | `LICENSE` |
| | `.git/`, `.gitignore`, `firebase.json` |

## Verificar antes de publicar

Desde la raíz del proyecto del artículo:

```bash
node .claude/skills/verificar-modelo/verificar.js
```

Y para ver el sitio en tu máquina tal como va a quedar publicado:

```bash
firebase serve --only hosting
```

Levanta en `http://localhost:5000`. Es más fiel que abrir el archivo con doble clic, porque respeta las rutas y los headers reales.

---

## Dominio propio (opcional)

Si algún día querés `modelo-ida.cesarriat.com`:

Firebase Console → proyecto `modelo-ida` → Hosting → **Agregar dominio personalizado**. Te da un registro DNS para cargar donde tengas el dominio. La URL `.web.app` sigue funcionando en paralelo.

Si lo hacés, actualizá el dominio en las 3 líneas de `index.html` marcadas con el comentario `EDITAR` — son las etiquetas que arman la vista previa al compartir el enlace por WhatsApp o LinkedIn.

---

## Cada vez que actualices el sitio

```bash
firebase deploy --only hosting
```

Reemplaza el contenido publicado por lo que tengas en la carpeta. Como este proyecto solo aloja el Modelo IDA, no hay riesgo de pisar nada más.
