from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import *

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)