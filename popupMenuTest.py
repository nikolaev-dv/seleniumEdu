from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1920,1080)

driver.get('https://www.vysota5642.ru')

buttonRest = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/ul/li[2]/a")
buttonRest.click()
time.sleep(1)

buttonEkb = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[3]/div/div[3]/div/ul/li[2]/div/div/div/ul/li[5]/a')
buttonEkb.click()
time.sleep(1)

driver.close()