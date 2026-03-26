from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('watch')
driver.find_element(By.XPATH, "//div[@id='sac-suggestion-row-4-cell-1']").click()
driver.find_element(By.XPATH,"//span[@class='a-button-text a-declarative']").click()
driver.find_element(By.LINK_TEXT,"Newest Arrivals").click()
driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[3]").click()
print(driver.find_element(By.XPATH,"(//div[@data-cy='asin-faceout-container'])[1]//div[2]//div[1]").text , "= Rs.",driver.find_element(By.XPATH,"(//span[@class='a-price-whole'])[1]").text)
sleep(3)
driver.close()
