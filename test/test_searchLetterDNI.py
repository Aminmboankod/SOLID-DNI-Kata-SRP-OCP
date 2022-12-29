from src.searchLetterDNI import *
import pytest

@pytest.mark.checkDni
def test_searchLetterDNI():
    assert "El número no es correcto" == Dni.checkNumDni("45312")
    assert "Número DNI correcto" == Dni.checkNumDni("45301872")

@pytest.mark.assignLetter
def test_searchLetterDNI():
    assert "Z" == Dni.checkLetter("45301872")

