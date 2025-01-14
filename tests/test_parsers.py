# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.
    
    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    # Good Fasta
    good_fasta_records = list(FastaParser("tests/good.fa")) # Convert into a list of tuples, and assert as opposed to for looping through records
    assert good_fasta_records == [("seq0", "TGATTG"),
                                  ("seq1", "TCCGCC")]

    # Bad Fasta
    bad_fasta = FastaParser("tests/bad.fa")
    with pytest.raises(ValueError):
        list(bad_fasta)

    # Empty Fasta
    blank_fasta = FastaParser("tests/blank.fa")
    with pytest.raises(ValueError):
        list(blank_fasta)


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    good_fastq_records = list(FastaParser("tests/good.fq")) # Convert into a list of tuples, and assert as opposed to for looping through records
    assert good_fastq_records[0][0] == None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    good_fastq_records = list(FastqParser("tests/good.fq")) 
    assert good_fastq_records == [("seq0","TGTGGT","*540($"),
                                 ("seq1","CCCCGG","'(<#/0")] 
    
    bad_fastq = FastqParser("tests/bad.fq")
    with pytest.raises(ValueError):
        list(bad_fastq)

    # Empty Fasta
    blank_fastq = FastqParser("tests/blank.fq")
    with pytest.raises(ValueError):
        list(blank_fastq)



def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    good_fasta_records = list(FastqParser("tests/good.fa")) # Convert into a list of tuples, and assert as opposed to for looping through records
    assert good_fasta_records[0][0] == None
    