# Arquitectura del Sistema — InvManager

## Diagrama de arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENTE (Browser)                    │
│              Bootstrap 5 + Bootstrap Icons              │
└─────────────────────┬───────────────────────────────────┘
                      │  HTTP/HTTPS
┌─────────────────────▼───────────────────────────────────┐
│                 Django 4.2 (MVT)                        │
│  ┌────────────┐  ┌─────────────┐  ┌──────────────────┐  │
│  │  usuarios  │  │  productos  │  │   movimientos    │  │
│  │            │  │             │  │                  │  │
│  │ models     │  │ models      │  │ models           │  │
│  │ views      │  │ views       │  │ views            │  │
│  │ forms      │  │ forms       │  │ forms            │  │
│  │ urls       │  │ urls        │  │ urls             │  │
│  └────────────┘  └─────────────┘  └──────────────────┘  │
│                                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │          templates/ (Django Templates)          │    │
│  │   base.html ← dashboard, productos, movimientos │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────┬───────────────────────────────────┘
                      │  psycopg2
┌─────────────────────▼───────────────────────────────────┐
│                   PostgreSQL 15                         │
│  usuarios_usuario | productos_producto | ...            │
└─────────────────────────────────────────────────────────┘
```

## Modelo de datos

### usuarios_usuario
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | BigInt PK | |
| username | Varchar(150) | único |
| first_name, last_name | Varchar | |
| email | Varchar | |
| rol | Varchar(10) | admin / empleado |
| telefono | Varchar(20) | |
| is_active | Boolean | |

### productos_categoria
| Campo | Tipo |
|-------|------|
| id | BigInt PK |
| nombre | Varchar(100) único |
| descripcion | Text |

### productos_proveedor
| Campo | Tipo |
|-------|------|
| id | BigInt PK |
| nombre | Varchar(200) |
| contacto, telefono, email, direccion | Varchar/Text |
| activo | Boolean |

### productos_producto
| Campo | Tipo |
|-------|------|
| id | BigInt PK |
| nombre | Varchar(200) |
| codigo | Varchar(50) único |
| categoria_id | FK → Categoria |
| proveedor_id | FK → Proveedor |
| precio_compra, precio_venta | Decimal(10,2) |
| stock_actual, stock_minimo | Integer |
| unidad_medida | Varchar(10) |
| activo | Boolean |

### movimientos_movimientoinventario
| Campo | Tipo |
|-------|------|
| id | BigInt PK |
| producto_id | FK → Producto |
| tipo | Varchar(10): entrada/salida/ajuste |
| cantidad | Integer |
| stock_anterior, stock_posterior | Integer |
| precio_unitario | Decimal(10,2) |
| notas | Text |
| usuario_id | FK → Usuario |
| fecha | DateTimeField auto |

## Patrones de diseño

- **MVT** (Model-View-Template) — patrón nativo de Django
- **Class-Based Views** para todas las vistas CRUD
- **Context Processor** global para el contador de alertas en el sidebar
- **Soft Delete** en Producto y Proveedor (campo `activo`)
- **LoginRequiredMixin + AdminRequiredMixin** para control de acceso

## Tecnologías y licencias

| Tecnología | Versión | Licencia |
|-----------|---------|---------|
| Python | 3.11 | PSF |
| Django | 4.2 LTS | BSD-3 |
| PostgreSQL | 15 | PostgreSQL |
| Bootstrap | 5.3.3 | MIT |
| Bootstrap Icons | 1.11.3 | MIT |
| Docker | latest | Apache 2.0 |
| psycopg2-binary | 2.9.9 | LGPL-3 |
| python-decouple | 3.8 | MIT |
