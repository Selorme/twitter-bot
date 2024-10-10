import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
SPEED_TEST_URL = os.environ["speed_test_url"]
message = "hi there, just working on an X automation as my project for #100daysofcode day 51 project. So yes, this tweet is from Selenium!"

# start_text = driver.find_element(By.CLASS_NAME, "start-text")
# start_text.click()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # self.driver.get("https://www.speedtest.net/")
        #
        # accept_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        # accept_button.click()
        #
        # time.sleep(3)
        #
        # go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        # go_button.click()
        #
        # time.sleep(120)
        # self.up = self.driver.find_element(By.XPATH,
        #                                    value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # self.down = self.driver.find_element(By.XPATH,
        #                                      '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        pass

    def tweet_at_provider(self):
        time.sleep(10)
        self.driver.get(url="https://x.com")
        self.driver.maximize_window()
        time.sleep(3)
        welcome_close = self.driver.find_elements(By.CSS_SELECTOR, value='.css-175oi2r .r-2o02ov .css-175oi2r .r-1777fci')
        for x in welcome_close:
            x.click()
        time.sleep(5)
        login_window = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        time.sleep(5)
        login_window.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        password_window = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_window.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(10)
        comment_window = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div')
        comment_window.click()
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(message)
        post_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span')
        post_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
