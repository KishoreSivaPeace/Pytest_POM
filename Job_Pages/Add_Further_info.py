import time

from selenium.webdriver.common.by import By


class AddFurtherInfo():
    def __init__(self, driver):
        self.driver = driver

    def add_further_info(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='notesshowmore']/mat-tab-header/div[2]/div/div/div[3]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='notesshowmore']/div/mat-tab-body[3]/div/div/div/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()=' Terms Name ']/following::input[1]").send_keys("Automation")
        self.driver.find_element(By.XPATH, "//*[text()=' Is Report Show']/following::input[1]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='furtherinfoModal']/div/div/form/div[2]/div/div[3]/div/div/div/angular-editor/div/div/div").send_keys(
            "For Automation Testing")
        self.driver.find_element(By.XPATH, "//*[@id='furtherinfoModal']/div/div/form/div[3]/button[1]").click()