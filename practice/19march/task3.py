from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
sleep(2)
driver.find_element(By.LINK_TEXT , "Register").click()
driver.find_element(By.ID , "gender-female").click()
driver.find_element(By.ID , "FirstName").send_keys("Akshita")
driver.find_element(By.ID , "LastName").send_keys("Agarwal")
driver.find_element(By.ID , "Email").send_keys("akshita@gmail.com")
driver.find_element(By.ID , "Password").send_keys("abcd123@1")
driver.find_element(By.ID , "ConfirmPassword").send_keys("abcd123@1")
driver.find_element(By.ID , "register-button").click()
driver.close()
