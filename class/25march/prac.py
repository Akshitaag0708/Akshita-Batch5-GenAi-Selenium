from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.page import Screenshot

o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
# driver.get("https://www.google.com")
# driver.maximize_window()
# sleep(2)
# print(driver.title)

# assert : by using it will will check if title is expected or not
# expected='Google'
# actual=driver.title
# #  we provide assert expected_test_result == actual test result
# assert expected == actual    # if this fails then further execution will stop and a assertion exception will come

# assert 'chrome' == actual     # this will give AssertionError as title mismatch and the further execution will stop

# driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys('Selenium')

# --------------------------------------------------------------------------------------------------------------------

# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT,"Bestsellers").click()
# expected="Amazon.in Bestsellers: The most popular items on Amazon"
# actual=driver.title
# assert expected == actual

# --------------------------------------------------------------------------------------------------------------------

# Screenshot
driver.get("https://www.google.com")
driver.maximize_window()
sleep(2)
# full screen screenshot
#  we takes screenshot to show test failure proof
# driver.save_screenshot('screenshot1.png')      # we get this screenshot in directory whwre we have file

#  if u want to store in differ location

import os  # if u want to store in differ location
folder=os.path.join(os.getcwd() , "screenshot")    # now this folder is created now we check if it exists or not
os.makedirs(folder,exist_ok=True)                   # this will check folder existance
#
# driver.save_screenshot(f'{folder}/screenshot.png')

# screenshot of a particular element
# ele=driver.find_element(By.XPATH,"//textarea[@title='Search']")
# ele.screenshot(f'{folder}/search.png')

#  based on time also we can store screenshot
#  we need to import time
# multiple screenshot will not have same name
# ele2=driver.find_element(By.XPATH,"//div[@id='LS8OJ']")
import time
timestamp=time.strftime("%Y%m%d%H%M%S")
# ele2.screenshot(f'{folder}/{timestamp}.png')

ele3=driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']")
ele3.screenshot(f'{folder}/screenshot_ele3_{timestamp}.png')



sleep(4)
driver.close()