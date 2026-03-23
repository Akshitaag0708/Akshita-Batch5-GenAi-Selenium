from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
hover=driver.find_element(By.XPATH , "//button[text()='Point Me']")
actions = ActionChains(driver)
actions.move_to_element(hover).perform()
sleep(2)
dc=driver.find_element(By.XPATH , "//button[text()='Copy Text']")
actions.double_click(dc).perform()
sleep(2)
drag=driver.find_element(By.XPATH , "//p[contains(text(),'Drag me to')]")
drop=driver.find_element(By.XPATH , "//p[text()='Drop here']")
actions.drag_and_drop(drag,drop).perform()
sleep(2)
driver.close()