from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
class DemoSeleniumLearning():
    def demo_browser_methods(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.youtube.com/")
        print(driver.current_url)
        print(driver.title)
        driver.fullscreen_window()
        driver.refresh()
        #driver.find_element(By.LINK_TEXT().click())
        driver.back()
        driver.forward()
        driver.maximize_window()

        # driver.back()
        # driver.forward()
        # driver.refresh()
        # driver.title()
        # driver.maximize_window()
        # driver.minimize_window()
        #driver.fullscreen.window()
        #driver.close()
        # driver.quit()

        time.sleep(3)
        driver.quit()



findbyid  = DemoSeleniumLearning()
findbyid.demo_browser_methods()