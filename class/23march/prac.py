from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID , "twotabsearchtextbox").send_keys("shoes")
# driver.find_element(By.ID, "nav-search-submit-button").click()

# ---------------------------------------------------------------------------------------------------
#   enter keyword

# elm=driver.find_element(By.ID , "twotabsearchtextbox")
# elm.send_keys("shoes")
# elm.send_keys(Keys.ENTER)  # instead of click we can use keys action

# driver.find_element(By.ID , "twotabsearchtextbox").send_keys("shoes")
# driver.find_element(By.ID , "twotabsearchtextbox").send_keys(Keys.ENTER)

# -----------------------------------------------------------------------------------------------------
# copy-paste

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID,"currentAddress").send_keys("jaipur")
# a=driver.find_element(By.ID,"currentAddress").send_keys(Keys.CONTROL,'a')
# a=driver.find_element(By.ID,"currentAddress").send_keys(Keys.CONTROL,'c')
# driver.find_element(By.ID,"permanentAddress").send_keys(Keys.CONTROL , 'v')

# -----------------------------------------------------------------------------------------------------
# Action Chain

# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
# sleep(2)
# # driver.find_elements(By.ID,"doubleClickBtn").click()       #this will give error
# # driver.find_elements(By.ID,"rightClickBtn").click()        #this will give error
# # driver.find_element(By.XPATH , "//button[text()='Click Me']").click()
#
# single_click=driver.find_element(By.XPATH , "//button[text()='Click Me']")
# actions = ActionChains(driver)
# actions.click(single_click).perform()
#
# double_click=driver.find_element(By.ID , "doubleClickBtn")
# # actions.click(double_click).click(double_click).perform()       # this will perform double click
# actions.double_click(double_click).perform()                  # this will also perform double click
#
# right_click=driver.find_element(By.ID,"rightClickBtn")
# actions.context_click(right_click).perform()

# ---------------------------------------------------------------------------------------------------------------------
# scroll
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# elt=driver.find_element(By.XPATH,"//span[text()='Best Sellers in Home & Kitchen']")
# #
# actions = ActionChains(driver)
# actions.move_to_element(elt).perform()
#
# actions.scroll_by_amount(0,400).perform()
#
# origin=ScrollOrigin.from_element(elt)
# actions.scroll_from_origin(origin,0,200).perform()

# actions.move_to_element(elt).perform()


# ------------------------------------------------------------------------------------------------------------------------

# click and hold

# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# driver.maximize_window()
# sleep(2)
# elt=driver.find_element(By.ID,"password")
# sleep(2)
# elt.send_keys("akshita")
# actions = ActionChains(driver)
# sleep(10)
# eye=driver.find_element(By.XPATH , "//img[@class='ng-star-inserted']")
# # actions.click_and_hold(eye).perform()
#
# actions.click_and_hold(eye).pause(10).release().perform()      #after 15 sec release will release the click and hold


# -------------------------------------------------------------------------------------------------------------------

# drag and drop
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# sleep(2)
# drag=driver.find_element(By.XPATH,"//div[text()='Drag Me']")
# drop=driver.find_element(By.XPATH,"//p[text()='Drop Here']")
# actions = ActionChains(driver)
# actions.drag_and_drop(drag,drop).perform()

# ------------------------------------------------------------------------------------------------------------------------

# only droppable
# driver.get("https://demoqa.com/dragabble")
# driver.maximize_window()
# sleep(2)
# drag=driver.find_element(By.XPATH,"//div[text()='Drag me']")
# actions = ActionChains(driver)
# actions.drag_and_drop_by_offset(drag , 0,300).perform()

# -------------------------------------------------------------------------------------------------------------------
# here action chain is completed
# -----------------------------------------------------------------------------------------------------------------------------
# switching window

# current_window_handle
# driver.get("https://www.google.com/")
# driver.maximize_window()
# sleep(5)
# print(driver.current_window_handle)
# print(driver.title)
# # driver.switch_to.window(driver.window_handles[1])
# # print(driver.window_handles)
# # print(driver.current_window_handle)
# driver.switch_to_new_window()
# driver.get("https://www.amazon.in")
# # driver.switch_to.window(driver.window_handles[1])
# print(driver.current_window_handle)
# print(driver.title)
#

sleep(5)

# driver.close()


# --------------------------------------------------------------------------------------------------------------------------------
