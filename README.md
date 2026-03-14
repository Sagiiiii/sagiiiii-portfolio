# 🦊 Sagiii.dev — Portfolio Personal

> Portfolio personal desarrollado con Python y Flask, tema oscuro con paleta de colores fox/naranja.

🌐 **Demo en vivo:** [sagiiiii-portfolio.onrender.com](https://sagiiiii-portfolio.onrender.com)

---

## 🚀 Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend | Python + Flask |
| Templates | Jinja2 |
| Frontend | Bootstrap 5 Dark + CSS personalizado |
| Email | Flask-Mail + Gmail SMTP |
| Imágenes | Archivos estáticos locales |
| Deploy | Render.com (gratuito) |

---

## 📄 Páginas

- **/** — Inicio: Hero, badges de tecnologías y proyectos destacados
- **/projects** — Galería con filtros por categoría
- **/project/<id>** — Detalle de cada proyecto
- **/about** — CV completo, experiencia y formación académica
- **/contact** — Formulario con envío directo a Gmail

---

## ⚙️ Instalación y ejecución local

### 1. Clonar el repositorio
```bash
git clone https://github.com/Sagiiiii/sagiiiii-portfolio.git
cd sagiiiii-portfolio
```

### 2. Crear y activar el entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows CMD
venv\Scripts\activate.bat

# Activar en Windows PowerShell
venv\Scripts\Activate.ps1

# Activar en Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto con este contenido:
```
SECRET_KEY=tu-clave-secreta-aqui
CONTACT_EMAIL=tu-email@gmail.com
GMAIL_PASSWORD=tu-app-password-de-gmail
```

> ⚠️ Para obtener el `GMAIL_PASSWORD` necesitas una **App Password** de Google:
> 1. Ve a [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
> 2. Crea una contraseña para "portfolio"
> 3. Copia los 16 caracteres generados

### 5. Ejecutar el servidor
```bash
python run.py
```

### 6. Abrir en el navegador
```
http://127.0.0.1:5000
```

---

## 🌐 Deploy en Render.com

### 1. Prerequisitos
- Código subido a GitHub
- Cuenta gratuita en [render.com](https://render.com)

### 2. Crear el servicio
1. En Render click en **New +** → **Web Service**
2. Conecta tu repositorio de GitHub
3. Configura el servicio:

| Campo | Valor |
|-------|-------|
| Name | `sagiii-portfolio` |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn run:app --bind 0.0.0.0:$PORT` |
| Instance Type | `Free` |

### 3. Variables de entorno
En Render → **Environment** agrega:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | tu clave secreta |
| `CONTACT_EMAIL` | tu-email@gmail.com |
| `GMAIL_PASSWORD` | tu app password de Gmail |

### 4. Deploy
Click en **Create Web Service** — Render construye y despliega automáticamente.

Cada vez que hagas `git push` a `main`, Render redespliega automáticamente.

> ⚠️ **Nota sobre el plan gratuito:** El servicio se "duerme" tras 15 minutos de inactividad. La primera visita después puede tardar hasta 50 segundos en cargar.

---

## 📁 Estructura del proyecto
```
sagiiiii-portfolio/
├── app/
│   ├── data/
│   │   └── projects.py       # Lista de proyectos
│   ├── portfolio/
│   │   ├── __init__.py
│   │   └── routes.py         # Rutas principales
│   ├── static/
│   │   ├── css/
│   │   │   └── base.css      # Tema oscuro fox
│   │   ├── js/
│   │   │   └── preloader.js  # Animación de carga
│   │   └── img/              # Imágenes del portfolio
│   ├── templates/
│   │   ├── base.html         # Template base
│   │   └── portfolio/        # Templates de páginas
│   └── __init__.py           # Factory de Flask
├── .env                      # Variables locales (no subir)
├── .gitignore
├── Procfile                  # Comando de inicio para Render
├── requirements.txt
└── run.py                    # Punto de entrada
```

---

## 📦 Agregar un nuevo proyecto

Abre `app/data/projects.py` y agrega un bloque al final de la lista `PROJECTS`:
```python
{
    "id": 6,
    "title": "Nombre del proyecto",
    "short_desc": "Descripción corta para la card.",
    "description": "Descripción completa del proyecto.",
    "technologies": ["Python", "Flask"],
    "github_urls": [
        {"label": "Repositorio", "url": "https://github.com/Sagiiiii/repo"},
    ],
    "live_url": "",
    "image_url": "/static/img/nombre_imagen.png",
    "category": ["web"],
    "featured": False,
},
```

Luego:
```bash
git add app/data/projects.py
git commit -m "✨ Agrega proyecto: Nombre del proyecto"
git push
```

Render redespliega automáticamente en 2-3 minutos.

---

## 👤 Autor

**David A. Garcia Giron**  
BSc. Data Science · Téc. Diseño de Software · CAPM  
📍 Huancayo, Perú 🇵🇪  
📧 sagitaforever64@gmail.com  
🐙 [github.com/Sagiiiii](https://github.com/Sagiiiii)  
💼 [LinkedIn](https://www.linkedin.com/in/david-garcia-giron)

---

*Hecho con ♥ y Python · 2026*