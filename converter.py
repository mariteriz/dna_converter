"""
Core functions. Functions that transform DNA, RNA and codons sequences. 
"""

def count_nucleotides(nucleotides: str) -> str:
    """
    Count the nucleotides in the DNA or RNA sequence.

    Args:
        nucleotides: a nucleotide (DNA or RNA) sequence.

    Returns: 
        A message indicating the number of nucleotides.
    """
    count = len(nucleotides)
    message = f"La secuencia que ingresaste tiene {count} nucleótidos"

    return message


def dna_to_rna(dna: str) -> str:
    """
    Transcription of DNA to RNA sequence.
    
    Args:
        dna: a DNA nucleotide sequence

    Returns:
        An RNA nucleotide sequence.
    """
    rna = ""

    for nucleotide in dna:
        if nucleotide == "T":
            nucleotide = "U"
        rna = rna + nucleotide

    return rna

def rna_to_codons(rna: str) -> list:
    """
    Converts an RNA sequence to codons.
    
    Args:
        rna: An RNA nucleotide sequence.

    Returns:
        A list of codons.
    """
    return __rna_to_codons(rna, [])

def __rna_to_codons(rna: str, codons: list) -> list:
    """
    Initially this function is called with `codons` = []. Adds the first
    three RNA nucleotides to the `codons` list, then removes those three
    nucleotides from `rna` and repeats it recursively until `rna` is 
    less than 3 in lenght.
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
    Translates an RNA sequence to protein sequence.
    
    Args:
        rna: an RNA sequence
    
    Returns:
        a protein sequence.
    """

    codons = rna_to_codons(rna)

    protein = ""

    for codon in codons:
        aminoacid = CODON_DICTIONARY[codon]
        protein = protein + aminoacid

    return protein
