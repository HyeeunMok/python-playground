from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "/Users/hyeeun/Projects/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Hyeeun")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Mok")
email = driver.find_element_by_name("email")
email.send_keys("fastsloth.cs@gmail.com")

sign_up = driver.find_element_by_css_selector(".form-signin button")
sign_up.click()


