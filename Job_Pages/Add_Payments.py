import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Job_Form import Job_Form_Locators


class AddPayment():
    def __init__(self, driver):
        self.driver = driver

    def add_payment(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, Job_Form_Locators.payment_tab_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.add_payment_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.payment_amount_textbox_id).send_keys("43.89")
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.payment_method_dropdown_id)
        select = Select(dropdown)
        select.select_by_visible_text("Credit Card")
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.payment_type_dropdown_id)
        select = Select(dropdown)
        select.select_by_visible_text("Deposit")
        self.driver.find_element(By.XPATH, Job_Form_Locators.payment_description_text_id).send_keys(
            "For Automation Testing")
        self.driver.find_element(By.XPATH, Job_Form_Locators.payment_save_button_id).click()
