from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(5)
driver.find_element(By.NAME , 'q').send_keys("washing machine")
driver.find_element(By.CLASS_NAME,'XFwMiH').click()
driver.find_element(By.PARTIAL_LINK_TEXT , '8 kg 5 Star Inverter Steam Technology,').click()
print(driver.find_element(By.XPATH,"//div[@class='hZ3P6w DeU9vF']/..//div").text)
sleep(2)
driver.quit()