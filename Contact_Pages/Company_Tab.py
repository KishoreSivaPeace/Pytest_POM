import time

from selenium.webdriver.common.by import By


class CompanyTab():
    def __init__(self,driver):
        self.driver = driver

    def company_tab(self):
        time.sleep(6)
        self.driver.find_element(By.XPATH,
                            "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button").click()
        self.driver.find_element(By.XPATH,
                            "/html/body/app-root/main/section/app-job/div[11]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/button[2]").click()
        time.sleep(2)
        current_window_handle = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        next_window_handle = window_handles[(window_handles.index(current_window_handle) + 1) % len(window_handles)]
        self.driver.switch_to.window(next_window_handle)
        time.sleep(6)
        self.driver.find_element(By.XPATH, "(//*[@class='mat-tab-labels'])[2]/div[1]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div[2]/app-dynamic-field/input").send_keys(
            "ACC005")
        self.driver.find_element(By.XPATH, "//*[text()='Source']/following::mat-select[1]/div/div/span").click()
        self.driver.find_element(By.XPATH, "//*[@aria-label='dropdown search']").send_keys("FB")
        self.driver.find_element(By.XPATH, "//*[@class='cdk-overlay-pane']/div/div/div/mat-option[3]").click()
        self.driver.find_element(By.XPATH,
                            "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[5]/div/div[2]/app-dynamic-field/input").send_keys(
            "234589")
        self.driver.find_element(By.XPATH,
                            "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[6]/div/div[2]/app-dynamic-field/input").send_keys(
            "kishoresiva@gmail.com")
        self.driver.find_element(By.XPATH,
                            "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[7]/div/div[2]/app-dynamic-field/input").send_keys(
            "www.kishoresiva.com")
        self.driver.find_element(By.XPATH,
                            "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[8]/div/div[2]/app-dynamic-field/input").send_keys(
            "785612")
        self.driver.find_element(By.XPATH, "//*[@id='customform']/div[2]/button[1]").click()