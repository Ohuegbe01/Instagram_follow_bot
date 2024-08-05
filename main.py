import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException


SIMILAR_ACCOUNT = 'https://www.instagram.com/coding_unicorn/'
USERNAME = ''
PASSWORD = ''
url = ' https://www.instagram.com/accounts/login/'


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(url)
        time.sleep(5)
        cookies = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        cookies.click()

        time.sleep(5)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(USERNAME)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        time.sleep(3)
        log_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        log_button.click()

        time.sleep(10)
        save_info = self.driver.find_element(By.CSS_SELECTOR, '.x78zum5 button')
        save_info.click()

        time.sleep(5)
        notifications_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
        notifications_button.click()


    def find_followers(self):
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(5)
        follower_list = self.driver.find_element(By.LINK_TEXT, '110K followers')
        follower_list.click()
        time.sleep(5)
        scroll_window = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]'
        for _ in range(5):  # Adjust the range as needed
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_window)
            time.sleep(2)

    def follow(self):
        follow_button = self.driver.find_elements(By.CSS_SELECTOR, '.xyi19xy button')
        print(follow_button)
        for _ in follow_button:
            try:
                print(_)
                _.click()
                time.sleep(1.1)

            except ElementClickInterceptedException:
                try:
                    ok = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
                    ok.click()
                except NoSuchElementException:
                    pass
                try:
                    cancel_button = self.driver.find_element(by=By.XPATH,
                                                             value="/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")
                    cancel_button.click()
                except NoSuchElementException:
                    pass

instagram = InstaFollower()
instagram.login()
instagram.find_followers()

instagram.follow()
