from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

#launching a browser
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
# driver.get("https://demoqa.com/text-box")
# sleep(2)

#  class using , and id using # in CSS Selector
# driver.find_element(By.CSS_SELECTOR ,".mr-sm-2.form-control").send_keys("Akshita")
# sleep(2)
# driver.find_element(By.CSS_SELECTOR , "#currentAddress").send_keys("Jaipur")
# sleep(2)

# XPATH

# syntax : //tag_name[@attribute="value"]

#   XPATH USING attribute
# driver.find_element(By.XPATH ,'//input[@placeholder="Full Name"]').send_keys("Akshita")
# sleep(2)
# driver.find_element(By.XPATH ,'//input[@id="userEmail"]').send_keys("Akshita@gmail.com")
# sleep(2)
# driver.find_element(By.XPATH ,'//textarea[@placeholder="Current Address"]').send_keys("Jaipur")
# sleep(2)
# driver.find_element(By.XPATH ,'//textarea[@id="permanentAddress"]').send_keys("Jaipur")
# sleep(2)
# driver.find_element(By.XPATH ,'//button[@id="submit"]').click()
# sleep(2)


# XPATH using text
# driver.find_element(By.XPATH ,'//input[@placeholder="Full Name"]').send_keys("Akshita")
# sleep(2)
# driver.find_element(By.XPATH ,'//input[@id="userEmail"]').send_keys("Akshita@gmail.com")
# sleep(2)
# driver.find_element(By.XPATH ,'//textarea[@placeholder="Current Address"]').send_keys("Jaipur")
# sleep(2)
# driver.find_element(By.XPATH ,'//textarea[@id="permanentAddress"]').send_keys("Jaipur")
# sleep(2)
# # driver.find_element(By.XPATH ,'//button[text()="Submit"]').click()      # use of xpath with text here
# # sleep(2)
#  # instead of text() we can also use .
# driver.find_element(By.XPATH ,'//button[.="Submit"]').click()      # use of xpath with text here
# sleep(2)

# driver.get("https://www.amazon.in/")
# sleep(2)

# with contains text
# driver.find_element(By.XPATH, '//input[@placeholder="Full Name"]').send_keys("Akshita")
# sleep(2)
# driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys("Akshita@gmail.com")
# sleep(2)
# driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]').send_keys("Jaipur")
# sleep(2)
# driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys("Jaipur")
# sleep(2)
# driver.find_element(By.XPATH, '//button[contains(text(),"Submit")]').click()   # XPath with text()
# sleep(2)

# xpath with contains attribute
driver.get("https://www.amazon.in/")
sleep(2)
# driver.maximize_window()
# driver.find_element(By.XPATH, "//a[contains(@href,'amazon-global-selling')]").click()  #here we pass a part of href
# sleep(2)

# driver.find_element(By.XPATH , "//a[contains(text(),'Global Selling')]").click()      #here we passed a part of text
# sleep(2)
# driver.close()

