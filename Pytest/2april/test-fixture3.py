import pytest
from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    sleep(5)
    driver.quit()

class Test_Demo:
    def test_register(self,setup):
        driver = setup
        driver.find_element(By.LINK_TEXT, "Register").click()

    def test_gender(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='gender-female']").click()

    def test_fname(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("John")

    def test_lname(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Doe")

    def test_email(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("akshit@gmail.com")

    def test_pass(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("123456")

    def test_confirm(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("123456")

    def test_submit(self,setup):
        driver = setup
        driver.find_element(By.XPATH, "//input[@id='register-button']").click()