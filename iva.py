from faulthandler import is_enabled
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome(executable_path=r'C:\\Users\\nerv_\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome()

driver.get('https://vcs.domrf.ru/doc/api/rest.html')
# time.sleep(1)

# with open('pyIVA/__init__.py', 'w') as f:
#     f.write("__version__ = '0.0.1'\n\n")
#     [f.write(f"class {c.title()}:\n    pass\n\n") for c in [' '.join(c).replace(' ', '_') for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][1:]]]

# cmd_def = [i.text.replace(' ', '_') for i in driver.find_elements(By.TAG_NAME, 'h2')]
# print(cmd_def)   

# h1 = [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][1:]]
# h2 = [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')]]



href = [str(i.get_attribute('href'))[39:] for i in driver.find_elements(By.TAG_NAME, "a")]
z = []
for i in href:
    if i[0:9] == 'operation' and i not in z:
        z.append(i)
for i in z:
    print(i)
    try:
        print(driver.find_element(By.ID, f"{i}").text)
    except:
        pass


# for i in driver.find_elements(By.TAG_NAME, 'h1'):
#     if i.text in button:
#         i.click()
#         time.sleep(2)
#         for c in driver.find_elements(By.CLASS_NAME, 'dbpfvr'):
#             print([' '.join(c) for c in [c.text.split()]])
#         print(i.text)


driver.quit()
