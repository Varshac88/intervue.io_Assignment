from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.intervue.io")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

links = driver.find_elements(By.XPATH, "//a[@href]")
for link in links:
    if "Login" in link.get_attribute("innerHTML"):
        link.click()
        break

For_companies = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()

Email = wait.until(EC.presence_of_element_located((By.ID, "login_email"))).send_keys("neha@intervue.io")
Password = driver.find_element(By.ID, "login_password").send_keys("Neha@567intervue")
Login = driver.find_element(By.CSS_SELECTOR, ".btn.ant-btn-lg").click()
print("login clicked")

search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "SearchBox__StyledInput-ctnsh0-4")))
search_input.send_keys("hello")

time.sleep(4)

logout_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Logout']")))
logout_link.click()

time.sleep(2)
driver.quit()
