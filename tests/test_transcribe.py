# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest 

#Define some seqs

wrong_seq = "ATCGZ"
test_seq = "ATCG"
transcribe_seq = "UAGC"
reverse_transcribe_seq = "CGAU"

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    assert transcribe(test_seq) == transcribe_seq   
    with pytest.raises(ValueError):
        transcribe(wrong_seq)
    


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert reverse_transcribe(test_seq) == reverse_transcribe_seq
    with pytest.raises(ValueError):
        reverse_transcribe(wrong_seq)
    