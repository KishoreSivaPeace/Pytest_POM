import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from Locators.Login_Logout import Login_out_Locators


# @pytest.fixture()
# def error_screenshot(request, chrome_driver):
#     yield
#     item = request.node
#     driver = chrome_driver
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # self.company_name_id = "//*[@id='companyname']"
        # self.user_name_id = "#username"
        # self.password_id = "#password"
        # self.login_button_id = "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[""4" \
        #                        "]/button[1]"

    # def enter_companyname(self, companyname):
    #     self.driver.find_element(By.XPATH, self.company_name_id).send_keys(companyname)
    # def enter_username(self, username):
    #     self.driver.find_element(By.CSS_SELECTOR, self.user_name_id).send_keys(username)
    # def enter_password(self, password):
    #     self.driver.find_element(By.CSS_SELECTOR, self.password_id).send_keys(password)
    # def click_login(self):
    #     self.driver.find_element(By.XPATH, self.login_button_id).click()

    # @pytest.mark.usefixtures("error_screenshot")
    def login_module(self):
        self.driver.find_element(By.XPATH, Login_out_Locators.company_name_id).send_keys(
            Login_out_Locators.company_name)
        self.driver.find_element(By.CSS_SELECTOR, Login_out_Locators.user_name_id).send_keys(
            Login_out_Locators.user_name)
        self.driver.find_element(By.CSS_SELECTOR, Login_out_Locators.password_id).send_keys(Login_out_Locators.password)
        self.driver.find_element(By.XPATH, Login_out_Locators.login_button_id).click()
        allure.attach(self.driver.get_screenshot_as_png(),name="Error", attachment_type=AttachmentType.PNG)

    # def login_module(self, companyname,username,password):
    #     self.driver.find_element(By.XPATH, self.company_name_id).send_keys(companyname)
    #     self.driver.find_element(By.CSS_SELECTOR, self.user_name_id).send_keys(username)
    #     self.driver.find_element(By.CSS_SELECTOR, self.password_id).send_keys(password)
    #     self.driver.find_element(By.XPATH, self.login_button_id).click()
