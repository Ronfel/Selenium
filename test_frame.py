import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.hyrtutorials.com/p/frames-practice.html")

frame2 = browser.find_element(By.ID, "frm2")
browser.switch_to.frame(frame2)
firstName = browser.find_element(By.XPATH, "//*[@class='inp']/following-sibling::input")
firstName.send_keys("Rodrigo")

browser.switch_to.default_content()
frame1 = browser.find_element(By.ID, "frm1")
browser.switch_to.frame(frame1)

time.sleep(10)

dropdown = Select(browser.find_element(By.ID, "course"))
dropdown.select_by_visible_text("Python")


time.sleep(10)
