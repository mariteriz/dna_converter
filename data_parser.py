"""
Contiene funciones utilitarias relacionadas con dar formato. 
"""

def format_body(body: str) -> str:
    """
    Da formato al cuerpo de un archivo de texto:
        - Convierte todos los caracteres a mayúsculas.
        - Elimina los enters.
        - Elimina los espacios.

    Args:
        body: el cuerpo de un archivo.

    Returns:
        El cuerpo de un archivo formateado.
    """

    body = body.upper()
    body = body.replace("\n", "")
    body = body.replace(" ", "")

    return body

def format_path(path: str) -> str:
    """
    Da formato a una ruta:
        - Elimina las comillas a los extremos de la ruta.

    Args:
        path: una ruta.

    Returns:
        Un string de una ruta con formato.
    """

    path = remove_spaces(path)
    path = remove_quotes(path)

    return path

def remove_quotes(string: str) -> str:
    """
    Elimina las comillas a los extremos de un string, en caso de que las tenga.

    Args:
        string: cualquier string.

    Returns:
        Un string sin comillas en los extremos.
    """

    if string[0] == "'" and string[-1] == "'":
        string = string[1:-1]

    return string

def remove_spaces(string: str) -> str:
    """
    Elimina los espacios a los extremos de un string, en caso de que los tenga.

    Args:
        string: cualquier string.

    Returns:
        Un string sin espacios en los extremos.
    """

    if string[0] == " ":
        string = string[1:]

    if string[-1] == " ":
        string = string[:-1]

    return string
