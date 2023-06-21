import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from Locators.Login_Logout import Login_out_Locators
from LoginOut_Pages.Login import LoginPage
from LoginOut_Pages.logout import LogOut
from Contact_Pages.Add_Contact import AddContact
from Contact_Pages.Add_Job_from_Contact import AddJobFromContact
from Contact_Pages.Company_Tab import CompanyTab
from Contact_Pages.Pricing_Tab import PricingTab
from Contact_Pages.Payment_Info_Tab import PaymentInfoTab
from Contact_Pages.Commission_Tab import CommissionTab
from Contact_Pages.Document_Tab import DocumentTab
from Contact_Pages.Product_Config_Tab import ProductConfigTab
from Contact_Pages.Online_Portal_tab import OnlinePortalTab
from Contact_Pages.FTP_Tab import FTPTab
from Contact_Pages.Add_Task_from_3dots import AddTaskFrom3Dots
from Contact_Pages.Add_Appointment_from_3dots import AddAppointmentFrom3dots
from Contact_Pages.Add_Task_from_Contact_Tab import AddTaskFromContactTab
from Contact_Pages.Add_Appointment_from_Contact_Tab import AddAppointmentFromContactTab
from Contact_Pages.Add_Contact_from_Contact_Tab import AddContactFromContactTab
from Contact_Pages.Delete_Contact import DeleteContact
from Job_Pages.Add_Job_Item import JobItem
from Job_Pages.Add_Appointment import AddAppointment
from Job_Pages.Add_Task import AddTask
from Job_Pages.Job_Copy_Edit_Delete import JobCopyEditDelete
from Job_Pages.Add_Payments import AddPayment
from Job_Pages.CheckList import Checklist
from Job_Pages.Add_Notes import AddNotes
from Job_Pages.Add_Further_info import AddFurtherInfo
from Job_Pages.Alternative_Delivery_Address import AlternativeDeliveryAddress


class Contact_Module(unittest.TestCase):

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

    def test_02_add_contact(self):
        driver = self.driver
        AddContact(driver).add_contact()

    def test_03_add_job_from_contact(self):
        driver = self.driver
        AddJobFromContact(driver).add_job_from_contact()

    # @pytest.mark.skip
    def test_04_add_job_item(self):
        driver = self.driver
        JobItem(driver).new_job_item()

    def test_05_add_appointment(self):
        driver = self.driver
        AddAppointment(driver).add_appointment()

    def test_06_add_task(self):
        driver = self.driver
        AddTask(driver).add_task()

    # @pytest.mark.skip
    def test_07_job_copy_edit_delete(self):
        driver = self.driver
        JobCopyEditDelete(driver).job_copy_edit_delete()

    def test_08_add_payment(self):
        driver = self.driver
        AddPayment(driver).add_payment()

    def test_09_checklist(self):
        driver = self.driver
        Checklist(driver).checklist()

    def test_10_add_notes(self):
        driver = self.driver
        AddNotes(driver).add_notes()

    def test_11_add_further_info(self):
        driver = self.driver
        AddFurtherInfo(driver).add_further_info()

    def test_12_alternative_delivery_address(self):
        driver = self.driver
        AlternativeDeliveryAddress(driver).alternative_delivery_address()

    def test_13_company_tab(self):
        driver = self.driver
        CompanyTab(driver).company_tab()

    def test_14_pricing_tab(self):
        driver = self.driver
        PricingTab(driver).pricing_tab()

    def test_15_payment_tab(self):
        driver = self.driver
        PaymentInfoTab(driver).payment_info_tab()

    def test_16_commission_tab(self):
        driver = self.driver
        CommissionTab(driver).commission_tab()

    def test_17_document_tab(self):
        driver = self.driver
        DocumentTab(driver).document_tab()

    def test_18_product_config_tab(self):
        driver = self.driver
        ProductConfigTab(driver).product_config_tab()

    def test_19_online_portal_tab(self):
        driver = self.driver
        OnlinePortalTab(driver).online_portal_tab()

    def test_20_ftp_tab(self):
        driver = self.driver
        FTPTab(driver).ftp_tab()

    def test_21_add_task_from_3dots(self):
        driver = self.driver
        AddTaskFrom3Dots(driver).add_task_from_3dots()

    def test_22_add_appointment_from_3dots(self):
        driver = self.driver
        AddAppointmentFrom3dots(driver).add_appointment_from_3dots()

    @pytest.mark.skip
    def test_23_add_task_from_contact_tab(self):
        driver = self.driver
        AddTaskFromContactTab(driver).add_task_from_contact_tab()

    @pytest.mark.skip
    def test_24_add_appointment_from_contact_tab(self):
        driver = self.driver
        AddAppointmentFromContactTab(driver).add_appointment_from_contact_tab()

    @pytest.mark.skip
    def test_25_add_contact_from_contact_tab(self):
        driver = self.driver
        AddContactFromContactTab(driver).add_contact_from_contact_tab()

    @pytest.mark.skip
    def test_26_delete_contacts(self):
        driver = self.driver
        DeleteContact(driver).delete_contact()

    def test_27_log_out(self):
        driver = self.driver
        LogOut(driver).logout()

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.close()
        # cls.driver.quit()
        print("Test Completed")
