# TC_PIM_01 : Forgot password link validation on OrangeHRM Portal - Chrome Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Ajith:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'Admin'
    

# Render URL & Forgot password link validation
    def forgot_password(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p').click()
        sleep(2)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
        sleep(5)
        confirmation_message = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/div/p[1]/p')
        try:
            assert confirmation_message.text == 'A reset password link has been sent to you via email.'
            print("'Reset Password' link validation - Successful")
        except AssertionError:
            print("'Reset Password' link validation - Failed")        
        sleep(5)
        self.driver.quit()

Ajith().forgot_password()