import pytest

@pytest.fixture
def greet():
    print("hello world")
    yield
    print("byyy")

def test_bye(greet):
    print("gm")

def test_by():
    print("hh")