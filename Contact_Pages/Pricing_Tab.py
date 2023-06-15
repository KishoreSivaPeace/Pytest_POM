import time

import pyautogui
from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class PricingTab():
    def __init__(self, driver):
        self.driver = driver

    def pricing_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.pricing_tab).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.VAT_rate_field).send_keys("45.56")
        pyautogui.press('tab')
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.VAT_regis_no_field).send_keys("ADTEX789456")
        pyautogui.press('tab')
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.surcharge_field).send_keys("7.56")
        pyautogui.press('tab')
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.default_delivery_cost_field).send_keys("14.23")
        pyautogui.press('tab')
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.default_appointment_type_dropdown).click()
        self.driver.find_element(By.XPATH, Contact_Locators.appointment_type_search).send_keys("Measurer")
        self.driver.find_element(By.XPATH, Contact_Locators.appointment_type_option).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.default_staff).click()
        self.driver.find_element(By.XPATH, Contact_Locators.staff_option).click()
