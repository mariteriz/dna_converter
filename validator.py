"""Se definen las funciones necesarias para validar que la opción ingresada por 
el usuario sea correcta, que el archivo exista y que el contenido del archivo 
tenga las características adecuadas. Estas funciones se utilizan en main.py"""


from pathlib import Path
from file_handler import FileHandler
from formatter import format_content, format_path


def is_option_valid(option):
    """El menú presenta solo las opciones 0, 1, 2 y 3, así que cualquier otro 
    carácter ingresado por el usuario será una opción inválida"""
    is_option_valid = option in "0123"

    return is_option_valid


def file_exists(path_to_file):
    """Para confirmar que la ruta que el usuario nos dio, corresponda a un 
    archivo que sí existe"""
    path_to_file = Path(path_to_file)
    file_exists = path_to_file.is_file()

    return file_exists


def is_content_valid(path_to_file):
    """Para confirmar que el contenido del archivo proporcionado por el usuario 
    corresponde a una secuencia de ADN o de ARN, es decir, que contiene 
    únicamente símbolos de nucleótidos: A, G, C, T, U"""

    path_to_file = format_path(path_to_file)
    file_handler = FileHandler(path_to_file)
    raw_content = file_handler.read_file()
    formatted_content = format_content(raw_content)

    for nucleotide in formatted_content:

        if nucleotide in "AGCTU":
            is_content_valid = True
        else:
            is_content_valid = False
            break

    return is_content_valid
