import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:/Chrome-webdrivers/chromedriver.exe')
driver.get("https://pos.yimiglobal.com/login")
Email = driver.find_element(By.ID, 'emailInputCheck')
Email.send_keys('yimiwings@gmail.com')

logButton = driver.find_element(By.ID, 'loginButton')
logButton.click()

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "passWordLogin")))
password.send_keys('123456')

LoginButton = driver.find_element(By.ID, 'loginButton')
LoginButton.click()
time.sleep(10)

PinButton = driver.find_element(
    By.XPATH, 'html/body/div/div[3]/div[2]/div[4]/div[2]')
for i in range(4):
    PinButton.click()

