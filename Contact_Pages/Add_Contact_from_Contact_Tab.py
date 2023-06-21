import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Contact_Module import Contact_Locators


class AddContactFromContactTab():
    def __init__(self, driver):
        self.driver = driver
        
    def add_contact_from_contact_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_add_contact_button).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_role_field).send_keys("Tester")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_first_name_field).send_keys("Peace")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_last_name_field).send_keys("Art")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_phone_field).send_keys("234556")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_mobile_field).send_keys("784512132")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_Email_field).send_keys("automation@gmail.com")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_default_contact_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_acc_ref_field).send_keys("Acc44")
        AddressType = self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_address_type_dropdown)
        select = Select(AddressType)
        select.select_by_visible_text("Delivery Address")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_zipcode_field).send_keys("MK13")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_zipcode_search).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_address1_field).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_address1_field).send_keys("Temple Tower")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_address2_field).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_address2_field).send_keys("Anna Salai")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_town_city_field).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_town_city_field).send_keys("Chennai")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_state_dropdown).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_state_dropdown).send_keys("Tamil Nadu")
        pyautogui.scroll(-1500)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_email_yes_radio_button).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_received_document_yes_radio_button).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_received_document_setting_button)).click().perform()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_quotation_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_invoiced_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_order_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_delivery_note_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_credit_note_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_daily_status_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_contact_save_button).click()