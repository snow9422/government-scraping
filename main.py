from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

base_url = "https://www.tenders.vic.gov.au/login"
driver.get(base_url)

wait = WebDriverWait(driver, 10)

usernameInput_id = "supplierUsername"
passwordInput_id = "supplierPassword"
loginButton_class = "btn-primary"

username = "Edf"
password = "Passme3!"

wait.until(EC.presence_of_element_located((By.ID, usernameInput_id))).send_keys(username)
wait.until(EC.presence_of_element_located((By.ID, passwordInput_id))).send_keys(password)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, loginButton_class))).click()

driver.get("https://www.tenders.vic.gov.au/secure/tender/downloadSpecDocs?tenderId=249237")

downloadBtn = "downloadButton"

download_button = wait.until(EC.element_to_be_clickable((By.ID, downloadBtn)))

driver.execute_script("arguments[0].scrollIntoView();", download_button)
driver.execute_script("arguments[0].click();", download_button)

sleep(200)
driver.quit()
