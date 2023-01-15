from src.caculadoraDNI import CalculadoraDNI
import pytest

@pytest.fixture
def calculadoraDNI():
    table = CalculadoraDNI()
    return table

@pytest.mark.getLetter
def test_getLetter():

@pytest.mark.returnRest
def test_assignmentLetter(assignmentTable):
    assert 14 == assignmentTable.assignmentLetter("45301872")
