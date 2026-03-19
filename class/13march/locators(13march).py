from time import sleep

from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

#launching a browser
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(3)

# id locator and entering value in demoqa
# element=driver.find_element(By.ID, "userName")

# element.send_keys("Akshita")
# driver.find_element(By.ID, "userEmail").send_keys("akshita@gmail.com")
# driver.find_element(By.ID, "currentAddress").send_keys("jaipur")
# driver.find_element(By.ID, "permanentAddress").send_keys("jaipur")
# driver.find_element(By.ID, "submit").click()
# sleep(5)

# task 1
# to search for shirts in AMAZON
# driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=279977868388654900&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061786&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
# driver.maximize_window()
# sleep(2)
# element=driver.find_element(By.ID , "twotabsearchtextbox")
# element.send_keys("shirt")
# driver.find_element(By.ID, "nav-search-submit-button").click()
# sleep(2)

# name locator
# driver.get("https://www.amazon.in")
#
# search_box = driver.find_element(By.NAME, "site-search")
# search_box.send_keys("laptop")
# sleep(3)
# driver.close()



# class locator
# driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=279977868388654900&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061786&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("shirt")
# driver.find_element(By.ID, "nav-search-submit-button").click()

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()

# sleep(2)
#Compound class are classes that are nested inside other classes. The compound class name should be replaced with '.'.
# driver.find_element(By.CLASS_NAME,"mr-sm-2.form-control").send_keys("Akshita")
# driver.find_element(By.CLASS_NAME,"form-control").send_keys("Jaipur")
# driver.find_element(By.ID, "submit").click()
# sleep(5)
# driver.close()


# tag name locator
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.TAG_NAME ,"input").send_keys("Akshita")
# driver.find_element(By.TAG_NAME ,"textarea").send_keys("Jaipur")
# driver.find_element(By.ID, "submit").click()
# sleep(5)
# driver.close()


# link text
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# sleep(3)
# driver.find_element(By.LINK_TEXT,'Toys & Games').click()
# sleep(2)
# driver.close()



# partial link
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(3)
# driver.find_element(By.PARTIAL_LINK_TEXT,'Home').click()
# sleep(2)
# driver.close()



# css
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(3)
# driver.find_element(By.CSS_SELECTOR ,'input[placeholder="Search Amazon.in"]').send_keys("laptop")