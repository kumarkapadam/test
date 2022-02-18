from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByIdandName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("")
        driver.find_element_by_name('login-input').send_keys('test@test.com')



findbyid = DemoFindElementByIdandName()
findbyid.locate_by_id_demo()
