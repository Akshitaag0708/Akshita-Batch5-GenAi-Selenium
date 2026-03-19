from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

# driver.get("http://www.google.com")
# driver.maximize_window()
# driver.implicitly_wait(10)

# driver.find_element(By.TAG_NAME , "a").click()
# links=driver.find_elements(By.TAG_NAME , "a")
# print(links)
# for link in links:
#     print(link.text)
# print(len(links))

# ------------------------------------------------------------------------------------------

# links=driver.find_elements(By.TAG_NAME , "a")
# for link in links:
#     print(link.get_attribute("href"))

# emt=driver.find_element(By.XPATH , "//a[@class='gb_Z']")
# print(emt.get_attribute("aria-label"))

# --------------------------------------------------------------------------------------------
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)
links=driver.find_elements(By.XPATH, "//div[@class='nav-div']//a")
print(len(links))
for link in links:
    print(link.get_attribute("href"))