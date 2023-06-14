import time

from selenium.webdriver.common.by import By


class AddJobFromContact():
    def __init__(self, driver):
        self.driver = driver

    def add_job_from_contact(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH,
                            "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div/div/div/span").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/div/button[2]").click()
        time.sleep(7)
        self.driver.find_element(By.XPATH, "(//*[text()='Customer Ref'])[3]/following::input[1]").send_keys(
            "Automation Customer")
        self.driver.find_element(By.XPATH, "//*[text()='Additional Ref']/following::input[1]").send_keys(
            "Automation Testing")
        self.driver.find_element(By.XPATH, "//*[text()='Status Notes']/following::input[1]").send_keys("Automation")
        self.driver.find_element(By.XPATH,
                            "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[2]/button[1]").click()
