'''
Question 1 : Using ID
--> Open Amazon
--> Click on Update Location
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
driver.find_element(By.ID,"glow-ingress-line2").click()
sleep(3)
driver.close()
