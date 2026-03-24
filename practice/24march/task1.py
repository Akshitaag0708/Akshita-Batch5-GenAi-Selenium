from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://x.com/?lang=en")
driver.maximize_window()
sleep(2)
frame1=driver.find_element(By.XPATH , "//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//span[.='Sign up with Google']").click()
sleep(2)
driver.close()