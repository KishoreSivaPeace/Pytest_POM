import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from Locators.Login_Logout import Login_out_Locators
from LoginOut_Pages.Login import LoginPage
from LoginOut_Pages.logout import LogOut
from Job_Pages.Add_Job import AddJob
from Job_Pages.Add_Job_Item import JobItem
from Job_Pages.Add_Appointment import AddAppointment
from Job_Pages.Add_Task import AddTask
from Job_Pages.Job_Copy_Edit_Delete import JobCopyEditDelete
from Job_Pages.Add_Payments import AddPayment
from Job_Pages.CheckList import Checklist
from Job_Pages.Add_Notes import AddNotes
from Job_Pages.Add_Further_info import AddFurtherInfo
from Job_Pages.Alternative_Delivery_Address import AlternativeDeliveryAddress


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # cls.options = webdriver.EdgeOptions()
        # cls.options.add_experimental_option("detach", True)
        # cls.driver = webdriver.Edge(options=cls.options, service=EdgeService(EdgeChromiumDriverManager().install()))
        # cls.driver.maximize_window()
        # cls.driver.implicitly_wait(10)
        cls.options = webdriver.ChromeOptions()
        cls.options.add_experimental_option("detach", True)
        cls.prefs = {"profile.default_content_setting_values.notifications": 2}
        cls.options.add_experimental_option("prefs", cls.prefs)
        cls.driver = webdriver.Chrome(options=cls.options, service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_01_login(self):
        driver = self.driver
        driver.get(Login_out_Locators.final_testing)
        LoginPage(driver).login_module()

    def test_02_add_job(self):
        driver = self.driver
        AddJob(driver).new_add_job()

    # @pytest.mark.skip
    def test_03_add_job_item(self):
        driver = self.driver
        JobItem(driver).new_job_item()

    def test_04_add_appointment(self):
        driver = self.driver
        AddAppointment(driver).add_appointment()

    def test_05_add_task(self):
        driver = self.driver
        AddTask(driver).add_task()

    # @pytest.mark.skip
    def test_06_job_copy_edit_delete(self):
        driver = self.driver
        JobCopyEditDelete(driver).job_copy_edit_delete()

    def test_07_add_payment(self):
        driver = self.driver
        AddPayment(driver).add_payment()

    def test_08_checklist(self):
        driver = self.driver
        Checklist(driver).checklist()

    def test_09_add_notes(self):
        driver = self.driver
        AddNotes(driver).add_notes()

    def test_10_add_further_info(self):
        driver = self.driver
        AddFurtherInfo(driver).add_further_info()

    def test_11_alternative_delivery_address(self):
        driver = self.driver
        AlternativeDeliveryAddress(driver).alternative_delivery_address()

    def test_12_log_out(self):
        driver = self.driver
        LogOut(driver).logout()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")
