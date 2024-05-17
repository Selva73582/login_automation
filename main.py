from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

login_url="https://platform.bosscoderacademy.com/login"



driver.get(login_url)
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
input_password.send_keys("123456789")

login_button_xpath = "//button[contains(@class, 'flex') and contains(@class, 'w-full') and contains(@class, 'select-none') and contains(@class, 'items-center') and contains(@class, 'justify-center') and contains(@class, 'rounded-sm') and contains(@class, 'font-medium') and contains(@class, 'py-4') and contains(@class, 'px-8') and contains(@class, 'text-base') and contains(@class, 'leading-5') and contains(@class, 'bg-new-gradient') and contains(@class, 'text-new-solid-white') and contains(@class, 'hover:bg-new-accent') and contains(@class, 'hover:bg-none')]"
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))
button = driver.find_element(By.XPATH, login_button_xpath)
button.click()


dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/aside/nav/div/div[3]/div[1]/div/span[2]'))
)

dropdown.click()

leader_board = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/aside/nav/div/div[3]/div[2]/div[2]/a/div/span[2]'))
)

leader_board.click()


table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="dashboard"]/div/div/div[2]/div[2]/table'))
)


rows = table.find_elements(By.TAG_NAME,"tr")

data = []


for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")
    row_data = []
    for column in columns:
        text = column.text.split("\n", 1)[-1] 
        row_data.append(text)
    print(row_data)
    data.append(row_data)




df = pd.DataFrame(data)
df.to_excel('table_data.xlsx', index=False, header=False)
driver.quit()
