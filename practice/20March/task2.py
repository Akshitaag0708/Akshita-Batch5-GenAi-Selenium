from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,"sc-dBfaGr.dyyfrm").send_keys("Pizza")
driver.find_element(By.CLASS_NAME,"sc-dBfaGr.dyyfrm").click()
sleep(2)
list = driver.find_elements(By.CLASS_NAME,"sc-glUWqk.GrjUP")
for i in list:
    print(i.text)
list[2].click()
driver.close()