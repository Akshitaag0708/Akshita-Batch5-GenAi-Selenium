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
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# links=driver.find_elements(By.XPATH, "//div[@class='nav-div']//a")
# print(len(links))
# for link in links:
#     print(link.get_attribute("href"))
#

# -----------------------------------------------------------------------------------------------
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# x=driver.find_element(By.XPATH, "//div[@aria-label='Log in']")
# print("displayed: ",x.is_displayed())
# print("enabled : ",x.is_enabled())
#
# btn=driver.find_element(By.XPATH , "//input[@type='submit']")     #hidden element
# print("displayed: ",btn.is_displayed())
# print("enabled : ",btn.is_enabled())


# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# driver.maximize_window()
# driver.implicitly_wait(10)
# x=driver.find_element(By.XPATH, "//button[@class='submitbtn resman-btn-primary resman-btn-regular resman-btn-disabled']")
# print("displayed :",x.is_displayed())
# print("enabled : ",x.is_enabled())

# using headless

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# driver.implicitly_wait(10)
# x=driver.find_element(By.XPATH , "//input[@type='checkbox'][1]")
# x.click()
# y=driver.find_element(By.XPATH , "//input[@type='checkbox'][2]")
# y.click()
# print(x.is_selected)
# print(y.is_selected)



# --------------------------------------------------------------------------------------------------
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.find_element(By.ID, "firstName").send_keys("Akshita")
driver.find_element(By.ID, "lastName").send_keys("Agarwal")
driver.find_element(By.ID, "userEmail").send_keys("abc@abc.com")
driver.find_element(By.XPATH, '//input[@id="gender-radio-1"]').click()
driver.find_element(By.XPATH, '//input[@id="userNumber"]').send_keys("6378074820")

driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
mon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//option[@value="7"]')))
mon.click()
driver.find_element(By.XPATH, '//input[@id="dateOfBirthInput"]').click()
dat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[. = "15"]')))
dat.click()
driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[5]').click()
driver.find_element(By.XPATH, '(//div[@class="form-check form-check-inline"])[6]').click()
driver.find_element(By.XPATH, '//input[@id="uploadPicture"]').send_keys(r"C:\Users\hp\Downloads\5.png")
driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]').send_keys("jaipur")
# driver.find_element(By.XPATH, '//div[@class="css-1wy0on6"]').click()
# driver.find_element(By.XPATH, '//input[@id="submit"]').click()
driver.find_element(By.XPATH, '//button[@id="submit"]').click()
driver.quit()