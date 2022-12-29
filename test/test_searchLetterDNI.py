from src.searchLetterDNI import *
import pytest

@pytest.mark.checkDni
def test_searchLetterDNI():
    assert "Número DNI incorrecto" == Dni.checkDni("45312")
    assert "Número DNI incorrecto" == Dni.checkDni("4531239495834821")
    assert "Número DNI incorrecto" == Dni.checkDni("45301RE2")
    assert "Número DNI incorrecto" == Dni.checkDni("ªªªªª>>>")
    assert "Número DNI incorrecto" == Dni.checkDni("        ")
    assert "Número DNI incorrecto" == Dni.checkDni("1234Hola")
    assert "Número DNI correcto" == Dni.checkDni("45301872")
    assert "Número DNI correcto" == Dni.checkDni("06523123")


# @pytest.mark.assignLetter
# def test_searchLetterDNI():
#     assert "Z" == Dni.checkLetter("45301872")

