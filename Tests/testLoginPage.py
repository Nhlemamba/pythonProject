import time
import allure
import pytest
from allure_commons.types import AttachmentType
from Pages.loginPage import LoginPage
from Pages.accountPage import AccountPage
from Utilities.readProperties_LoginDetails import ReadLoginConfig

class Login_Test:
    Way2Automation_URL = ReadLoginConfig.getWay2Automation_URL

    @pytest.mark.login
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login_Test(self, setup):
        self.driver = setup
        self.driver.get(self.Way2Automation_URL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickCustomerLogin()
        self.login.clickSelectUser()
        self.login.selectUserAccount()

        allure.attach(self.driver.get_screenshot_as_png(), name="Login_Page_Screenshot", attachment_type=AttachmentType)
        self.login.clickLoginButton()

        self.account = AccountPage(self.driver)
        self.account.selectAccountNumber()
        self.account.clickDeposit()
        self.account.enterDepositOnField()
        self.account.clickMainDeposit()
        self.account.clickLogout()

    time.sleep(2)









