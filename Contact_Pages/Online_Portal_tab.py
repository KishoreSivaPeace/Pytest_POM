import time

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Contact_Module import Contact_Locators


class OnlinePortalTab():
    def __init__(self, driver):
        self.driver = driver

    def online_portal_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.online_portal_tab).click()
        time.sleep(4)
        # Alljobs = self.driver.find_element(By.XPATH, Contact_Locators.online_portal_all_job_dropdown)
        # select1 = Select(Alljobs)
        # select1.select_by_visible_text("Default View")
        # time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.online_portal_discount_field).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.online_portal_discount_field).send_keys("15")
        pyautogui.press('tab')
        time.sleep(3)
        Language = self.driver.find_element(By.XPATH, Contact_Locators.online_portal_language_dropdown)
        select2 = Select(Language)
        select2.select_by_visible_text("English")
        time.sleep(3)
        Notification = self.driver.find_element(By.XPATH, Contact_Locators.online_portal_notification_dropdown)
        select3 = Select(Notification)
        select3.select_by_visible_text("Acknowledge Template")
