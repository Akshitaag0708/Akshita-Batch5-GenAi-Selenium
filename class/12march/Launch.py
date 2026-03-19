# 12 march


# 1.launch the browser
# from time import sleep
#
# from selenium.webdriver import Chrome
# driver =Chrome()
# sleep(5)


# from time import sleep
# from selenium.webdriver import Edge
# driver=Edge()
# sleep(7)

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)

# 2. open a web page
# driver.get("https://www.google.com")

#  maximize the screen of browser
# driver.maximize_window()

# minimize the window
# driver.minimize_window()

# fullscreen the window
# driver.fullscreen_window()


# task1 : to launch amzon website in max min and fullscreen
# driver.get("https://www.amazon.com")
# sleep(5)
# driver.maximize_window()
# sleep(2)
# driver.minimize_window()
# sleep(3)
# driver.fullscreen_window()
# to do all 3 task together we will use sleep() between all 3 as selenium is very fast and browser is slow so to match both we use sleep and wake

# t = driver.title       # we fetch title to perform validation
# print(t)
# print(driver.current_url)    # sometimes title are same for multiple sites so we use current_url for verification
# print(driver.page_source)     # it is not used much , gives html file

# task2 :
# driver.get("https://demoqa.com/")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)

# print(driver.name)     # print the name of the browser we are using

# sleep(5)
# driver.close()      # suppose we open more tab manually in browser then this will close the url tab only as the sleep time completes

# driver.quit()        # suppose we open more tab manually in browser then this will close all tabs including url page as the sleep time completes

# whenever we launch we have 3 options back , next and refresh
# sleep(3)
# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()


# task3:  open wikipidea , refresh , fetch the title  , open amazon , fetch title, go back , go close
# driver.get("https://www.wikipedia.org/")
# sleep(5)
# driver.refresh()
# sleep(5)
# print(driver.title)
# driver.get("https://www.amazon.com/")
# sleep(5)
# driver.refresh()
# print(driver.title)
# sleep(5)
# driver.back()
# sleep(5)
# driver.close()
