from src.logic.Dni import DNI
import pytest

@pytest.mark.checkDni
def test_verificarNIF():

    documento = DNI("", "45312", "")
    assert documento.verificarNIF() == False

    documento = DNI("", "4531239495834821", "")
    assert documento.verificarNIF() == False

    documento = DNI("", "45301RE2", "")
    assert documento.verificarNIF() == False

    documento = DNI("", "ªªªªª>>>", "")
    assert documento.verificarNIF() == False

    documento = DNI("", "        ", "")
    assert documento.verificarNIF() == False
    
    documento = DNI("", "45301872", "")
    assert documento.verificarNIF() == True

    documento = DNI("", "06523123", "")
    assert documento.verificarNIF() == True

@pytest.mark.completeDni
def test_dniCompleto():
    documento = DNI("","45301872", "")
    assert documento.dniCompleto() == "45301872Z"
    documento = DNI("", "43211433", "")
    assert documento.dniCompleto() == "43211433E"
    documento = DNI("", "43211434", "")
    assert documento.dniCompleto()== "43211434T"




