from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


browser.get("https://www.google.com")

browser.maximize_window()
time.sleep(5)

browser.get("https://www.saucedemo.com/v1/")
username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
button = browser.find_element(By.ID, "login-button")


username.send_keys("standard_user")
password.send_keys("secret_sauce")
button.click()

title = browser.find_element(By.CLASS_NAME, "product_label")
print(title.text)
assert title.text == "Products"
imgBag = browser.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")
print(imgBag.get_attribute("class"))
imgBag.click()

time.sleep(30)

authelements = browser.find_elements(By.CLASS_NAME, 'form_input')
print('Total de Elementos: ', str(len(authelements)))

'''
assert len(authelements) == 3, "Total de Campos não é igual a 3"
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
'''
browser.quit()
