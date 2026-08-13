# 🏋️‍♂️ IronTrack API

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-red.svg)](https://www.sqlalchemy.org/)
[![Package Manager](https://img.shields.io/badge/uv-fast-purple.svg)](https://github.com/astral-sh/uv)
[![Architecture](https://img.shields.io/badge/Architecture-4--Layer%20Monolith-orange.svg)](#-arquitectura)

**IronTrack** es un backend de alto rendimiento diseñado para el seguimiento de entrenamiento físico, rutinas, progreso de fuerza y métricas corporales. Está construido bajo una **arquitectura monolítica modular en 4 capas** estricta, garantizando desacoplamiento, escalabilidad y facilidad de mantenimiento.

---

## 📸 Tabla de Contenidos
- [Vista General y Objetivos](#-vista-general-y-objetivos)
- [Arquitectura (4 Capas)](#-arquitectura-4-capas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Stack Tecnológico](#-stack-tecnológico)
- [Requisitos Previos e Instalación](#-requisitos-previos-e-instalación)
- [Ejecución y Desarrollo](#-ejecución-y-desarrollo)
- [Testing y Calidad de Código](#-testing-y-calidad-de-código)
- [Hoja de Ruta (Roadmap)](#-hoja-de-ruta-roadmap)

---

## 🎯 Vista General y Objetivos

IronTrack proporciona la base sólida para aplicaciones de fitness y gimnasio. El sistema desacopla completamente la lógica de negocio de los detalles de entrega (API REST) y la infraestructura de almacenamiento (Base de datos PostgreSQL/SQLite), permitiendo:

1. **Gestión de Usuarios y Perfiles**: Autenticación JWT, roles y perfiles físicos.
2. **Catálogo de Ejercicios y Rutinas**: Clasificación por grupos musculares, equipamiento y niveles.
3. **Registro de Sesiones de Entrenamiento (Workouts)**: Seguimiento de series, repeticiones, peso (RPE/1RM) y tiempos de descanso.
4. **Métricas y Analíticas**: Progreso histórico, récords personales (PRs) y volumen de carga acumulado.

---

## 🏛 Arquitectura (4 Capas)

El proyecto sigue rigurosamente el patrón de **Monolito en 4 Capas** para evitar acoplamiento directo entre el framework HTTP y la base de datos:

```
┌─────────────────────────────────────────────────────────┐
│              1. Presentation Layer (app/api)            │
│  FastAPI Routers, Request/Response Validation (Schemas)  │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│               2. Business Layer (app/services)          │
│     Lógica de dominio, Reglas de negocio, Casos de uso   │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│              3. Data Access Layer (app/repositories)    │
│      Patrón Repository para consultas y persistencia    │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            4. Infrastructure Layer (app/db)             │
│    Modelos SQLAlchemy, Sesiones DB, Migraciones Alembic │
└─────────────────────────────────────────────────────────┘
```

---

## 📂 Estructura del Proyecto

```text
irontrack/
├── app/
│   ├── api/                # Capa 1: Routers y endpoints (FastAPI)
│   │   └── v1/
│   │       ├── endpoints/  # Controladores HTTP (users, items, workouts, etc.)
│   │       └── router.py   # Router principal v1
│   ├── services/           # Capa 2: Lógica de negocio y reglas de dominio
│   ├── repositories/       # Capa 3: Patrón Repository (Acceso a datos)
│   ├── db/                 # Capa 4: Configuración DB (Engine, SessionMaker, Base)
│   ├── models/             # Modelos ORM SQLAlchemy
│   ├── schemas/            # Esquemas Pydantic (DTOs)
│   ├── integrations/       # Clientes de servicios externos (opcional)
│   └── main.py             # Instancia principal de FastAPI y Middlewares
├── tests/                  # Suite de pruebas automatizadas (espejo de app/)
│   ├── api/
│   ├── services/
│   ├── repositories/
│   ├── db/
│   └── integrations/
├── AGENTS.md               # Definición de sub-agentes de desarrollo
├── CLAUDE.md               # Guía de estándares de codificación
├── pyproject.toml          # Configuración de proyecto y dependencias Python
├── pytest.ini              # Configuración de la suite de pruebas
└── README.md               # Documentación general del proyecto
```

---

## 🛠 Stack Tecnológico

| Componente | Tecnología | Descripción |
| :--- | :--- | :--- |
| **Lenguaje** | Python 3.12+ / 3.14 | Entorno de ejecución con tipos estrictos |
| **Framework HTTP** | FastAPI 0.136+ | API REST asíncrona de alto rendimiento |
| **ORM** | SQLAlchemy 2.0+ | Mapper Objeto-Relacional asíncrono |
| **Validación** | Pydantic v2 | Serialización y validación de tipos |
| **Gestor de Paquetes** | `uv` | Administrador ultrarrápido de dependencias Python |
| **Migraciones** | Alembic | Control de versiones del esquema de base de datos |
| **Pruebas** | pytest / pytest-asyncio | Suite de pruebas unitarias e integración |

---

## 🚀 Requisitos Previos e Instalación

### Requisitos
- **Python 3.12+** (o compatible con el entorno especificado en `pyproject.toml`)
- **uv** (Gestor de entorno y paquetes de Python)

### Instalación de `uv` (si no lo tienes instalado)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clonar e Instalar Dependencias
```bash
# Clonar repositorio
git clone <repository-url>
cd irontrack

# Crear entorno virtual e instalar dependencias con uv
uv sync
```

---

## 💻 Ejecución y Desarrollo

### Servidor de Desarrollo
Para levantar la aplicación FastAPI en modo recarga automática (hot reload):

```bash
uv run uvicorn app.main:app --reload --port 8000
```

Una vez ejecutado, la documentación interactiva estará disponible en:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Testing y Calidad de Código

### Ejecutar Pruebas Automatizadas
Para correr toda la suite de pruebas con `pytest`:

```bash
uv run pytest
```

### Ejecutar con Cobertura (Coverage)
```bash
uv run pytest --cov=app --cov-report=term-missing
```

---

## 📋 Hoja de Ruta (Roadmap)

- [ ] **Fase 1: Infraestructura Base**
  - Implementar conexión de base de datos asíncrona (`AsyncSession`) en `app/db/`.
  - Inicializar migraciones con Alembic.
  - Implementar middleware de manejo global de excepciones y CORS.
- [ ] **Fase 2: Autenticación y Usuarios**
  - Modelo `User`, esquema `UserCreate`/`UserOut`, repositorio y servicio de hashing de contraseñas.
  - Endpoints de Login (`/api/v1/auth/login`) y Registro (`/api/v1/auth/register`).
- [ ] **Fase 3: Dominio Fitness (Workouts & Exercises)**
  - Modelos SQLAlchemy para Ejercicios, Rutinas y Sesiones.
  - Repositorios genéricos y servicios de cálculo de volumen y RPE.
- [ ] **Fase 4: Cobertura de Pruebas**
  - Alcanzar >80% de cobertura en capas `services` y `repositories`.
