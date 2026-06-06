# RecargaYa S.A.S.

## Descripción

Este proyecto implementa una solución para el cálculo de recargas telefónicas utilizando las prácticas de Desarrollo Guiado por Pruebas (TDD), Desarrollo Guiado por Comportamiento (BDD), una API REST con FastAPI, pruebas de rendimiento con Locust e Integración Continua mediante GitHub Actions.

El sistema valida el monto de la recarga, calcula las bonificaciones correspondientes y aplica beneficios adicionales para usuarios premium.

---

## Reglas de negocio

### Validación de montos

- Monto mínimo permitido: $1.000
- Monto máximo permitido: $50.000

Si el monto está fuera de este rango, la recarga será rechazada.

### Bonificaciones

- Recargas entre $10.000 y $29.999 reciben una bonificación del 10%.
- Recargas desde $30.000 reciben una bonificación del 25%.

### Usuarios Premium

Los usuarios premium reciben un 5% adicional sobre la bonificación obtenida.

### Ejemplos

| Monto | Premium | Bonificación |
|--------|----------|-------------|
| $5.000 | No | 0% |
| $10.000 | No | 10% |
| $10.000 | Sí | 15% |
| $30.000 | No | 25% |
| $30.000 | Sí | 30% |

---

## Casos de prueba

### Partición de equivalencia

| ID | Tipo | Entrada | Resultado esperado |
|----|------|----------|-------------------|
| CP-01 | Inválido | 500 | Recarga rechazada |
| CP-02 | Válido | 5.000 | Bonificación 0% |
| CP-03 | Válido | 10.000 | Bonificación 10% |
| CP-04 | Válido | 30.000 | Bonificación 25% |
| CP-05 | Inválido | 60.000 | Recarga rechazada |

### Análisis de valores límite

| ID | Entrada | Resultado esperado |
|----|----------|-------------------|
| VL-01 | 999 | Recarga rechazada |
| VL-02 | 1.000 | Recarga válida |
| VL-03 | 1.001 | Recarga válida |
| VL-04 | 49.999 | Recarga válida |
| VL-05 | 50.000 | Recarga válida |
| VL-06 | 50.001 | Recarga rechazada |

### Casos automatizados (TDD)

| ID | Escenario | Resultado esperado |
|----|------------|-------------------|
| TDD-01 | Recarga menor a $1.000 | Inválida |
| TDD-02 | Recarga mayor a $50.000 | Inválida |
| TDD-03 | Recarga de $10.000 | Bonificación 10% |
| TDD-04 | Recarga de $30.000 | Bonificación 25% |
| TDD-05 | Usuario premium con recarga de $30.000 | Bonificación 30% |

### Cobertura de reglas de negocio

| Regla | Casos que la validan |
|---------|---------------------|
| Monto mínimo permitido | CP-01, VL-01, VL-02 |
| Monto máximo permitido | CP-05, VL-05, VL-06 |
| Bonificación del 10% | CP-03, TDD-03 |
| Bonificación del 25% | CP-04, TDD-04 |
| Bonificación premium (+5%) | TDD-05 |

---

## Tecnologías utilizadas

- Python 3
- Pytest
- FastAPI
- Uvicorn
- Locust
- GitHub Actions

---

## Instalación

### Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd parcial_pruebas2
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de pruebas unitarias

```bash
python -m pytest
```

Resultado esperado:

```text
===== test session starts =====
collected 5 items

tests/test_recarga.py ..... [100%]

===== 5 passed =====
```

---

## Desarrollo guiado por pruebas (TDD)

Durante el desarrollo se siguió el ciclo:

1. RED → Crear una prueba que falle.
2. GREEN → Implementar el mínimo código para aprobarla.
3. REFACTOR → Mejorar el código sin modificar su comportamiento.

---

## Desarrollo guiado por comportamiento (BDD)

Los escenarios BDD fueron definidos utilizando sintaxis Gherkin.

Archivo:

```text
features/recarga.feature
```

Escenarios cubiertos:

- Recarga válida sin bonificación.
- Recarga con bonificación del 10%.
- Recarga con bonificación del 25%.
- Usuario premium.
- Validación de montos mediante Scenario Outline.

---

## Ejecución de la API

```bash
uvicorn app.main:app --reload
```

La API quedará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación Swagger

FastAPI genera automáticamente la documentación interactiva.

```text
http://127.0.0.1:8000/docs
```

---

## Pruebas de rendimiento

Las pruebas de carga fueron implementadas utilizando Locust.

Ejecutar:

```bash
locust
```

Luego abrir:

```text
http://localhost:8089
```

Configuración recomendada:

- Usuarios: 30
- Spawn Rate: 5

Objetivo:

- Percentil P95 menor a 300 ms.

---

## Integración continua

El proyecto incluye una canalización de integración continua mediante GitHub Actions.

Archivo:

```text
.github/workflows/test.yml
```

La canalización ejecuta automáticamente:

- Instalación de dependencias.
- Ejecución de pruebas unitarias.
- Verificación de errores en cada push y pull request.

---

## Estructura del proyecto

```text
parcial_pruebas2/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── service.py
│
├── tests/
│   ├── __init__.py
│   └── test_recarga.py
│
├── features/
│   └── recarga.feature
│
├── docs/
│   └── casos_prueba.md
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── locustfile.py
├── requirements.txt
└── README.md
```