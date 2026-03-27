from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
def test_register():
    driver.find_element(By.LINK_TEXT , "Register").click()
def test_gender():
    driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
def test_fname():
    driver.find_element(By.XPATH , "//input[@id='FirstName']").send_keys("John")
def test_lname():
    driver.find_element(By.XPATH , "//input[@id='LastName']").send_keys("Doe")
def test_email():
    driver.find_element(By.XPATH , "//input[@id='Email']").send_keys("akshit@gmail.com")
def test_pass():
    driver.find_element(By.XPATH , "//input[@id='Password']").send_keys("123456")

def test_confirm():
    # pss =driver.find_element(By.XPATH , "//input[@id='Password']").send_keys(Keys.CONTROL,'a')
    # pss = driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(Keys.CONTROL, 'c')
    # driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys(Keys.CONTROL , 'v')
    driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("123456")
def test_submit():
    driver.find_element(By.XPATH, "//input[@id='register-button']").click()
def test_close():
    sleep(2)
    driver.quit()