from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


id = "<mail here>"
password = "<password>"
profile_name = "<profile_name>"

# Using google chrome and maximum the window
driver = webdriver.Chrome()
driver.maximize_window()

# Going to https://www.netflix.com/in/login
driver.get('https://www.netflix.com/in/login')

# Putting userid / email
driver.find_element_by_name("userLoginId").send_keys(id)

# Putting password
driver.find_element_by_name("password").send_keys(password)

# Doing signin
signin = driver.find_element_by_css_selector(".btn.login-button.btn-submit.btn-small")
signin.click()

# Set up profile
time.sleep(5)
driver.find_element_by_link_text(profile_name).click()

# running any trailer 
time.sleep(5)
driver.find_element_by_xpath('//*[@id="title-card-2-0"]/div[1]/a/div[1]/img').click()

# Get description
time.sleep(5)
description = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[1]/p/div').text
print("The description is - " + description)

# Get starcast
time.sleep(5)
starcast = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[2]/div[1]').text
print("The star casts are - " + starcast)
