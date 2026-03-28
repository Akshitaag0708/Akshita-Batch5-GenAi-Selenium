from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver=Chrome(options=o)
def test_open():
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
def test_click():
    driver.find_element(By.LINK_TEXT , "Apparel & Shoes").click()
def test_sort():
    sort1=driver.find_element(By.XPATH, "//select[@id='products-orderby']")
    ch1=Select(sort1)
    ch1.select_by_index(2)
def test_page():
    sort2=driver.find_element(By.XPATH, "//select[@id='products-pagesize']")
    ch2=Select(sort2)
    ch2.select_by_value("https://demowebshop.tricentis.com/apparel-shoes?orderby=6&pagesize=4")
def test_view():
    sort3=driver.find_element(By.XPATH, "//select[@id='products-viewmode']")
    ch3=Select(sort3)
    ch3.select_by_visible_text("List")
def test_close():
    sleep(2)
    driver.quit()
