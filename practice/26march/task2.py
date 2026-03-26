from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import os
import time
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get('https://www.lenskart.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT , "EYEGLASSES").click()
assert "https://www.lenskart.com/eyeglasses.html" == driver.current_url
driver.find_element(By.XPATH,"//div[@class='sc-dbae65e7-0 eNvqPZ']//select[1]").click()
sel=driver.find_element(By.XPATH,"//div[@class='sc-dbae65e7-0 eNvqPZ']//select[1]")
s=Select(sel)
s.select_by_visible_text("Most Viewed")
folder=os.path.join(os.getcwd() , "lenskart")
os.makedirs(folder,exist_ok=True)
timestamp=time.strftime("%Y%m%d%H%M%S")
driver.save_screenshot(f'{folder}/screenshot_{timestamp}.png')
sleep(2)
driver.quit()
