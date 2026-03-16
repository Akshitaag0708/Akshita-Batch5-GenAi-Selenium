'''task1
open amazon
search for mobile
click on search icon
use mobile name and fetch its price
'''

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("mobiles")
driver.find_element(By.ID, 'nav-search-submit-button').click()
driver.find_element(By.PARTIAL_LINK_TEXT , "Samsung Galaxy M07 Mobile").click()
print(driver.find_element(By.XPATH,'(//span[@class="a-price-symbol"])[5]/..//span[2]').text)
# sleep(2)
# driver.quit()



