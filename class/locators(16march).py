from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_argument("--headless")         #browser runs without opening a visible GUI window.
driver=Chrome(options=o)
# driver.get("https://demoqa.com/webtables")
# sleep(3)
#  locating dynamic element via parent

# print(driver.find_element(By.XPATH , "//td[text()='Gentry']/..//td[6]").text)     # to locate the dynamic element

# driver.get('https://the-internet.herokuapp.com/tables')
# print(driver.find_element(By.XPATH , "//td[text()='Bach']/..//td[4]").text)
# locating dynamic parent via sibling

# locating following sibling :
# print(driver.find_element(By.XPATH , "//td[text()='Bach']/following-sibling::td[2]").text)

# locating preceding sibling
# print(driver.find_element(By.XPATH , "//td[text()='Frank']/preceding-sibling::td[1]").text)


# task
# driver.get("https://www.amazon.in/")
# sleep(3)
# driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("mobiles")
# driver.find_element(By.ID, 'nav-search-submit-button').click()
# driver.find_element(By.PARTIAL_LINK_TEXT , "Samsung Galaxy M07 Mobile").click()
# print(driver.find_element(By.XPATH,'(//span[text()="₹"])[5]//following-sibling::span').text)



sleep(2)
driver.quit()




