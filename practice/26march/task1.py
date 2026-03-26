import os
import time
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://in.pinterest.com/")
driver.maximize_window()
driver.implicitly_wait(10)
folder=os.path.join(os.getcwd() , "pinterest")
os.makedirs(folder,exist_ok=True)
timestamp=time.strftime("%Y%m%d%H%M%S")
driver.save_screenshot(f'{folder}/pinterest-ss-{timestamp}.png')
ele=driver.find_element(By.XPATH , "(//div[@class='ADXRXN gEQpi5'])[20]")
actions=ActionChains(driver)
actions.scroll_to_element(ele).perform()
ele.screenshot(f'{folder}/pinterest2-ss-{timestamp}.png')
sleep(2)
driver.close()