from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get('https://vcs.domrf.ru/doc/api/rest.html')
time.sleep(1)
items = [i for i  in [c.text.split() for c in driver.find_elements(By.CLASS_NAME, 'sc-fznNvL')] if i]

# [print(c) for c in items]

with open('pyIVA/__init__.py', 'w') as f:
    f.write("__version__ = '0.0.1'\n\n")
    [f.write(f"class {c[0].title()}:\n    pass\n\n") for c in items if c[0].isupper()]

buttons = [' '.join(c) for c in items if not c[0].isupper()]

for i in driver.find_elements(By.CLASS_NAME, 'sc-fznNvL'):
    if i.text in buttons:
        i.click()
        time.sleep(1)


driver.quit()
