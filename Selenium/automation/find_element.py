from selenium import webdriver

# create webdriver object
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.youtube.com/")

# get element
element = driver.find_element(By.ID,"search_query")
action = ActionChains(driver)
action.send_keys("    ").perform()
action.click()

# print complete element
print(element)

