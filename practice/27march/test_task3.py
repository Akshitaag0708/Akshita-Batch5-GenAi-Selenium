from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options=o)
def test_open():
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
def test_scroll():
    ele=driver.find_element(By.LINK_TEXT,"Facebook")
    actions = ActionChains(driver)
    actions.scroll_to_element(ele).pause(2).click(ele).perform()
def test_switch():
    driver.switch_to.window(driver.window_handles[1])
def test_login():
    driver.find_element(By.XPATH,"//label[@class='x78zum5 xh8yej3']//div//descendant::input").send_keys("abcd@gmail.com")
    driver.find_element(By.XPATH,"(//label[@class='x78zum5 xh8yej3'])[2]//div//descendant::input").send_keys("abcd")
    driver.find_element(By.XPATH,"(//div[@class='x1c436fg'])[2]//descendant::div[1]").click()
def test_close():
    sleep(2)
    driver.quit()