import pytest

from  ..main import plus

def test_one():
    assert 1==1
    # assert 1==2


def test_plus():
    assert plus(1,1) == 2
    assert plus(1,1) == 1
