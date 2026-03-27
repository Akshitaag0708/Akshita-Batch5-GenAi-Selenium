from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT , "Apparel & Shoes").click()
dd1=driver.find_element(By.XPATH, "//select[@id='products-orderby']")
choice1=Select(dd1)
choice1.select_by_index(2)
dd2=driver.find_element(By.XPATH, "//select[@id='products-pagesize']")
choice2=Select(dd2)
choice2.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?orderby=6&pagesize=4")
dd3=driver.find_element(By.XPATH, "//select[@id='products-viewmode']")
choice3=Select(dd3)
choice3.select_by_visible_text("List")
sleep(2)
driver.close()