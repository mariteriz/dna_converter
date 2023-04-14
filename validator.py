"""
Functions required for validation.
"""

from pathlib import Path
from file_handler import FileHandler
from data_parser import format_body, format_path


def is_option_valid(option: str) -> bool:
    """
    Evaluates if the given option appears on the menu.

    Args: 
        option: one of the options available on the menu.

    Returns: 
        True if the option is on the menu, False if it is not on the 
        menu.
    """

    option_valid = option in "0123"

    return option_valid


def file_exists(path_to_file: str) -> bool:
    """
    Evaluates if a path corresponds to a file that does exist.
    
    Args:
        path_to_file: a path

    Returns: 
        True if the file exists, False if the file does not exist.
    """

    path_to_file = Path(path_to_file)
    exists = path_to_file.is_file()

    return exists


def is_body_valid(path_to_file: str) -> bool:
    """
    Evaluates that the content of the file corresponds to a DNA or RNA 
    sequence.
    
    Args:
        path_to_file: a path

    Returns:
        True if the content of the file corresponds to a DNA or RNA 
        sequence, False if it does not.
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
