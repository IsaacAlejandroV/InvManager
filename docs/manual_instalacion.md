# Manual de Instalación — InvManager

## Opción A: Instalación manual (sin Docker)

### Prerrequisitos

- Python 3.11 o superior — https://python.org/downloads
- PostgreSQL 15 — https://www.postgresql.org/download
- Git — https://git-scm.com

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/sistema-inventario.git
cd sistema-inventario
```

### Paso 2 — Crear entorno virtual

```bash
# Crear
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/Mac
source venv/bin/activate
```

### Paso 3 — Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4 — Crear la base de datos

Abrir `psql` y ejecutar:

```sql
CREATE DATABASE inventario_db;
```

### Paso 5 — Configurar variables de entorno

```bash
cp .env.example .env
```

Editar `.env` con tus datos:

```
SECRET_KEY=una-clave-secreta-larga-y-aleatoria
DEBUG=True
DB_NAME=inventario_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```

### Paso 6 — Aplicar migraciones

```bash
python manage.py migrate
```

### Paso 7 — Crear usuario administrador

```bash
python manage.py createsuperuser
```

Ingresar: nombre de usuario, email (opcional) y contraseña.
Luego, en el panel admin o desde el sistema, asignar `rol = admin` al usuario.

> **Nota:** Para que el primer usuario tenga rol de administrador desde el inicio,
> ejecutar en el shell de Django:
> ```bash
> python manage.py shell
> >>> from usuarios.models import Usuario
> >>> u = Usuario.objects.get(username='tu_usuario')
> >>> u.rol = 'admin'
> >>> u.save()
> ```

### Paso 8 — Recopilar archivos estáticos

```bash
python manage.py collectstatic
```

### Paso 9 — Iniciar el servidor

```bash
python manage.py runserver
```

Abrir http://127.0.0.1:8000

---

## Opción B: Instalación con Docker

### Prerrequisitos

- Docker Desktop — https://www.docker.com/products/docker-desktop
- Git

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/sistema-inventario.git
cd sistema-inventario
```

### Paso 2 — Construir y levantar los contenedores

```bash
docker-compose up --build
```

Este comando:
1. Construye la imagen del servidor web
2. Descarga la imagen de PostgreSQL
3. Aplica las migraciones automáticamente
4. Inicia el servidor en el puerto 8000

### Paso 3 — Crear superusuario

En una segunda terminal:

```bash
docker-compose exec web python manage.py createsuperuser
```

### Paso 4 — Acceder al sistema

Abrir http://localhost:8000

### Detener los contenedores

```bash
docker-compose down
```

---

## Verificación de la instalación

Al ingresar al sistema, deberías ver:

1. Pantalla de login con el logo InvManager
2. Dashboard con 4 tarjetas de estadísticas
3. Sidebar con navegación a Productos, Movimientos y (si eres admin) Usuarios

---

## Solución de problemas comunes

| Error | Solución |
|-------|---------|
| `psycopg2.OperationalError` | Verificar que PostgreSQL esté corriendo y las credenciales en `.env` sean correctas |
| `ModuleNotFoundError: decouple` | Ejecutar `pip install -r requirements.txt` con el venv activado |
| Puerto 8000 en uso | Usar `python manage.py runserver 8001` |
| `STATICFILES_DIRS` error en Docker | Ejecutar `python manage.py collectstatic --noinput` |
