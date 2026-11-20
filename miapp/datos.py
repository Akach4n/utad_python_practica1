NOTA_APROBADO = 5.0

alumnado = []


def calcular_media(notas):
    """Media de una lista de notas."""
    if not notas:
        return 0.0
    return float(sum(notas) / len(notas))


def esta_aprobado(media):
    """True si la media es >= 5."""
    return media >= NOTA_APROBADO


def texto_resultado(media):
    return "Aprobado" if esta_aprobado(media) else "Suspenso"


def registrar_alumno(nombre, notas):
    """Añade un alumno/a a la lista."""
    registro = {"nombre": nombre, "notas": list(notas)}
    alumnado.append(registro)
    return registro


def buscar_alumno(nombre):
    """Busca por nombre sin distinguir mayúsculas."""
    nombre_buscado = nombre.strip().lower()
    for registro in alumnado:
        if registro["nombre"].lower() == nombre_buscado:
            return registro
    return None


def calcular_estadisticas(lista_alumnado):
    """Total, media global, aprobados, suspensos y mejor media."""
    if not lista_alumnado:
        return None

    medias = [(registro["nombre"], calcular_media(registro["notas"])) for registro in lista_alumnado]
    aprobados = sum(1 for _, media in medias if esta_aprobado(media))
    mejor_nombre, mejor_media = max(medias, key=lambda par: par[1])

    return {
        "total": len(medias),
        "media_global": calcular_media([media for _, media in medias]),
        "aprobados": aprobados,
        "suspensos": len(medias) - aprobados,
        "mejor_nombre": mejor_nombre,
        "mejor_media": mejor_media,
    }


def formatear_alumno(registro):
    media = calcular_media(registro["notas"])
    return f"{registro['nombre']:<15} Media: {media:.2f}   {texto_resultado(media)}"


def formatear_detalle(registro):
    notas = "  ".join(f"Nota {indice}: {nota:g}" for indice, nota in enumerate(registro["notas"], start=1))
    return f"{registro['nombre']}\n{notas}\n{formatear_alumno(registro)}"


def formatear_estadisticas(estadisticas):
    return (
        f"Personas registradas: {estadisticas['total']}\n"
        f"Media global: {estadisticas['media_global']:.2f}\n"
        f"Aprobados: {estadisticas['aprobados']}\n"
        f"Suspensos: {estadisticas['suspensos']}\n"
        f"Mejor media: {estadisticas['mejor_nombre']} ({estadisticas['mejor_media']:.2f})"
    )
