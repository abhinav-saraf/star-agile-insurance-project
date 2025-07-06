from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_agrument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.get("http://54.173.223.6:8084")

assert "InsureMe" in driver.title

driver.quit()
