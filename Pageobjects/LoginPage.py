
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    usernameid=(By.ID,'Email')
    password_id=(By.ID,'Password')
    rememberme_id=(By.ID,'RememberMe')
    login_button_id=(By.XPATH,'//button[@type="submit"]')
    logout_xpath=(By.XPATH,'//a[@href="/logout"]')

    def getUsername(self):
        return self.driver.find_element(*LoginPage.usernameid)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password_id)

    def getLoginCheckbox(self):
        return self.driver.find_element(*LoginPage.rememberme_id).click()

    def getLogin(self):
        return self.driver.find_element(*LoginPage.login_button_id).click()

    def getlogOut(self):
        return self.driver.find_element(*LoginPage.logout_xpath).click()