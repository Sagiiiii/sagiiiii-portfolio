PROJECTS = [
    # proyecto 1
    {
        "id": 1,
        "title": "E-commerce Soreus Motors — Frontend & Admin",
        "short_desc": "Interfaz de tienda online y panel administrativo para gestión de productos, pedidos y clientes de una distribuidora automotriz.",
        "description": "Desarrollo del frontend y módulo administrativo del sistema e-commerce de Soreus Motors E.I.R.L. La tienda presenta un catálogo visual de productos con filtros por categoría, carrito de compras interactivo y flujo de checkout. El panel admin permite gestionar el inventario, revisar pedidos entrantes, actualizar estados de entrega y administrar la base de clientes mediante un módulo CRM integrado. Diseño responsive con Bootstrap orientado a una experiencia de usuario fluida tanto en desktop como en móvil.",
        "technologies": ["HTML", "CSS", "Bootstrap", "JavaScript", "NodeJS", "MEAN Stack"],
        "github_urls": [
            {"label": "Tienda",  "url": "https://github.com/Sagiiiii/ecommerce_tienda"},
            {"label": "Admin",   "url": "https://github.com/Sagiiiii/ecommerce_admin"},
        ],
        "live_url": "https://ecommercesoreustienda.netlify.app",
        "image_url": "/static/img/soreus.jpeg",
        "category": ["frontend", "web", "mobile"],
        "featured": True,
    },
    # proyecto 2
    {
        "id": 2,
        "title": "E-commerce Soreus Motors — Backend & API",
        "short_desc": "Motor del servidor, API REST y base de datos del sistema e-commerce para distribuidora automotriz, construido con Python y Flask.",
        "description": "Desarrollo del backend completo del sistema e-commerce de Soreus Motors E.I.R.L. Incluye una API REST construida con Flask que expone endpoints para productos, pedidos, usuarios y reportes. La capa de datos usa MySQL con modelos relacionales optimizados para consultas de inventario y trazabilidad de pedidos. Implementa autenticación con sesiones seguras, validación de datos en servidor, control de stock en tiempo real y generación de reportes exportables. Arquitectura modular con Blueprints para facilitar el mantenimiento y escalabilidad del sistema.",
        "technologies": ["MEAN Stack", "MongoDB", "SQLAlchemy", "REST API", "NodeJS"],
        "github_urls": [
            {"label": "Backend", "url": "https://github.com/Sagiiiii/eccommerce_back"},
        ],
        "live_url": "https://ecommercesoreusadmin.netlify.app",
        "image_url": "/static/img/soreus_back.jpg",
        "category": ["backend", "web"],
        "featured": False,
    },
    # proyecto 3
    {
        "id": 3,
        "title": "Análisis Predictivo — Soreus Motors Capstone",
        "short_desc": "Modelo de ciencia de datos con ARIMA, Regresión Lineal y Random Forest para optimizar inventario y predecir ventas en una distribuidora automotriz.",
        "description": """Proyecto Capstone de Data Science desarrollado para SOREUS MOTORS E.I.R.L., 
        empresa del sector automotriz en Huancayo, Perú. El objetivo fue transformar los datos 
        generados por su sistema e-commerce MEAN (2024) en conocimiento estratégico para optimizar 
        decisiones comerciales.

        Se aplicó la metodología CRISP-DM con tres modelos predictivos:
        • ARIMA (2,1,1): Series temporales para pronóstico de sobrestock mensual. Proyectó ~6,500 
        unidades de sobrestock promedio para 2025, con pico en marzo.
        • Regresión Lineal Múltiple (RLM): R² = 0.75, identificó el inventario como variable 
        principal. Reducción proyectada del 40% en costos de sobrestock (de S/ 15.3M a S/ 9.1M).
        • Random Forest (RF): Mejor modelo con R² = 0.9995, MAE = 0.01. Reducción del 70% 
        en sobrestock (ahorro potencial de S/ 10M+ anuales).

        El análisis identificó que la categoría 'Otros', 'Repuestos Técnicos' y 'Equipamiento 
        Personal' concentran el mayor sobrestock en días pico. Se generaron dashboards interactivos 
        con Matplotlib, Seaborn y Plotly para facilitar la toma de decisiones gerenciales.""",
        "technologies": ["Python", "Pandas", "Scikit-learn", "ARIMA", "Random Forest", 
                        "Matplotlib", "Seaborn", "Plotly", "MongoDB", "Jupyter Notebook"],
        "github_urls": [
            {"label": "Repositorio", "url": "https://github.com/Sagiiiii/Analsis-Soreus-Motors-CAPSTOM-PROJECT"},
        ],
        "live_url": "",
        "image_url": "/static/img/datascience.jpg",
        "category": ["data"],
        "featured": True,
    },
    # proyecto 4
    {
        "id": 4,
        "title": "Flutter Components — App Multiplataforma",
        "short_desc": "Colección de componentes reutilizables desarrollados en Flutter para aplicaciones multiplataforma: Android, iOS, Web, Windows, Linux y macOS.",
        "description": """Proyecto de desarrollo multiplataforma construido con Flutter y Dart, 
        orientado a la creación y documentación de componentes reutilizables para aplicaciones 
        modernas. El repositorio incluye soporte nativo para 6 plataformas simultáneas desde 
        una sola base de código.

        Plataformas soportadas:
        • Android — aplicación nativa compilada con Flutter
        • iOS — compatible con dispositivos Apple
        • Web — exportable como aplicación web progresiva (PWA)
        • Windows — aplicación de escritorio nativa
        • Linux — soporte para entornos de escritorio Linux
        • macOS — compatible con el ecosistema Apple Desktop

        Stack tecnológico del repositorio:
        • Dart 63.1% — lenguaje principal de Flutter
        • C++ 30.7% — capas nativas de escritorio
        • CMake 13.5% — sistema de compilación multiplataforma
        • HTML / Swift / C — capas de integración nativa por plataforma

        El proyecto sirve como base de arranque (starter kit) para nuevos proyectos Flutter, 
        incluyendo estructura de carpetas estándar, configuración de assets, análisis estático 
        con analysis_options.yaml y gestión de dependencias con pubspec.""",
        "technologies": ["Flutter", "Dart", "Android", "iOS", "Web", "Windows", "C++", "CMake"],
        "github_urls": [
            {"label": "Repositorio", "url": "https://github.com/Sagiiiii/flutter-components"},
        ],
        "live_url": "",
        "image_url": "/static/img/mobile_flutter.jpg",
        "category": ["mobile"],
        "featured": False,
    },
    # proyecto 5
    {
        "id": 5,
        "title": "Sagiii.dev — Portfolio Personal",
        "short_desc": "Portfolio personal desarrollado con Python + Flask, tema oscuro naranja fox. Muestra proyectos, CV y formulario de contacto.",
        "description": """Portfolio personal diseñado y desarrollado desde cero con Python y Flask, 
        implementando un tema oscuro con paleta de colores fox/naranja personalizada.

        Este mismo sitio que estás viendo fue construido con:
        • Arquitectura Flask con Blueprints para separación de responsabilidades
        • Bootstrap 5 con Dark Mode nativo + CSS personalizado (variables fox)
        • Templates Jinja2 con herencia de plantillas (base.html)
        • Proyectos gestionados desde archivo Python sin base de datos
        • Formulario de contacto con Flask-Mail + Gmail SMTP
        • Preloader animado con sessionStorage para primera visita
        • Diseño responsive adaptado a móvil, tablet y desktop
        • Imagen de perfil circular con efecto glow pulsante naranja
        • Filtros de proyectos por categoría: Web, Frontend, Backend, Mobile, Data Science

        Páginas incluidas:
        • Inicio — Hero con foto, badges de tecnologías y proyectos destacados
        • Proyectos — Galería con filtros y detalle de cada proyecto
        • Sobre mí — CV completo, experiencia profesional y formación académica
        • Contacto — Formulario funcional con envío directo a Gmail
        • Próximamente — Página para proyectos en desarrollo""",
        "technologies": ["Python", "Flask", "Bootstrap 5", "Jinja2", "CSS", "JavaScript",
                        "Flask-Mail", "HTML", "Git"],
        "github_urls": [
            {"label": "Repositorio", "url": "https://github.com/Sagiiiii/sagiiiii-portfolio"},
        ],
        "live_url": "https://sagiiiii-portfolio.onrender.com",
        "image_url": "/static/img/FOX2.jpg",
        "category": ["web", "frontend"],
        "featured": True,
    },

    # proyecto n
]

def get_all():
    return PROJECTS

def get_featured():
    return [p for p in PROJECTS if p.get("featured")]

def get_by_id(id):
    return next((p for p in PROJECTS if p["id"] == id), None)

def get_by_category(cat):
    if not cat:
        return PROJECTS
    # Busca si la categoría está dentro de la lista
    return [p for p in PROJECTS if cat in p["category"]]