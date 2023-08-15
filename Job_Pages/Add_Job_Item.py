import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Locators.Job_Form import Job_Form_Locators


class JobItem():
    def __init__(self, driver):
        self.driver = driver

    def new_job_item(self):
        time.sleep(15)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, Job_Form_Locators.add_product_button_id)).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Job_Form_Locators.add_product_search_id).send_keys("Roller")
        action.move_to_element(self.driver.find_element(By.XPATH, Job_Form_Locators.add_product_id)).click().perform()
        time.sleep(15)
        self.driver.find_element(By.XPATH, Job_Form_Locators.room_id).send_keys("Hall")
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.blind_recess_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.blind_option_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Job_Form_Locators.width_id).send_keys("1500")
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.drop_id).send_keys("2000")
        time.sleep(3)
        dropdown = self.driver.find_element(By.XPATH, Job_Form_Locators.product_type_id)
        select = Select(dropdown)
        select.select_by_visible_text("FB Band AA")
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.fabric_field_id).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.fabric_id).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, Job_Form_Locators.color_field_id).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, Job_Form_Locators.color_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, Job_Form_Locators.Further_Instruction_id).send_keys("Automation")
        time.sleep(2)
        self.driver.find_element(By.XPATH, Job_Form_Locators.job_item_save_button_id).click()
