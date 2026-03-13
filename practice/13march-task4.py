'''
Question 4 : Using LINK TEXT and PARTIAL LINK TEXT
--> Open https://www.selenium.dev/
--> Click on 'Downloads'
--> Click on 'Other Languages Exist'
--> Click on 'Register Now'
--> Fetch Page titl
'''



from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT , 'Downloads').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT , 'other').click()
sleep(2)
driver.find_element(By.LINK_TEXT , 'Register now!').click()
sleep(2)
print(driver.title)
driver.quit()

