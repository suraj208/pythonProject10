from Pageobjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from logs.customLogger import LogGen
class Test_001_login(BaseClass):
    logger = LogGen.logjen()
    def test_01(self):

        login=LoginPage(self.driver)
        self.logger.info("*******case is passsed")
        login.getUsername().clear()
        login.getUsername().send_keys("admin@yourstore.com")
        login.getPassword().clear()
        login.getPassword().send_keys("admin")
        login.getLoginCheckbox()
        login.getLogin()
        pagetitle=self.driver.title

        if pagetitle=="Dashboard / nopCommerce administration":

            self.logger.info("************Login case is  PASSED***********")
            assert  True
        else:
            self.driver.get_screenshot_as_file(".\\Screenshots\\test001 is fail.png")

