from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("http://13.220.161.209:8084")

time.sleep(3)
assert "InsureMe" in driver.title or "Login" in driver.page_source

print("Test Passed: Web app is running")

driver.quit()
