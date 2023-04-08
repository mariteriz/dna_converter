"""
El archivo que se ejecuta y en el que se da la interacción con el 
usuario.
"""

from data_parser import format_path
from task_manager import task_manager
from validator import is_option_valid, file_exists, is_body_valid


MENU = """
1) Contar nucleotidos
2) Transcribir ADN a ARN
3) Traducir ARN a Proteína

0) Salir
"""

print("Bienvenido")

# Inicia un ciclo while en True para que el programa se ejecute hasta que
# el usuario indique lo contrario.
while True:

    print(MENU)

    option = input("\nIngresa el número correspondiente a la opción deseada: ")

    # Si se ingresa la opción 0, sale del ciclo while para terminar el
    # programa.
    if option == "0":
        break

    if not is_option_valid(option):
        print("\n ¡OPCIÓN INVÁLIDA! Por favor, inténtalo de nuevo: ")
        continue

    path_to_file = input(
        "Ingresa la ruta de tu archivo o arrástralo a la terminal: ")

    path_to_file = format_path(path_to_file)

    if not file_exists(path_to_file):
        print("\n ¡ERROR! El archivo no existe. Por favor, inténtalo de nuevo: ")
        continue

    if not is_body_valid(path_to_file):
        print("\n ¡ERROR! El contenido del archivo no contiene una secuencia "
              "de ADN o ARN. Por favor, inténtalo de nuevo: ")
        continue

    task_manager(option, path_to_file)

    print("\n Tarea completada, ¿qué quieres hacer ahora?")

print("\n¡Hasta luego!")
