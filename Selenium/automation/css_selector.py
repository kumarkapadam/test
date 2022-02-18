from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
class DemoFindelementByandName():
    def locate_by_id_demo(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.get_element(By.CSS_SELECTOR, "#login-input").send_keys("kumarr")
        time.sleep(3)



findbyid  = DemoFindelementByandName()
findbyid.locate_by_id_demo()