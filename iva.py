from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://vcs.domrf.ru/doc/api/rest.html')
time.sleep(2)
items = [i for i  in [c.text.split() for c in driver.find_elements(By.CLASS_NAME, 'sc-fznNvL')] if i]
print(items)

driver.quit()
