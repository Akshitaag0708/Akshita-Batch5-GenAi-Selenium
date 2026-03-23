from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

#launching a browser
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.maximize_window()
# # sleep(2)
# driver.find_element(By.XPATH , "//div[@id='start']//button").click()
# # sleep(6)
# driver.implicitly_wait(10)
# print(driver.find_element(By.ID,"finish").text)
# --------------------------------------------------------------------------------------------------------------------------------

#'''Implicit wait (implicitly_wait(10)) only waits for the element to appear in the DOM (presence), not for it to become visible.
# Because it exists, Selenium finds it immediately and returns an empty string, before the text actually loads.'''

# so we use explicit wait


# from time import sleep
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# # launching browser
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//div[@id='start']//button").click()
# # Explicit wait for visibility of text
# wait = WebDriverWait(driver, 10)
# text_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
#
# print(text_element.text)
# driver.quit()

# ---------------------------------------------------------------------------------------------------------------------

# open decathlon click on WinterReady and click on any object
# difference b/w sleep and implicit wait


# driver.get("https://www.decathlon.in/")
# driver.maximize_window()
# # sleep(2)
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//div[@class='py-2 flex flex-nowrap md:px-7 md:py-3 justify-around']//a[1]").click()
# # sleep(2)
# driver.find_element(By.XPATH,'//div[@class="py-2 flex flex-nowrap md:px-7 md:py-3 justify-around"]//a[1]').click()
# # sleep(2)
# driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
