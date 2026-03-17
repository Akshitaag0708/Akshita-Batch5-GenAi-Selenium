from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[@id = 'addNewRecordButton']").click()
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Akshita")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Agarwal")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH, "//input[@id='age']").send_keys("22")
driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("58000")
driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Q&T")
driver.find_element(By.XPATH, "//button[@id = 'submit']").click()

s = driver.find_element(By.XPATH, "//td[text() = 'Akshita']/..//td[5]")
print("The Salary is:",s.text)

driver.quit()