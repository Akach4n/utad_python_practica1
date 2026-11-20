from miapp import datos, utilidades

NUMERO_NOTAS = 3
OPCIONES = ("1", "2", "3", "4", "5")
MENU = (
    "\n=== Gestor académico CLI ===\n"
    "1) Registrar alumno/a\n"
    "2) Mostrar alumnado\n"
    "3) Mostrar estadísticas\n"
    "4) Buscar alumno/a\n"
    "5) Salir"
)
SIN_REGISTROS = "No hay alumnado registrado todavía."


def registrar():
    nombre = utilidades.pedir_texto("Nombre del alumno/a: ")
    notas = [utilidades.pedir_nota(f"Nota {indice}: ") for indice in range(1, NUMERO_NOTAS + 1)]
    datos.registrar_alumno(nombre, notas)
    print("Registro guardado correctamente.")


def mostrar_alumnado():
    if not datos.alumnado:
        print(SIN_REGISTROS)
        return
    for registro in datos.alumnado:
        print(datos.formatear_alumno(registro))


def mostrar_estadisticas():
    estadisticas = datos.calcular_estadisticas(datos.alumnado)
    print(datos.formatear_estadisticas(estadisticas) if estadisticas else SIN_REGISTROS)


def buscar():
    registro = datos.buscar_alumno(utilidades.pedir_texto("Nombre a buscar: "))
    print(datos.formatear_detalle(registro) if registro else "Alumno/a no encontrado")


ACCIONES = {"1": registrar, "2": mostrar_alumnado, "3": mostrar_estadisticas, "4": buscar}


def main():
    """Saludo y menú principal."""
    usuario = utilidades.pedir_texto("¿Cómo te llamas? ")
    print(f"Hola, {usuario}")

    while True:
        print(MENU)
        opcion = utilidades.pedir_opcion("Opción: ", OPCIONES)
        if opcion is None:
            continue
        if opcion == "5":
            print("Saliendo. ¡Hasta pronto!")
            break
        print()
        ACCIONES[opcion]()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nSaliendo. ¡Hasta pronto!")
