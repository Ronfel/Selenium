from selenium import webdriver
import time

browser = webdriver.Chrome()


browser.get("https://www.google.com")

browser.maximize_window()
time.sleep(5)

browser.get("https://www.saucedemo.com/v1/")
time.sleep(10)

browser.back()
time.sleep(10)

browser.forward()
time.sleep(30)

browser.refresh()
time.sleep(15)

browser.switch_to.new_window("tab")
time.sleep(30)

driver.get("https://www.saucedemo.com/v1/")
time.sleep(30)

browser.quit()