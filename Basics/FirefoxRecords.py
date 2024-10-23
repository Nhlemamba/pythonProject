import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.way2automation.com/angularjs-protractor/webtables/")
faker = Faker()

nameText = driver.find_element(By.XPATH,"//span[contains(.,'First Name')]").text
assert nameText == "First Name"

surnameText = driver.find_element(By.XPATH,"//span[contains(.,'Last Name')]").text
assert surnameText == "Last Name"

emailText = driver.find_element(By.XPATH,"//span[contains(.,'E-mail')]").text
assert emailText =="E-mail"
time.sleep(1)
driver.save_screenshot("Screenshot/screenshots/verify_existing_file.png")
count = 0
for _ in range(2):
    count +=1
    driver.find_element(By.XPATH,"//button[contains(.,'Add User')]").click()

    userPage = driver.find_element(By.XPATH,"//h3[contains(.,'Add User')]").text
    assert userPage == "Add User"

    enterName =faker.name()
    enterSurname =faker.last_name()
    password = faker.password()
    email = faker.email()

    driver.find_element(By.XPATH,"//input[@name='FirstName']").clear()
    driver.find_element(By.XPATH,"//input[@name='FirstName']").send_keys(enterName)
    driver.find_element(By.XPATH,"//input[@name='LastName']").clear()
    driver.find_element(By.XPATH,"//input[@name='LastName']").send_keys(enterSurname)
    time.sleep(1)
    enterUserName = enterName + enterSurname + "_"+ str(faker.random_digit_not_null())
    print(enterUserName)

    driver.find_element(By.XPATH,"//input[@name='UserName']").clear()
    driver.find_element(By.XPATH,"//input[@name='UserName']").send_keys(enterUserName)
    driver.find_element(By.XPATH,"//input[@name='Password']").send_keys("MySecret")

    select = Select(driver.find_element(By.XPATH,"//select[contains(@name,'RoleId')]"))
    select.select_by_index(2)

    driver.find_element(By.XPATH,"//input[@type='email']").clear()
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Mobilephone']").clear()
    driver.find_element(By.XPATH, "//input[@name='Mobilephone']").send_keys("0897666645")
    time.sleep(1)
    driver.save_screenshot("save_entered_details.png")
    driver.find_element(By.XPATH,"//button[contains(.,'Save')]").click()
    time.sleep(1)

    verifyUserName = driver.find_element(By.XPATH,"(//td[@ng-hide='column.noList'])[3]").text
    assert verifyUserName == enterUserName
    driver.save_screenshot("Screenshot/verify_new_entered_record"+enterUserName+".png")
time.sleep(1)




