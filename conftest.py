import pytest
from solution import ReversePolishNotation


@pytest.fixture(name="solution")
def fixture_solution():
    solution = ReversePolishNotation()

    return solution
