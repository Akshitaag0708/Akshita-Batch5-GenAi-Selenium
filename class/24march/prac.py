from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

o = ChromeOptions()
o.add_experimental_option("detach", True)
# driver = Chrome(options=o)
# driver.get("file:///C:/Users/hp/Desktop/selenium/index.html")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID,"mainInput").send_keys("Hello World")

# switching frames using index

# driver.switch_to.frame(0)                     #its index is 0 bcz it is first frame of page
# driver.find_element(By.ID,"frame1Input").send_keys("Hello ")
# driver.switch_to.frame(1)
# driver.find_element(By.ID,"frame2Input").send_keys("Hi")

#switching frame using name

# driver.switch_to.frame("frame1")
# driver.find_element(By.ID,"frame1Input").send_keys("Hello ")
# driver.switch_to.frame("frame2")
# driver.find_element(By.ID,"frame2Input").send_keys("Hi")


# switching frame using id

# driver.switch_to.frame("frameone")
# driver.find_element(By.ID,"frame1Input").send_keys("Hello ")
# driver.switch_to.frame("frametwo")
# driver.find_element(By.ID,"frame2Input").send_keys("Hi")

# switching using webelements

# frame1=driver.find_element(By.ID,"frameone")
# driver.switch_to.frame(frame1)
# driver.find_element(By.ID,"frame1Input").send_keys("Hello ")
# frame2=driver.find_element(By.ID,"frametwo")
# driver.switch_to.frame(frame2)
# driver.find_element(By.ID,"frame2Input").send_keys("Hi")

# ----------------------------------------------------------------------------------------------------
# switch from child to parent

# driver.switch_to.frame("frame1")
# driver.find_element(By.ID,"frame1Input").send_keys("Hello ")
# driver.switch_to.frame("frame2")
# driver.find_element(By.ID,"frame2Input").send_keys("Hi")
# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"frame1Input").clear()
# driver.find_element(By.ID,"frame1Input").send_keys("Back from frame 2")
#
# driver.switch_to.frame("frame2")
# driver.switch_to.default_content()
# driver.find_element(By.ID,"mainInput").clear()
# driver.find_element(By.ID,"mainInput").send_keys("direct from frame 2")

# -----------------------------------------------------------------------------------------------------

# Alerts and popups
#
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()
# sleep(2)
# alert=driver.switch_to.alert
# alert.accept()

# driver.find_element(By.XPATH,"//button[text()='Confirmation Alert']").click()
# sleep(2)
# alert=driver.switch_to.alert
# alert.accept()                    #to accept means to click on ok
# alert.dismiss()                   #to reject means to click on cancel


# driver.find_element(By.XPATH , "//button[text()='Prompt Alert']").click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys("John")
# sleep(2)
# alert.accept()

# ---------------------------------------------------------------------------------------------------------------
# to upload and

# driver.get("https://demoqa.com/upload-download")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT , "Download").click()
# driver.find_element(By.ID , "uploadFile").send_keys(r"C:\Users\hp\Downloads\2.png")


# -----------------------------------------------------------------------------------------------------------------

# driver.get("https://www.python.org/")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT , "Downloads").click()
# driver.find_element(By.LINK_TEXT , "Python 3.14.3").click()          # this will not works for downloading saying safe browsing is off
# so we need to add safe browsing from ChromeOptions

# o.add_experimental_option("prefs",{"safebrowsing.enabled":True})
# driver = Chrome(options=o)
# driver.get("https://www.python.org/")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT , "Downloads").click()
# sleep(2)
# driver.find_element(By.LINK_TEXT , "Python 3.14.3").click()          # this will start downloading as we have enabled the safe browsing
# --------------------------------------------------------------------------------------------------------------------

# o.add_argument("--disable-notifications")
# driver = Chrome(options=o)     #to disable notification we can also use ChromeOption
# driver.get("https://www.easemytrip.com/")
# driver.maximize_window()
# sleep(10)

# -----------------------------------------------------------------------------------------------------------------------------------

o.add_argument("--disable-notifications")
driver = Chrome(options=o)
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.XPATH,"//span[@class='ng-tns-c69-9 ui-calendar']").click()
# driver.find_element(By.XPATH,"//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9']").click()
# driver.find_element(By.XPATH,"(//a[@class='ui-state-default ng-tns-c69-9 ng-star-inserted'])[3]").click()

# ----------------------------------------------------------------------------------------------------------------------------------------

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"dateOfBirthInput").click()
month=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
mon=Select(month)
mon.select_by_visible_text("August")
year=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
yr=Select(year)
yr.select_by_visible_text("2003")
driver.find_element(By.XPATH,"//div[@class='react-datepicker__day react-datepicker__day--007']").click()



sleep(2)
# driver.close()
