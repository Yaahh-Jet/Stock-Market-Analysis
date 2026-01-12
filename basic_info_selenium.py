#selenium not working becoz google uses ghost DOM and now does not works

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = "https://www.google.com/finance/quote/ONGC:NSE"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get(url)

# ---- accept cookies if present ----
try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button//div[normalize-space()='Accept all']")
        )
    ).click()
except:
    pass


time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

rows = soup.select(".KxsRFb")

print("Rows found:", len(rows))

data = {}
for row in rows:
    label = row.select_one(".SwQK7")
    value = row.select_one(".dO6ijd")
    if label and value:
        data[label.text.strip()] = value.text.strip()

driver.quit()

for k, v in data.items():
    print(f"{k:25} : {v}")


