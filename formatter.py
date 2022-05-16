"""Se define una función para dar formato a la ruta del archivo. Esta función 
se utiliza en main, en task_manager y en validator. También se define la 
función format_content que se utiliza en task_manager y en validator"""


def format_path(path_to_file):
    """Cuando se arrastra un archivo a terminal, la ruta se agrega entre 
    comillas. Esta función es para quitar el entrecomillado en caso de que lo 
    tenga."""

    if path_to_file[0] == "'" and path_to_file[-1] == "'":

        path_to_file = path_to_file[1:-1]

    return path_to_file

def format_content(raw_content):
    """En ocasiones el contenido del archivo viene en minúsculas, con espacios 
    o con enters. Esta función homogeneiza el contenido para trabajar solo con 
    nucleótidos en mayúsculas"""
    
    content = raw_content.upper()
    content = content.replace("\n", "")
    content = content.replace(" ", "")

    return content
