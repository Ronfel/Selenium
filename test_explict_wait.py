import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://www.hyrtutorials.com/p/waits-demo.html#google_vignette")

wait = WebDriverWait(browser, 60)

btn1 = browser.find_element(By.ID, "btn1").click()
wait.until(EC.element_to_be_clickable((By.ID, "txt1")))


btn2 = browser.find_element(By.ID, "btn2").click()
wait.until(EC.element_to_be_clickable((By.ID, "txt2")))
browser.quit()