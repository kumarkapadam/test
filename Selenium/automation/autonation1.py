from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementById():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("")
        # driver.find_element_by_id('login-input').send_keys('test@test.com')
        # driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("kumar")
        driver.find_element(By.ID,'login-input').send_keys('test@test.com')

findbyid = DemoFindElementById()
findbyid.locate_by_id_demo()
