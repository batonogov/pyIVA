from faulthandler import is_enabled
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://vcs.domrf.ru/doc/api/rest.html')
time.sleep(1)

with open('pyIVA/__init__.py', 'w') as f:
    f.write("__version__ = '0.0.1'\n\n")
    [f.write(f"class {c.title()}:\n    pass\n\n") for c in [' '.join(c).replace(' ', '_') for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][1:]]]

driver.quit()
