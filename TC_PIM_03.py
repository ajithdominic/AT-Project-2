# TC_PIM_03 : Validation MENU options in the Admin page's side pane of OrangeHRM portal - Chrome Browser

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
    

# Render URL, Login & Navigate to Admin page
    def login_admin(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
        sleep(2)
        
# Displayed MENU options validation in the Admin page's side pane 
    def menu_options(self):
        admin_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        try:
            assert admin_menu.text == 'Admin'
            print("'Admin' Menu option is displayed")
        except AssertionError:
            print("'Admin' Menu option is NOT displayed")
          
        pim_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        try:
            assert pim_menu.text == 'PIM'
            print("'PIM' Menu option is displayed")
        except AssertionError:
            print("'PIM' Menu option is NOT displayed")

        leave_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')
        try:
            assert leave_menu.text == 'Leave'
            print("'Leave' Menu option is displayed")
        except AssertionError:
            print("'Leave' Menu option is NOT displayed")

        time_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
        try:
            assert time_menu.text == 'Time'
            print("'Time' Menu option is displayed")
        except AssertionError:
            print("'Time' Menu option is NOT displayed")

        recruitment_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a')
        try:
            assert recruitment_menu.text == 'Recruitment'
            print("'Recruitment' Menu option is displayed")
        except AssertionError:
            print("'Recruitment' Menu option is NOT displayed")

        myinfo_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
        try:
            assert myinfo_menu.text == 'My Info'
            print("'My Info' Menu option is displayed")
        except AssertionError:
            print("'My Info' Menu option is NOT displayed")

        performance_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
        try:
            assert performance_menu.text == 'Performance'
            print("'Performance' Menu option is displayed")
        except AssertionError:
            print("'Performance' Menu option is NOT displayed")

        dashboard_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a')
        try:
            assert dashboard_menu.text == 'Dashboard'
            print("'Dashboard' Menu option is displayed")
        except AssertionError:
            print("'Dashboard' Menu option is NOT displayed")

        directory_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span')
        try:
            assert directory_menu.text == 'Directory'
            print("'Directory' Menu option is displayed")
        except AssertionError:
            print("'Directory' Menu option is NOT displayed")

        maintenance_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
        try:
            assert maintenance_menu.text == 'Maintenance'
            print("'Maintenance' Menu option is displayed")
        except AssertionError:
            print("'Maintenance' Menu option is NOT displayed")

        buzz_menu = self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
        try:
            assert buzz_menu.text == 'Buzz'
            print("'Buzz' Menu option is displayed")
        except AssertionError:
            print("'Buzz' Menu option is NOT displayed")
        sleep(5)
        self.driver.quit()


Ajith().login_admin()
Ajith().menu_options()