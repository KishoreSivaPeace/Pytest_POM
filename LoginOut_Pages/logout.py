import time

from selenium.webdriver.common.by import By
from Locators.Login_Logout import Login_out_Locators

class LogOut():
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, Login_out_Locators.profile_dropdown_id).click()
        self.driver.find_element(By.XPATH, Login_out_Locators.logout_id).click()
