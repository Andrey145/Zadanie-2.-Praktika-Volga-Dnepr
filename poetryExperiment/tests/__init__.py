import pytest
from poetryExperiment import extract_by_mask

def test1():
	result = extract_by_mask("0b110011", "0xff")
	assert result == "0b110011"

def test2():
	result = extract_by_mask("0b111001", "0b1100")
	assert result == "0b10"