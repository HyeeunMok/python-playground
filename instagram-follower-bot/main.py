import config
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import random

CHROME_DRIVER_PATH = "/Users/hyeeun/Projects/chromedriver"
SIMILAR_ACCOUNT = "theminimalists"
USERNAME = config.username
PASSWORD = config.password
INSTA_URL = "https://www.instagram.com/"

class InstaFollower:

    def __init__(self, driver_path):
        self.chrome_driver_path = driver_path
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get(f"{INSTA_URL}accounts/login/")
        sleep(2)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        sleep(1)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(3)
        self.driver.get(f"{INSTA_URL}{SIMILAR_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                wait_time = random.randint(4, 14)
                button.click()
                sleep(wait_time)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
