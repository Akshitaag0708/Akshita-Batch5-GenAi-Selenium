from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Log in").click()
frame1 = driver.find_element(By.ID, "auth-login-ui")
driver.switch_to.frame(frame1)
frame2=driver.find_element(By.XPATH , "//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH, "//span[text()='Sign in with Google']").click()

sleep(5)
driver.quit()