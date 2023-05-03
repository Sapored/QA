import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    'C:/Chrome-webdrivers/chromedriver.exe')
driver.get("https://www.yimi.com.mx/negocio")

CreateAccount = driver.find_element(
    By.XPATH, '/html/body/section[3]/div/div/div[1]/div/a[1]')
CreateAccount.click()

Email = driver.find_element(By.ID, 'emailInputCheck')
Email.send_keys("sochoadiaz899@gmail.com")

