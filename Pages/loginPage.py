from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    customer_Login_xpath = "//button[contains(.,'Customer Login')]"
    user_select_dropdown_xpath = "//span[contains(@class,'fontBig ng-binding')]"
    user_Account_xpath = "//select[contains(@id,'userSelect')]"
    login_button_xpath = "//button[contains(.,'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLogin(self):
        wait = WebDriverWait(self.driver, 10)
        customerLoginElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.customer_Login_xpath)))
        customerLoginElement.find_element().click()
    def clickSelectUser(self):
        wait = WebDriverWait(self.driver, 10)
        userSelection = wait.until(EC.visibility_of_element_located((By.XPATH, self.user_select_dropdown_xpath)))
        userSelection.find_element().click()

    def selectUserAccount(self):
        wait = WebDriverWait(self.driver, 10)
        select = Select(self.driver.find_element((By.XPATH, self.user_Account_xpath)))
        select.select_by_index(2)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        loginElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.login_button_xpath)))
        loginElement.find_element().click()
