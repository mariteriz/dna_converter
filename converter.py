"""
Contiene las funciones núcleo.
Transforman secuencias de nucleótidos de ADN, ARN y codones. 
"""

def count_nucleotides(nucleotides: str) -> str:
    """
    Cuenta los nucleótidos que contiene una secuencia de ADN o ARN.

    Args:
        nucleotides: una secuencia de nucleótidos.

    Returns: 
        Un mensaje que indica el número de nucleótidos.
    """
    count = len(nucleotides)
    message = f"La secuencia que ingresaste tiene {count} nucleótidos"

    return message


def dna_to_rna(dna: str) -> str:
    """
    Transcribe una secuencia de ADN a secuencia de ARN.
    
    Args:
        dna: una secuencia de nucleótidos de ADN.

    Returns:
        Una secuencia de nucleótidos de ARN.
    """
    rna = ""

    for nucleotide in dna:
        if nucleotide == "T":
            nucleotide = "U"
        rna = rna + nucleotide

    return rna

def rna_to_codons(rna: str) -> list:
    """
    Convierte una secuencia de ARN a codones.
    
    Args:
        rna: una secuencia de nucleótidos de ARN.

    Returns:
        Una lista de codones.
    """
    return __rna_to_codons(rna, [])

def __rna_to_codons(rna: str, codons: list) -> list:
    """
    Inicialmente esta función es llamada con 'codons' = [].
    Añade a la lista 'codons' los primeros tres nucleótidos de 'rna', 
    después elimina esos tres nucleótidos de 'rna' y lo repite de forma 
    recursiva hasta que 'rna' tiene una longitud menor a 3.
    """
    CODON_LENGTH = 3

    if len(rna) >= CODON_LENGTH:
        codons.append(rna[0:3])
        rna = rna[3:]
        codons = __rna_to_codons(rna, codons)

    return codons

CODON_DICTIONARY = {  # {codon: aminoacid}
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
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }


def rna_to_protein(rna: str) -> str:
    """
    Traduce una secuencia de ARN a secuencia proteíca.
    
    Args:
        rna: una secuencia de ARN.
    
    Returns:
        una secuencia proteíca.
    """

    codons = rna_to_codons(rna)

    protein = ""

    for codon in codons:
        aminoacid = CODON_DICTIONARY[codon]
        protein = protein + aminoacid

    return protein
