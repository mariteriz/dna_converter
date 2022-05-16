"""Se define la función que se encarga de conectar la opción elegida por el 
usuario con la función correspondiente. También se define una función que nos 
arroja si tenemos un error inesperado en esta fase."""


from formatter import format_content, format_path
from file_handler import FileHandler
from converter import count_nucleotides, dna_to_rna, rna_to_protein


def task_manager(option, path_to_file):
    
    """Crea un objeto con la clase FileHandler y abre el archivo proporcionado 
    por el usuario. """
    path_to_file = format_path(path_to_file)
    file_handler = FileHandler(path_to_file)
    raw_content = file_handler.read_file()

    """Le da formato al contenido y deriva a la función correspondientes según 
    la opción elegida por el usuario."""
    formatted_content = format_content(raw_content)

    if option == "1":
        converted_content = count_nucleotides(formatted_content)
        suffix = "nucleotides"

    elif option == "2":
        converted_content = dna_to_rna(formatted_content)
        suffix = "to_rna"

    elif option == "3":
        converted_content = rna_to_protein(formatted_content)
        suffix = "to_protein"

    """ Una vez terminada la conversión del contenido, escribe el archivo que 
    contiene el resultado."""
    
    file_handler.write_file(converted_content, suffix)

    return converted_content
