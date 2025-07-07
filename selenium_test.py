from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://13.220.161.209:8081")
print("Page Test", driver.title)

driver.quit()
