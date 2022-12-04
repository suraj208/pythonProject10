import pytest
import logging


from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:



    def getActionMethod(self):
        action=ActionChains(self.driver)
        return action

    def getscrollPageUp(self):
        return self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight")

    def getscrollPageDown(self):
        return self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight")

    def getscrollIntoview(self,ele):
        return self.driver.execute_script("arguments[0].scrollIntoView()",ele)

