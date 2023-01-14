from src.assignment_letter import MappingTable
import pytest

@pytest.fixture
def assignmentTable():
    table = MappingTable()
    return table

@pytest.mark.getLetter
def test_getLetter(assignmentTable):
    assert "Z" == assignmentTable.getLetter("45301872")

@pytest.mark.returnRest
def test_assignmentLetter(assignmentTable):
    assert 14 == assignmentTable.assignmentLetter("45301872")
