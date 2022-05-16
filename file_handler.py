"""Se crea una clase para manejar el archivo: poder abrirlo y obtener el 
contenido, así como crear el archivo con el resultado. Esta clase se utiliza en 
validator y en task_manager"""

from pathlib import Path


class FileHandler():
    """Con esta clase es posible instanciar el objeto responsable de la lectura 
    y escritura de archivos. """

    def __init__(self, path_to_file):
        self.path_to_file = Path(path_to_file)

    def read_file(self):
        """Para leer el archivo y obtener su contenido"""
        with self.path_to_file.open() as file:
            raw_content = file.read()
        return raw_content

    def write_file(self, converted_content, suffix):
        """Para escribir el archivo resultado, que se cree en la misma carpeta 
        que el archivo inicial y que tenga un nombre característico"""
        path_to_folder = self.path_to_file.parent
        filename = self.path_to_file.stem
        path_to_result = path_to_folder / f"{filename}_{suffix}.txt"

        with open(path_to_result, "w") as file:
            file.write(converted_content)
