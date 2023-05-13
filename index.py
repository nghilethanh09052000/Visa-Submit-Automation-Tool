import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


options = Options()
options.add_experimental_option("detach", True)


# Perform browser automation:
driver = webdriver.Chrome(options=options)
driver.get('https://online.immi.gov.au/lusc/login')

# Login website:
username_element = driver.find_element(By.ID,'username')
username_element.clear()
username_element.send_keys('nghilt19411@gmail.com')

password_element = driver.find_element(By.ID,'password')
password_element.clear()
password_element.send_keys('abcABC@123456789')

login_element = driver.find_element(By.NAME, 'login')
login_element.send_keys(Keys.ENTER)
time.sleep(2)

# Continue Website:
continue_element = driver.find_element(By.NAME, 'continue')
continue_element.click()
time.sleep(2)

# Edit Website: # https://online.immi.gov.au/ola/app
edit_element = driver.find_element(By.ID, 'defaultActionPanel_0_1')
edit_element.click()

# Page 1:
check_box_element = driver.find_element(By.XPATH, '//div[@class="wc-content"]/div/div/span/input')
if(check_box_element.is_selected()):
    next_element_page_1 = driver.find_element(By.XPATH,'//div[@class="wc-borderlayout"]/div/div[2]/button')
    next_element_page_1.click()
else:
    next_element_page_1 = driver.find_element(By.XPATH,'//div[@class="wc-borderlayout"]/div/div[2]/button')
    next_element_page_1.click()

# Page 2:
select_current_location_filed = Select(driver.find_element(By.XPATH,'//div[@class="wc-content"]/div[@class="wc-panel"]/div[@class="wc-content"]/div/div[@class="wc-content"]/div[2]/div/div[3]/div/div/div[2]/span/select'))
select_current_location_filed.select_by_visible_text("THAILAND")
