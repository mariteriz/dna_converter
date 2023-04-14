"""
Function that is in charge of managing tasks, that is, that connects the 
chosen option with the corresponding function.
"""

from data_parser import format_body, format_path
from file_handler import FileHandler
from converter import count_nucleotides, dna_to_rna, rna_to_protein


def task_manager(option, path_to_file):
    """
    Run the task corresponding to `option` on the file at 
    `path_to_file`. Save the result in a new file.

    Args:
        option: one of the options available on the menu.
        path_to_file: the file path
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
