import time

import pyautogui
from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class CommissionTab():
    def __init__(self, driver):
        self.driver = driver

    def commission_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_tab).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.add_commission_button).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_field).send_keys("45.89")
        self.driver.find_element(By.XPATH, Contact_Locators.sales_consultant_dropdown).click()
        self.driver.find_element(By.XPATH, Contact_Locators.sales_consultant_option1).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_dropdown).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_option1).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_option2).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_option3).click()
        pyautogui.press('tab')
        self.driver.find_element(By.XPATH, Contact_Locators.commission_save_button).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, Contact_Locators.add_commission_button).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_field).send_keys("25.89")
        self.driver.find_element(By.XPATH, Contact_Locators.sales_consultant_dropdown).click()
        self.driver.find_element(By.XPATH, Contact_Locators.sales_consultant_option2).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_dropdown).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_option1).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_product_option2).click()
        pyautogui.press('tab')
        self.driver.find_element(By.XPATH, Contact_Locators.commission_save_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.commission_3dot).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_3dot_delete).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_3dot_delete_ok).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.commission_send_email_checkbox).click()
