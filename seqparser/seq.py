# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    if set(seq).difference(set(ALLOWED_NUC)): #change into sets and just test !intersection
        raise ValueError("Invalid Nucleotide")
    
    transcribed = "".join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq if nuc in ALLOWED_NUC)
    #original approach I though was to use the dictionary, and do .str.replace(), but .str.replace() internally 
    #loops through the string and replaces each instance. Instead we use a generator here
    
    if reverse:
        return transcribed[::-1]
    else:
        return transcribed

    
def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True)