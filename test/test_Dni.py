from src.Dni import *
import pytest

@pytest.mark.checkDni
def test_searchLetterDNI():
    assert False == Dni.checkDni("45312")
    assert False == Dni.checkDni("4531239495834821")
    assert False == Dni.checkDni("45301RE2")
    assert False == Dni.checkDni("ªªªªª>>>")
    assert False == Dni.checkDni("        ")
    assert False == Dni.checkDni("1234Hola")
    assert True == Dni.checkDni("45301872")
    assert True == Dni.checkDni("06523123")






