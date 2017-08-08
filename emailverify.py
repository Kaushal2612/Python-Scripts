from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Users\\Kaushal Jhawar\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en")

print(driver.title)

driver.find_element_by_css_selector("input#GmailAddress").send_keys("kaushaljhawar3")
driver.find_element_by_id("Passwd").send_keys("kaushal")

error = driver.find_element_by_xpath("//span[@id='errormsg_0_GmailAddress']").text

print('Found')
print(error)
