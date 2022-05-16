"""El archivo que se ejecuta y en el que se da la interacción con el usuario."""

from formatter import format_path
from task_manager import task_manager
from validator import is_option_valid, file_exists, is_content_valid

"""Se describe el menú de opciones y se escribe un mensaje de bienvenida que se 
verá cuando se ejecute el archivo."""
MENU = """
1) Contar nucleotidos
2) Transcribir ADN a ARN
3) Traducir ARN a Proteína

0) Salir
"""

print("Bienvenido")

"""Inicia un ciclo while en True para que se ejecute hasta que el usuario 
indique lo contrario."""
while True:

    print(MENU)

    option = input("\nIngresa el número correspondiente a la opción deseada: ")

    """Si se ingresa la opción 0, sale del ciclo while y cierra el programa."""
    if option == "0":
        break

    """Valida la opción llamando a la función definida en validator.py. En caso 
    de que no sea una opción válida, regresa al inicio del ciclo while."""
    if not is_option_valid(option):
        print("\n ¡OPCIÓN INVÁLIDA! Por favor, inténtalo de nuevo: ")
        continue

    path_to_file = input(
        "Ingresa la ruta de tu archivo o arrástralo a la terminal: ")

    path_to_file = format_path(path_to_file)

    """Valida que el archivo que indicó el usuario exista llamando a la función 
    definida en validator. En caso de que el archivo no exista, regresa al 
    inicio del ciclo while."""
    if not file_exists(path_to_file):
        print("\n ¡ERROR! El archivo no existe. Por favor, inténtalo de nuevo: ")
        continue

    """Valida que el contenido del archivo sea lo esperado mandando llamar la 
    función definida en validator"""
    if not is_content_valid(path_to_file):
        print("\n ¡ERROR! El contenido del archivo no corresponde a ADN ni a ARN. Por favor, inténtalo de nuevo: ")
        continue

    """Manda llamar a la función definida en task_manager para realizar la 
    tarea que corresponde a la opción elegida por el usuario."""
    task_manager(option, path_to_file)

    print("\n Tarea completada, ¿qué quieres hacer ahora?")

print("\n¡Hasta luego!")
