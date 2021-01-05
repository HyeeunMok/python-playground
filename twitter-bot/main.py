from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import config
from time import sleep

PROMISED_DOWN = 513
PROMISED_UP = 507
CHROME_DRIVER_PATH = "/Users/hyeeun/Projects/chromedriver"
TWITTER_USERNAME = config.username
TWITTER_PASSWORD = config.password


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.chrome_driver_path = driver_path
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        sleep(2)
        go_button = self.driver.find_element_by_class_name("js-start-test")
        go_button.click()
        sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        url = "https://twitter.com/login/"
        self.driver.get(url)

        sleep(2)
        username = self.driver.find_element_by_name("session[username_or_email]")
        password = self.driver.find_element_by_name("session[password]")

        username.send_keys(TWITTER_USERNAME)
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        write_post = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        # tweet = f"@JayPark_io \nHey Jay, this is my internet speed for wireless: {self.down}down/{self.up}up. For a cable: {PROMISED_DOWN}down/{PROMISED_UP}up! And this is written by my Twitter Bot!"
        tweet = f"Hey, this is my internet speed for wireless: {self.down}down/{self.up}up. For a cable: {PROMISED_DOWN}down/{PROMISED_UP}up! And this is written by my Twitter Bot!"

        write_post.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()


