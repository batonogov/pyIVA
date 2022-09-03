from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Chrome(executable_path=r'C:\\Users\\nerv_\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome()

driver.get('https://vcs.domrf.ru/doc/api/rest.html')
# time.sleep(1)

with open('pyIVA/__init__.py', 'w') as f:
    f.write("__version__ = '0.0.1'\n\n")
    [f.write(f"class {c.title()}:\n    pass\n\n") for c in [' '.join(c).replace(' ', '_') for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][1:5]]]
    [f.write(f"class {c.title()}:\n") for c in [''.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][5]]]
    [f.write(f"    def {i.title().replace(' ', '_').replace('/', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][6:36]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][6:7]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][36:42]]]
    [f.write(f"class {c.title()}:\n") for c in [''.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][7]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][42:47]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][8:9]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][47:67]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][9:10]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][67:75]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][10:11]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][75:85]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][11:12]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][85:92]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][12:13]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][92:107]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][13:14]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][107:116]]]
    [f.write(f"class {c.title()}:\n") for c in [''.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][14]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][116:121]]]
    [f.write(f"class {c.title()}:\n") for c in [''.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][15]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][121:124]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][16:17]]]
    [f.write(f"    def {i.title().replace(' ', '_')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][124:126]]]
    [f.write(f"class {c.title()}:\n") for c in ['_'.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][17:18]]]
    [f.write(f"    def {i.title().replace(' ', '_').replace('.', '')}():\n        pass\n\n") for i in [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][126:138]]]
# User следущая строка для парсинга.

    

# cmd_def = [i.text.replace(' ', '_') for i in driver.find_elements(By.TAG_NAME, 'h2')]
# print(cmd_def)   

# h1 = [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h1')][1:]]
# h2 = [' '.join(c) for c in [c.text.split() for c in driver.find_elements(By.TAG_NAME, 'h2')][6:36]] # CHAT
# print(h2)

# href = [str(i.get_attribute('href'))[39:] for i in driver.find_elements(By.TAG_NAME, "a")]
# z = []
# for i in href:
#     if i[0:9] == 'operation' and i not in z:
#         z.append(i)
# with open('pyIVA/raw.py', 'w') as f:
#     for i in z:
#         try:
#             data = driver.find_element(By.ID, f"{i}").text
#             f.write(f"{data}\n\n")
#             print(data)
#         except:
#             pass

# for i in driver.find_elements(By.TAG_NAME, 'h1'):
#     if i.text in button:
#         i.click()
#         time.sleep(2)
#         for c in driver.find_elements(By.CLASS_NAME, 'dbpfvr'):
#             print([' '.join(c) for c in [c.text.split()]])
#         print(i.text)

driver.quit()
