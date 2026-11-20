NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0


def normalizar_nombre(texto):
    """Quita espacios y capitaliza."""
    return texto.strip().capitalize()


def pedir_texto(mensaje):
    """Pide un texto no vacío."""
    while True:
        texto = normalizar_nombre(input(mensaje))
        if texto:
            return texto
        print("El nombre no puede estar vacío. Inténtalo de nuevo.")


def pedir_nota(mensaje):
    """Pide una nota entre 0 y 10."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            nota = float(entrada)
        except ValueError:
            print("La nota debe ser un número. Inténtalo de nuevo.")
            continue
        if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            return nota
        print(f"La nota debe estar entre {NOTA_MINIMA:g} y {NOTA_MAXIMA:g}. Inténtalo de nuevo.")


def pedir_opcion(mensaje, opciones_validas):
    """Pide una opción del menú."""
    opcion = input(mensaje).strip()
    if opcion in opciones_validas:
        return opcion
    print("Opción no válida. Elige una opción del menú.")
    return None
