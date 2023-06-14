import time

import pyautogui
from selenium.webdriver.common.by import By


class PricingTab():
    def __init__(self, driver):
        self.driver = driver
        
    def pricing_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[3]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//*[text()='Customer-Specific VAT Rate']/following::input[1]").send_keys("45.56")
        pyautogui.press('tab')
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[text()='VAT Registration Number']/following::input[1]").send_keys(
            "ADTEX789456")
        pyautogui.press('tab')
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[text()='Customer Surcharge(%)']/following::input[1]").send_keys("7.56")
        pyautogui.press('tab')
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[text()='Default Delivery Cost']/following::input[1]").send_keys("14.23")
        pyautogui.press('tab')
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                            "//*[text()='Default Appointment Type']/following::mat-form-field[1]/div/div[1]/div/mat-select/div").click()
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/input").send_keys("Measurer")
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[2]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                            "(//*[@class='col-xl-8 col-lg-6 col-md-8']/following::mat-select[1]/div)[2]/div[1]").click()
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[2]").click()
