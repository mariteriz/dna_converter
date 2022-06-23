from pathlib import Path


class FileHandler():
    """
    Una clase para representar un operador de archivos.

    La clase tiene un atributo Path y hace operaciones de lectura y 
    escritura a partir de él.

    Atrributes:
        path_to_file (Path): Almacena la ruta del archivo con la que
        opera el objeto.
    """

    def __init__(self, path_to_file: str):
        """
        Método constructor de clase.

        Args:
            path_to_file: Ruta de un archivo.
        """

        self.path_to_file = Path(path_to_file)

    def read_file(self) -> str:
        """
        Lee un archivo y regresa su contenido.

        Returns: 
            El contenido del archivo.

        """

        with self.path_to_file.open() as file:
            body = file.read()
        return body

    def write_file(self, body: str, suffix: str):
        """
        Crea un archivo .txt en la carpeta de path_to_file, con
        contenido body. El nombre del archivo se deriva de path_to_file
        y el sufijo suffix.

        Args: 
            body: el contenido del archivo.
            suffix: el sufijo del nombre del archivo.
        """

        path_to_folder = self.path_to_file.parent
        filename = self.path_to_file.stem
        path_to_result = path_to_folder / f"{filename}_{suffix}.txt"

        with open(path_to_result, "w") as file:
            file.write(body)
