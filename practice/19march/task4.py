from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH, '//input[@id="singleFileInput"]').send_keys(r"C:\Users\hp\Downloads\5.png")
# via multiple send_keys()
# driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(r"C:\Users\hp\Downloads\5.png")
# driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(r"C:\Users\hp\Downloads\6.png")
# via single send_keys
driver.find_element(By.XPATH, '//input[@id="multipleFilesInput"]').send_keys(r"C:\Users\hp\Downloads\5.png"+"\n"+r"C:\Users\hp\Downloads\6.png")