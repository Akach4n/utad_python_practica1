**Nombre completo:** Izan Fernández Martín\
**Curso:** 2ºDAW\
**Asignatura:** Optativa 2 (Python)\
**Centro:** U-tad

# Gestor académico CLI

Aplicación de consola en **Python** para registrar alumnado con tres notas, ver sus medias, sacar estadísticas y buscar por nombre. Los datos se guardan en memoria.

## Puesta en marcha

Requiere **Python 3.x**. Desde la raíz del proyecto:

```bash
python main.py
```

## Estructura

```
├─ main.py             # menú principal, delega en miapp
├─ miapp/
│  ├─ __init__.py      # convierte miapp en paquete
│  ├─ datos.py         # alumnado, medias, búsqueda y estadísticas
│  └─ utilidades.py    # entrada, validación y normalización
└─ README.md
```

## Ejemplo de uso

```
Opción: 1
Nombre del alumno/a: marta
Nota 1: 7
Nota 2: 8
Nota 3: 6
Registro guardado correctamente.

Opción: 2
Marta           Media: 7.00   Aprobado
```
