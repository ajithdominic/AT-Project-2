# TC_PIM_02 : Header and other options validation in the Admin page of OrangeHRM portal - Chrome Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Ajith:
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    username = 'Admin'
    password = 'admin123'
    

# Render URL & Login
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(5)

#  Navigate to Admin page & Header Title validation 
    def admin(self):
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        sleep(2)
        try:
            assert self.driver.title == 'OrangeHRM'
            print("'OrangeHRM' title - Header Validation Successful")
        except AssertionError:
            print("Header Validation Failed")
        
# Displayed options validation in the Admin page   
    def admin_options(self):
        usermanagement_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
        try:
            assert usermanagement_option.text == 'User Management'
            print("'User Management' option is displayed")
        except AssertionError:
            print("'User Management' option is NOT displayed")
          
        job_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
        try:
            assert job_option.text == 'Job'
            print("'Job' option is displayed")
        except AssertionError:
            print("'Job' option is NOT displayed")

        organization_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
        try:
            assert organization_option.text == 'Organization'
            print("'Organization' option is displayed")
        except AssertionError:
            print("'Organization' option is NOT displayed")

        qualifications_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span')
        try:
            assert qualifications_option.text == 'Qualifications'
            print("'Qualifications' option is displayed")
        except AssertionError:
            print("'Qualifications' option is NOT displayed")

        nationalities_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a')
        try:
            assert nationalities_option.text == 'Nationalities'
            print("'Nationalities' option is displayed")
        except AssertionError:
            print("'Nationalities' option is NOT displayed")

        corporate_banking_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]')
        try:
            assert corporate_banking_option.text == 'Corporate Banking'
            print("'Corporate Banking' option is displayed")
        except AssertionError:
            print("'Corporate Banking' option is NOT displayed")
        
        configuration_option = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span')
        try:
            assert configuration_option.text == 'Configuration'
            print("'Configuration' option is displayed")
        except AssertionError:
            print("'Configuration' option is NOT displayed")
        sleep(5)
        self.driver.quit()


Ajith().login()
Ajith().admin()
Ajith().admin_options()