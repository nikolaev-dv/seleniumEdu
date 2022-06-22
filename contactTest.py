from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1920,1080)

driver.get('https://www.vysota5642.ru/')

buttonContacts = driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div/div[3]/div/div[3]/div/ul/li[3]/a')
buttonContacts.click()
time.sleep(1)

inputName = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/input')
inputName.send_keys('Denis')
time.sleep(1)

inputPhone = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div[2]/div[1]/input[1]')
inputPhone.send_keys('9997771122')
time.sleep(1)

selectCountry = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div[1]/select')
selectCountry.click()
time.sleep(1)
#выбрать регион пока не понял как



driver.close()