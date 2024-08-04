import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://www.hyrtutorials.com/p/waits-demo.html#google_vignette")
browser.implicitly_wait(12)

btn1 = browser.find_element(By.ID, "btn1")
btn2 = browser.find_element(By.ID, "btn2")


btn1.click()
browser.implicitly_wait(7)

txt1 = browser.find_element(By.ID, "txt1")
print(txt1.is_displayed())

btn2.click()
browser.implicitly_wait(14)

txt2 = browser.find_element(By.ID, "txt2")
print(txt2.is_displayed())

browser.quit()