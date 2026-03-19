from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.amazon.in/s?k=watch&crid=33SQ15BC0B506&sprefix=watch%2Caps%2C357&ref=nb_sb_noss_2")
driver.maximize_window()
driver.implicitly_wait(10)
links=driver.find_elements(By.TAG_NAME,'img')   # this will include sponsored pdt and add image also
print(len(links))
only=driver.find_elements(By.XPATH , '//div[@class="a-section a-spacing-base desktop-grid-content-view"]//img')#this will not include sponsored pdt
print(len(only))
only[4].click()
driver.quit()