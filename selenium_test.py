from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_agrument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.get("http://<TEST_PUBLIC_IP>:8084")

assert "InsureMe" in driver.title

driver.quit()
