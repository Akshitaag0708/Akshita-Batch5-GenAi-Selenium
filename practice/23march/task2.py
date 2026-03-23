from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.nike.in/")
driver.maximize_window()
sleep(2)
kids=driver.find_element(By.XPATH , "//span[text()='Kids']")
actions = ActionChains(driver)
actions.move_to_element(kids).pause(2).click(kids).perform()
driver.switch_to.window(driver.window_handles[1])
shop=driver.find_element(By.XPATH ,"//a[text()='Shop']")
actions.scroll_to_element(shop).pause(2).click(shop).perform()
shoe=driver.find_element(By.XPATH, "//div[@id='aria-label-24800718-1']")
actions.scroll_to_element(shoe).pause(2).click(shoe).perform()
driver.switch_to.window(driver.window_handles[2])
size=driver.find_element(By.XPATH , "//label[text()='UK 4']")
actions.click(size).perform()
cart=driver.find_element(By.XPATH , "//button[text()='Add to Bag']")
actions.click(cart).perform()

sleep(3)
driver.quit()
