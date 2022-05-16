"""Se definen las funciones que corresponden a cada opción del menú y que van a 
llevar a cabo la tarea de convertir el contenido del archivo inicial al 
resultado. Estas funciones se utilizan en task_manager."""


def count_nucleotides(formatted_content):
    """Cuenta los nucleótidos que contiene la secuencia de ADN o ARN"""
    count_nucleotides = str(len(formatted_content))
    message = f"La secuencia que ingresaste tiene {count_nucleotides} nucleótidos"

    return message


def dna_to_rna(formatted_content):
    """Transcribe la secuencia de ADN (que contiene A, G, C y T) a secuencia de 
    ARN (que contiene A, G, C y U), es decir, cambia las T por U."""
    rna = ""

    for nucleotide in formatted_content:
        if nucleotide == "T":
            nucleotide = "U"
        rna = rna + nucleotide

    return rna


def rna_to_codons(content, codons):
    """Parte la secuencia de ARN en una lista con cadenas de 3 caracteres 
    (codones) utilizando recursividad. El parámetro codons debe ser 
    inicialmente una lista vacía."""
    if len(content) >= 3:
        codons.append(content[0:3])
        content = content[3:]
        codons = rna_to_codons(content, codons)

    return codons


"""Se escribe la traducción de codones (ARN) a aminoácidos (proteína) en forma 
de diccionario. Cada codón es una 'palabra' y su 'definición' es el aminoácido 
que le corresponde."""

CODON_DICTIONARY = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}


def rna_to_protein(content):
    """Manda llamar la función de rna_to_codons() para obtener la lista de 
    codones que se van a traducir de ARN a proteína. Compara cada codón con el 
    diccionario y escribe la secuencia de aminoácidos (proteína) en un nuevo 
    string."""

    codons = rna_to_codons(content, [])

    protein = ""

    for codon in codons:
        aminoacid = CODON_DICTIONARY[codon]
        protein = protein + aminoacid

    return protein
