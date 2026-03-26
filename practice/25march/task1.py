from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
import time

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("ans")
driver.find_element(By.XPATH , "//input[@id='login-button']").click()

# try:
#     expected="https://www.saucedemo.com/inventory.html"
#     assert expected == driver.current_url
#     print("Login Successful")
# except Exception as e:
#     timestamp = time.strftime("%Y%m%d%H%M%S")
#     driver.save_screenshot(f'{timestamp}.png')

expected="https://www.saucedemo.com/inventory.html"
if expected == driver.current_url:
    print("Login Successful")
else:
    timestamp = time.strftime("%Y%m%d%H%M%S")
    driver.save_screenshot(f'{timestamp}.png')
driver.quit()