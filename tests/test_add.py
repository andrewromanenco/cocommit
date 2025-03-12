import pytest
from cocommit.add import add

def test_add():
    assert add(1, 2) == 3