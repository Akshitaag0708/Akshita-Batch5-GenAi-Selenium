from time import sleep

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_example():
    assert 5<6
#
@pytest.mark.skipif(0 < 1, reason="Condition is True")
def test_ex():
    assert True


@pytest.mark.parametrize("a,b", [(1,2), (3,4), (5,6)])
def test_add(a, b):
    assert a + b > 0



# from selenium.webdriver import Chrome,ChromeOptions
# o=ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://www.saucedemo.com/")

# @pytest.mark.parametrize("a,b", [("standard_user","secret_sauce")])
# def test_user(a,b):
#     driver.find_element(By.ID , "user-name").send_keys(a)
#     driver.find_element(By.ID, "password").send_keys(b)
#     driver.find_element(By.ID, "login-button").click()



