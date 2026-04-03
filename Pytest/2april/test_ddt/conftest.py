import pytest
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
@pytest.fixture
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com/")
    yield driver
    sleep(5)
    driver.quit()

# in conftest we keep code that does not change