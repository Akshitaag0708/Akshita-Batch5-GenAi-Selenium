from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com/")
    yield driver
    sleep(5)
    driver.quit()


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),("locked_out_user", "secret_sauce"),("problem_user", "secret_sauce")])
def test_login(setup, username, password):
    driver = setup

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()


