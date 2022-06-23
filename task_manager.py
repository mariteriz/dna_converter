"""
Contiene la función que se encarga manejar las tareas, es decir, de 
conectar la opción elegida con la función correspondiente.
"""

from formatter import format_body, format_path
from file_handler import FileHandler
from converter import count_nucleotides, dna_to_rna, rna_to_protein


def task_manager(option, path_to_file):
    """
    Ejecuta la tarea correspondiente a 'option' sobre el archivo en
    'path_to_file'. Guarda el resultado en un archivo nuevo.

    Args:
        option: una opción del menú
        path_to_file: ruta del archivo 
    """

    path_to_file = format_path(path_to_file)
    file_handler = FileHandler(path_to_file)
    body = file_handler.read_file()

    body = format_body(body)

    if option == "1":
        converted_body = count_nucleotides(body)
        suffix = "nucleotides"

    elif option == "2":
        converted_body = dna_to_rna(body)
        suffix = "to_rna"

    elif option == "3":
        converted_body = rna_to_protein(body)
        suffix = "to_protein"
    
    file_handler.write_file(converted_body, suffix)
