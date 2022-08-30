from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import time

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

path = "C:\\bin\\chromedriver.exe"

driver = webdriver.Chrome(chrome_options=opt, executable_path=rf'{path}')
driver.get('https://vcs.domrf.ru/doc/api/rest.html')
time.sleep(2)
items = [i for i  in [c.text.split() for c in driver.find_elements(By.CLASS_NAME, 'sc-fznNvL')] if i]
print(items)

driver.quit()