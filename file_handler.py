from pathlib import Path


class FileHandler():
    """
    This class represents a file operator.

    Class has a path attribute and does reading and writing from it.

    Attributes:
        path_to_file (Path): Stores the path of the file with which 
        operate the object.
    """

    def __init__(self, path_to_file: str):
        """
        Constructor method.

        Args:
            path_to_file: path of a file
        """

        self.path_to_file = Path(path_to_file)

    def read_file(self) -> str:
        """
        Read a file and return its content.

        Returns: 
            The content of a file.

        """

        with self.path_to_file.open() as file:
            body = file.read()
        return body

    def write_file(self, body: str, suffix: str):
        """
        Creates a .txt file in the `path_to_file` folder, with `body` as
        content. The file name is derived from `path_to_file` and the 
        suffix `suffix`.

        Args: 
            body: the content of a file.
            suffix: the suffix of the file name.
        """

        path_to_folder = self.path_to_file.parent
        filename = self.path_to_file.stem
        path_to_result = path_to_folder / f"{filename}_{suffix}.txt"

        with open(path_to_result, "w") as file:
            file.write(body)
