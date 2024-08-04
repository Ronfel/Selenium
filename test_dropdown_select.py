import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://www.hyrtutorials.com/p/html-dropdown-elements-practice.html")

dropdown = Select(browser.find_element(By.ID, "course"))
dropdown.select_by_visible_text("Python")
time.sleep(10)
dropdown.select_by_value("net")
time.sleep(10)
dropdown.select_by_index(1)
time.sleep(10)