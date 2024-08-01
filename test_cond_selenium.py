import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://demo.applitools.com/")

username = browser.find_element(By.ID, "username")
password = browser.find_element(By.ID, "password")

checkbox_remember_me = browser.find_element(By.CLASS_NAME, "form-check-label")

print(username.is_displayed())
print(password.is_enabled())

checkbox_remember_me.click()
print(checkbox_remember_me.is_selected())

time.sleep(200)