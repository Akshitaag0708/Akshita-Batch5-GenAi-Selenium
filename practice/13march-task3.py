'''
Question 3 : Using ID and PARTIAL LINK TEXT
--> Open Amazon
--> Search for Mobiles (use ID)
--> Click on any 1 mobile (use PARTIAL LINK TEXT)
'''


from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID ,'twotabsearchtextbox').send_keys("mobiles")
sleep(3)
driver.find_element(By.ID ,'nav-search-submit-button').click()
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT ,'iPhone 16 Plus').click()
sleep(3)
driver.quit()