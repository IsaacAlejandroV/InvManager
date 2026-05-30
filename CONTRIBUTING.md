# Guía de Contribución — InvManager

Gracias por querer contribuir a InvManager. Este documento establece las convenciones del equipo.

---

## Flujo de trabajo con Git

### Branches

| Branch | Propósito |
|--------|----------|
| `main` | Código estable y en producción |
| `develop` | Integración de nuevas features |
| `feature/<nombre>` | Desarrollo de una nueva funcionalidad |
| `fix/<nombre>` | Corrección de un bug |

### Convención de commits

Seguimos **Conventional Commits**:

```
<tipo>(<scope>): <descripción corta en español>

Ejemplos:
feat(productos): agregar campo de imagen al producto
fix(movimientos): corregir validación de stock negativo
docs(readme): actualizar instrucciones de instalación
refactor(usuarios): extraer mixin de permisos
test(productos): agregar pruebas para CategoriaForm
```

Tipos permitidos: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Pull Requests

1. Crear branch desde `develop`: `git checkout -b feature/mi-feature`
2. Hacer commits atómicos y descriptivos
3. Abrir PR hacia `develop` con descripción de los cambios
4. Solicitar review de al menos un integrante
5. Mergear solo con aprobación

---

## Estilo de código

- Seguir PEP 8 para Python
- Máximo 100 caracteres por línea
- Docstrings en español para funciones no triviales
- Variables y funciones en `snake_case`
- Clases en `PascalCase`

---

## Configurar el entorno de desarrollo

```bash
git clone https://github.com/TU_USUARIO/sistema-inventario.git
cd sistema-inventario
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env   # Editar con credenciales locales
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Reporte de issues

Usar los issues de GitHub con las etiquetas:
- `bug` — algo no funciona como se esperaba
- `feature` — solicitud de nueva funcionalidad
- `docs` — mejora en la documentación

---

## Código de conducta

Tratamos a todos los colaboradores con respeto. No se toleran comentarios ofensivos ni actitudes excluyentes.
