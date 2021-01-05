from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
import time

ACCOUNT_EMAIL = config.my_email
ACCOUNT_PASSWORD = config.password
PHOHNE = config.phone

url = "https://www.linkedin.com/jobs/search/?currentJobId=2332640105&geoId=102257491&keywords=web%20developer&location=London%2C%20England%2C%20United%20Kingdom"
chrome_driver_path = "/Users/hyeeun/Projects/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

user_name = driver.find_element_by_id("username")
time.sleep(1)
user_name.send_keys(ACCOUNT_EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)


#Locate the apply button
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone == "":
    phone.send_keys(PHOHNE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()


# next_button = driver.find_element_by_class_name("artdeco-button--primary")
# next_button.click()
# time.sleep(2)
# next_button.click()
#
# time.sleep(2)
# next_button.click()