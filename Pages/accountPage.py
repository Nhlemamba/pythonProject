from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    name_xpath = "//select[contains(@id,'userSelect')]"
    selected_account_number = "//span[contains(@class,'fontBig ng-binding')]"

    transactions_xpath = "//button[contains(.,'Transactions')]"
    deposit_xpath = "//button[contains(.,'Deposit')]"
    withdraw_xpath = "//button[contains(.,'Withdrawl')]"
    deposit_textfield = "//input[@fdprocessedid='hglzzr']"
    main_deposit = "//button[@type='submit'][contains(.,'Deposit')]"
    withdraw_textfield = "//input[@fdprocessedid='tsn05']"
    main_withdraw = "//button[@type='submit'][contains(.,'Withdraw')]"
    logout_xpath = "//button[contains(.,'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def readAccountName(self):
        wait = WebDriverWait(self.driver, 10)
        readNames = wait.until(EC.visibility_of_element_located((By.XPATH, self.name_xpath)))
        readNames.find_element()

    def selectAccountNumber(self):
        wait = WebDriverWait(self.driver, 10)
        selectAccount = wait.until(EC.visibility_of_element_located((By.XPATH, self.selected_account_number)))
        selectAccount.is_selected()

    def clickTransactions(self):
        wait = WebDriverWait(self.driver, 10)
        clickOnTransactions = wait.until(EC.visibility_of_element_located((By.XPATH, self.transactions_xpath)))
        clickOnTransactions.click()

    def clickDeposit(self):
        wait = WebDriverWait(self.driver, 10)
        clickOnDeposit = wait.until(EC.visibility_of_element_located((By.XPATH, self.deposit_xpath)))
        clickOnDeposit.click()

    def clickWithdraw(self):
        wait = WebDriverWait(self.driver, 10)
        clickOnWithdraw = wait.until(EC.visibility_of_element_located((By.XPATH, self.withdraw_xpath)))

    def enterDepositOnField(self):
        wait = WebDriverWait(self.driver, 10)
        enterTheDeposit = wait.until(EC.visibility_of_element_located((By.XPATH, self.deposit_textfield)))
        enterTheDeposit.send_keys("1500")

    def clickMainDeposit(self):
        wait = WebDriverWait(self.driver, 10)
        clickMainDeposit = wait.until(EC.visibility_of_element_located((By.XPATH, self.main_deposit)))
        clickMainDeposit.click()

    def enterWithdrawalonField(self):
        wait = WebDriverWait(self.driver, 10)
        enterMainWithdrawal = wait.until(EC.visibility_of_element_located((By.XPATH, self.withdraw_textfield)))
        enterMainWithdrawal.send_keys()

    def clickMainWithdrawal(self):
        wait = WebDriverWait(self.driver, 10)
        clickMainWithdrawal = wait.until(EC.visibility_of_element_located((By.XPATH, self.main_withdraw)))
        clickMainWithdrawal.click()

    def clickLogout(self):
        wait = WebDriverWait(self.driver, 10)
        clickLogout = wait.until(EC.visibility_of_element_located((By.XPATH, self.logout_xpath)))
        clickLogout.click()





















