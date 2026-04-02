import pytest

#  custom markers
def test_register():
    print("register successfully")
@pytest.mark.abc
def test_login():
    print("Login successfully")

@pytest.mark.apl
def test_logout():
    print("Logout successfully")




