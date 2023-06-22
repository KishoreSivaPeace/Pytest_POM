import time

import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Contact_Module import Contact_Locators


class AddContact():
    def __init__(self, driver):
        self.driver = driver

    def add_contact(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_main).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_add_button).click()
        self.driver.find_element(By.XPATH, Contact_Locators.add_customer_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.choose_contact_type).click()
        self.driver.find_element(By.XPATH, Contact_Locators.select_contact_type).click()
        self.driver.find_element(By.XPATH, Contact_Locators.next_button).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Contact_Locators.role_field).send_keys("Tester")
        self.driver.find_element(By.XPATH, Contact_Locators.first_name_field).send_keys("Peace")
        self.driver.find_element(By.XPATH, Contact_Locators.last_name_field).send_keys("Art")
        self.driver.find_element(By.XPATH, Contact_Locators.phone_field).send_keys("235689")
        self.driver.find_element(By.XPATH, Contact_Locators.mobile_field).send_keys("9876543210")
        self.driver.find_element(By.XPATH, Contact_Locators.Email_field).send_keys("kishoresiva95@gmail.com")
        self.driver.find_element(By.XPATH, Contact_Locators.default_contact_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.acc_ref_field).send_keys("ACC004")
        pyautogui.scroll(-1500)
        self.driver.find_element(By.XPATH, Contact_Locators.company_name_field).send_keys("9One Piece")
        self.driver.find_element(By.XPATH, Contact_Locators.source_field).click()
        self.driver.find_element(By.XPATH, Contact_Locators.source_option).click()
        AddressType = self.driver.find_element(By.XPATH, Contact_Locators.address_type_dropdown)
        select = Select(AddressType)
        select.select_by_visible_text("Invoice Address")
        self.driver.find_element(By.XPATH, Contact_Locators.zipcode_field).send_keys("MK13")
        self.driver.find_element(By.XPATH, Contact_Locators.zipcode_search).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.address1_field).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.address1_field).send_keys("Temple Tower")
        self.driver.find_element(By.XPATH, Contact_Locators.address2_field).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.address2_field).send_keys("Anna Salai")
        self.driver.find_element(By.XPATH, Contact_Locators.town_city_field).clear()
        self.driver.find_element(By.XPATH, Contact_Locators.town_city_field).send_keys("Chennai")
        Country = self.driver.find_element(By.XPATH, Contact_Locators.country_field)
        select = Select(Country)
        select.select_by_visible_text("USA")
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.state_dropdown).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Contact_Locators.state_option).click()
        self.driver.find_element(By.XPATH, Contact_Locators.email_yes_radio_button).click()
        self.driver.find_element(By.XPATH, Contact_Locators.received_document_yes_radio_button).click()
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element(By.XPATH, Contact_Locators.received_document_setting_button)).perform()
        self.driver.find_element(By.XPATH, Contact_Locators.quotation_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.invoiced_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.order_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.delivery_note_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.credit_note_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.daily_status_checkbox).click()
        self.driver.find_element(By.XPATH, Contact_Locators.online_portal_yes_radio_button).click()
        action2 = ActionChains(self.driver)
        action2.move_to_element(self.driver.find_element(By.XPATH, Contact_Locators.set_config_option)).perform()
        self.driver.find_element(By.XPATH, Contact_Locators.user_name_field).send_keys("KishoreSiva9")
        self.driver.find_element(By.XPATH, Contact_Locators.password_field).send_keys("1103")
        self.driver.find_element(By.XPATH, Contact_Locators.password_confirm_field).send_keys("1103")
        self.driver.find_element(By.XPATH, Contact_Locators.contact_save_button).click()
