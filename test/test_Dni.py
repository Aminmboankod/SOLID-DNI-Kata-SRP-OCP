from src.Dni import Dni
import pytest

@pytest.fixture
def objectDni():
    dni = Dni()
    return dni

@pytest.mark.checkDni
def test_checkDni():
    assert False == Dni.checkDni("45312")
    assert False == Dni.checkDni("4531239495834821")
    assert False == Dni.checkDni("45301RE2")
    assert False == Dni.checkDni("ªªªªª>>>")
    assert False == Dni.checkDni("        ")
    assert False == Dni.checkDni("1234Hola")
    assert True == Dni.checkDni("45301872")
    assert True == Dni.checkDni("06523123")

@pytest.mark.completeDni
def test_completeDni(objectDni):
    assert "45301872Z" == objectDni.completeDni("45301872")
    assert "43211433E" == objectDni.completeDni("43211433")
    assert "43211434T" == objectDni.completeDni("43211434")




