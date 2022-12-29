from src.assignment_letter import *
import pytest

@pytest.fixture
def assignmentTable():
    table = MappingTable()
    return table

@pytest.mark.assignLetter
def test_letterAssignment(assignmentTable):
    assert "Z" == assignmentTable.getLetter("45301872")

