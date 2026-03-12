'''
task2:
write a selenium script to open a website and print current url
'''


from time import sleep
from selenium.webdriver import Chrome
driver=Chrome()
driver.get("https://www.google.com")
sleep(3)
print(driver.current_url)
