import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Locators.Contact_Module import Contact_Locators


class DeleteContact():
    def __init__(self, driver):
        self.driver = driver
        
    def delete_contact(self):
        time.sleep(6)
        # From Contact Tab
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_delete_icon)).click().perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_delete_ok_button).click()
        time.sleep(5)
        # From 3dots
        self.driver.find_element(By.XPATH, Contact_Locators.contact_tab_leads_customers_name).click()
        time.sleep(8)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_1st_row_3dot_icon).click()
        self.driver.find_element(By.XPATH, Contact_Locators.contact_1st_row_3dot_delete_option).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, Contact_Locators.contact_1st_row_3dot_delete_ok_button).click()
        time.sleep(9)