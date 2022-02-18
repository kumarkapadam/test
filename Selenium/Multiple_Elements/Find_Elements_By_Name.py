from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
class DemoFindelementByandName():
    def locate_by_id_demo(self):
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        driver.get("https://www.yatra.com")
        list = driver.find_elements(By.TAG_NAME, "a")
        print(len(list))
        for i in list:
            print(i.text)
        time.sleep(3)



findbyid  = DemoFindelementByandName()
findbyid.locate_by_id_demo()