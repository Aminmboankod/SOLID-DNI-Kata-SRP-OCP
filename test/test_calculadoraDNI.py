from src.accesoDatos.caculadoraDNI import TablaAsignacion
import pytest

@pytest.fixture
def calculadoraDNI():
    table = TablaAsignacion()
    return table

@pytest.mark.getLetter
def test_obtenerDigito(calculadoraDNI):
    assert "Z" == calculadoraDNI.obtenerDigito("45301872")

@pytest.mark.returnRest
def test_calcularResto(calculadoraDNI):
    assert 14 == calculadoraDNI.calcularResto("45301872")
