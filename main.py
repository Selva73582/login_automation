from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://platform.bosscoderacademy.com/login")
email_id = "login-email"
password_id = "login-password"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, email_id))
    )
input_email = driver.find_element(By.ID, email_id)
input_email.send_keys("abc@gmail.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, password_id))
    )
input_password = driver.find_element(By.ID, password_id)
input_password.send_keys("12345678")

login_button_xpath = "//button[contains(@class, 'flex') and contains(@class, 'w-full') and contains(@class, 'select-none') and contains(@class, 'items-center') and contains(@class, 'justify-center') and contains(@class, 'rounded-sm') and contains(@class, 'font-medium') and contains(@class, 'py-4') and contains(@class, 'px-8') and contains(@class, 'text-base') and contains(@class, 'leading-5') and contains(@class, 'bg-new-gradient') and contains(@class, 'text-new-solid-white') and contains(@class, 'hover:bg-new-accent') and contains(@class, 'hover:bg-none')]"
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))
button = driver.find_element(By.XPATH, login_button_xpath)
button.click()

zoin_xpath = '//button[contains(@class, "flex") and contains(@class, "w-full") and contains(@class, "select-none") and contains(@class, "items-center") and contains(@class, "justify-center") and contains(@class, "rounded-sm") and contains(@class, "font-medium") and contains(@class, "w-fit") and contains(@class, "py-4") and contains(@class, "px-8") and contains(@class, "text-base") and contains(@class, "leading-5") and contains(@class, "bg-new-gradient") and contains(@class, "text-new-solid-white") and contains(@class, "hover:bg-new-accent") and contains(@class, "hover:bg-none")]'

WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,zoin_xpath)))
button = driver.find_element(By.XPATH,zoin_xpath)
button.click()

time.sleep(20)
driver.quit()
