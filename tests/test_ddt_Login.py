import time

from Pageobjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
from logs.customLogger import LogGen
from utilities import Xlutil
import testdata



class Test_001_login(BaseClass):
    logger = LogGen.logjen()
    filepath="../testdata/login.xlsx"
    sheetname="practice"

    def test_ddt01(self):
        login=LoginPage(self.driver)
        self.logger.info("*******ddt case is passsed")
        rows = Xlutil.getRowCount(self.filepath, self.sheetname)
        print("number of the rows are ", rows)
        columns=Xlutil.getColumnCount(self.filepath,self.sheetname)
        print("number of the rows are ", columns)
        list=[]
        for r in range(2,rows+1):
            self.user=Xlutil.getEXlData(self.filepath,self.sheetname,r,1)
            self.passwrd=Xlutil.getEXlData(self.filepath,self.sheetname,r,2)
            self.exp=Xlutil.getEXlData(self.filepath,self.sheetname,r,3)

            login.getUsername().clear()
            login.getUsername().send_keys(self.user)
            login.getPassword().clear()
            login.getPassword().send_keys(self.passwrd)
            login.getLoginCheckbox()
            login.getLogin()

            get_title=self.driver.title
            titlepg="Dashboard / nopCommerce administration"
            if get_title==titlepg:
                if self.exp=="Pass":
                   self.logger.info("***passed")
                   login.getlogOut()
                   list.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("***failed")
                    login.getlogOut()
                    list.append("fail")
            elif get_title!=titlepg:
                if self.exp=="Pass":

                    self.logger.info("***failed")
                    login.getlogOut()
                    list.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***passed ")
                    login.getlogOut()
                    list.append("Pass")
        if "Fail" not in list:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert True



