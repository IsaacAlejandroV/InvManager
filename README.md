# InvManager — Sistema de Gestión de Inventario

Sistema web de gestión de inventario desarrollado con tecnologías 100% Open Source como proyecto final de la materia **Sistemas y Lenguajes de Código Abierto** — Universidad Panamericana.

---

## Stack tecnológico

| Capa | Tecnología | Licencia |
|------|-----------|---------|
| Backend | Python 3.11 + Django 4.2 | BSD / Python PSF |
| Base de datos | PostgreSQL 15 | PostgreSQL License |
| Frontend | Bootstrap 5.3 + Bootstrap Icons | MIT |
| Contenedores | Docker + docker-compose | Apache 2.0 |
| Control de versiones | Git + GitHub | GPL-2 / MIT |
| Gestor de proyecto | Taiga | AGPL-3 |

---

## Funcionalidades principales

- **Autenticación y control de acceso** — roles Administrador y Empleado
- **Gestión de Productos** — CRUD completo con categorías y proveedores
- **Movimientos de Inventario** — entradas, salidas y ajustes con historial
- **Alertas de Stock Bajo** — notificaciones automáticas cuando el stock cae al mínimo
- **Dashboard** — KPIs, movimientos recientes y resumen del inventario

---

## Requisitos previos

- Python 3.11+
- PostgreSQL 15+ (o Docker)
- Git

---

## Instalación (sin Docker)

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/sistema-inventario.git
cd sistema-inventario

# 2. Crear y activar entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de PostgreSQL

# 5. Crear la base de datos en PostgreSQL
# psql -U postgres -c "CREATE DATABASE inventario_db;"

# 6. Aplicar migraciones
python manage.py migrate

# 7. Crear superusuario administrador
python manage.py createsuperuser

# 8. Ejecutar el servidor
python manage.py runserver
```

Abrir http://127.0.0.1:8000 en el navegador.

---

## Instalación con Docker

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/sistema-inventario.git
cd sistema-inventario

# 2. Levantar los contenedores
docker-compose up --build

# 3. En otra terminal, crear superusuario
docker-compose exec web python manage.py createsuperuser
```

Abrir http://localhost:8000 en el navegador.

---

## Estructura del proyecto

```
sistema-inventario/
├── inventario/          # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── views.py         # Vista del dashboard
│   └── context_processors.py
├── usuarios/            # App: autenticación y roles
├── productos/           # App: productos, categorías, proveedores
├── movimientos/         # App: entradas, salidas, ajustes, alertas
├── templates/           # Plantillas HTML
├── static/              # Archivos estáticos (CSS)
├── bitacora/            # Bitácora del equipo
├── docs/                # Documentación técnica
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

---

## Equipo

| Integrante | Módulos principales |
|-----------|-------------------|
| Integrante 1 | Autenticación, Dashboard, Movimientos |
| Integrante 2 | Productos, Categorías, Proveedores, Docker |

---

## Licencia

Distribuido bajo la licencia **MIT**. Ver `LICENSE` para más información.

---

## Contribuir

Lee `CONTRIBUTING.md` para las guías de contribución.
