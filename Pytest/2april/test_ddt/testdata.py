import pytest
import sheet2

from selenium.webdriver.common.by import By


data=sheet2.get_test_data()

@pytest.mark.parametrize("username, password" ,data)
def test_login(setup, username, password):
    driver = setup

    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)

    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    driver.find_element(By.ID, "login-button").click()