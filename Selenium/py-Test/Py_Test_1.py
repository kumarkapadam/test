# pip install pytest

# pytest --version
import pytest


@pytest.mark.skipif()
def testLogin():
    print("login success")

def testLogoff():
    print("login success")

def testCalculation():
    assert 2+2 == 4

def add():
    assert 3+3 == 6


if __name__== "__main__":
    print("all success")