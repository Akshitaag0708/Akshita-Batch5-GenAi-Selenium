import pytest

@pytest.mark.smoke
def test_smoke_1():
    assert 'hi' != 'Hello'

@pytest.mark.smoke
def test_smoke_2():
    assert "hello".upper() == "HELLO"


@pytest.mark.regression
def test_regression_1():
    l = ['apple', 'banana', 'litchi']
    assert 'apple' in l

@pytest.mark.regression
def test_regression_2():
    assert len([1, 2, 3]) == 3