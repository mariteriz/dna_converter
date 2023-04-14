"""
Utility functions related to data formatting.
"""

def format_body(body: str) -> str:
    """
    Format the body of a text file:
        - Converts all characters to uppercase.
        - Deletes enters.
        - Remove spaces.

    Args:
        body: the body of a file.

    Returns:
        Formatted body of a file.
    """

    body = body.upper()
    body = body.replace("\n", "")
    body = body.replace(" ", "")

    return body

def format_path(path: str) -> str:
    """
    Format a path:
        - Remove the quotes at the ends of the path.

    Args:
        path: a path

    Returns:
        Formatted string path
    """

    path = remove_spaces(path)
    path = remove_quotes(path)

    return path

def remove_quotes(string: str) -> str:
    """
    Removes the quotes at the ends of a string, in case it has them.

    Args:
        string: any string.

    Returns:
        A string without quotes at the ends.
    """

    if string[0] == "'" and string[-1] == "'":
        string = string[1:-1]

    return string

def remove_spaces(string: str) -> str:
    """
    Removes the spaces at the ends of a string, in case it has them.

    Args:
        string: any string.

    Returns:
        A string without spaces at the ends.
    """

    if string[0] == " ":
        string = string[1:]

    if string[-1] == " ":
        string = string[:-1]

    return string
