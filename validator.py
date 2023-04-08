"""
Contiene funciones necesarias para validación.
"""

from pathlib import Path
from file_handler import FileHandler
from data_parser import format_body, format_path


def is_option_valid(option: str) -> bool:
    """
    Evalúa si la opción se encuentra en el menú.

    Args: 
        option: una de las opciones disponibles en el menú.

    Returns: 
        True si la opción está en el menú, False si no lo está.
    """

    option_valid = option in "0123"

    return option_valid


def file_exists(path_to_file: str) -> bool:
    """
    Evalúa si una ruta corresponde a un archivo que sí existe.
    
    Args:
        path_to_file: una ruta

    Returns: 
        True si el archivo existe, False si el archivo no existe.
    """

    path_to_file = Path(path_to_file)
    exists = path_to_file.is_file()

    return exists


def is_body_valid(path_to_file: str) -> bool:
    """
    Evalúa que el contenido del archivo corresponda a una secuencia 
    de ADN o de ARN.
    
    Args:
        path_to_file: una ruta

    Returns:
        True si el contenido del archivo corresponde a una secuencia de 
        ADN o de ARN, False si no corresponde.
    """

    path_to_file = format_path(path_to_file)
    file_handler = FileHandler(path_to_file)
    body = file_handler.read_file()
    body = format_body(body)

    for nucleotide in body:

        if nucleotide in "AGCTU":
            body_valid = True
        else:
            body_valid = False
            break

    return body_valid
