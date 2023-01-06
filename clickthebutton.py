from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://clickcounter.io/')
driver.implicitly_wait(10)

while True:
    try:
        driver.find_element(By.XPATH, "//*[@id='clickarea']").click()
    except:
        print('buttonnya udahan')
        break

sleep(10)
