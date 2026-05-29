
# Bitácora del Equipo — InvManager

Registro de avances, decisiones y obstáculos del proyecto.

---

## Semana 1 — Propuesta y configuración inicial

**Fecha:** Mayo 2025  
**Participantes:** wlad, isaac

### Avances
- Definición del sistema a desarrollar: gestión de inventario para PyME
- Configuración del repositorio en GitHub
- Elección del stack: Django + PostgreSQL + Bootstrap 5
- Configuración del tablero en Taiga con milestones y sprints
- Instalación del entorno de desarrollo

### Decisiones
- **Taiga** como gestor de proyecto (tecnología analizada en el Primer Parcial)
- **MIT License** para el proyecto
- Arquitectura MVC con 3 apps Django independientes

### Obstáculos
- Configuración inicial de PostgreSQL en Windows 

---

## Semana 2 — Modelos y autenticación

**Fecha:** Mayo 2025  
**Participantes:** wlad, isaac

### Avances
- Definición de modelos: Usuario, Categoria, Proveedor, Producto, MovimientoInventario
- Implementación del modelo de usuario personalizado (AbstractUser + rol)
- Sistema de autenticación y control de acceso por roles
- Migraciones iniciales aplicadas

### Decisiones
- El campo `stock_actual` se actualiza directamente en la vista de movimientos
- `activo = False` como soft-delete para productos y proveedores

### Obstáculos
- Cambio de `AUTH_USER_MODEL` requirió limpiar migraciones y recrear la BD

---

## Semana 3 — CRUD de productos y movimientos

**Fecha:** Mayo 2025  
**Participantes:** wlad, isaac

### Avances
- CRUD completo de productos, categorías y proveedores
- Módulo de movimientos de inventario (entradas/salidas/ajustes)
- Dashboard con KPIs y alertas de stock bajo
- Templates con Bootstrap 5 y sidebar de navegación
- Configuración de Docker y docker-compose


## Semana 4 — Documentación y pruebas finales

**Fecha:** Mayo 2025  
**Participantes:** wlad, isaac

### Avances
- README, LICENSE y CONTRIBUTING.md
- Manual de instalación y arquitectura
- Grabación del video de presentación
- Corrección de bugs finales
- Deploy de prueba


