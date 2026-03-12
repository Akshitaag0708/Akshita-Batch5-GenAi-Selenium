'''
write a selenium script to open a website and print page title

'''

from time import sleep
from selenium.webdriver import Chrome
driver = Chrome()
driver.get("https://www.google.com")
sleep(5)
print(driver.title)
