from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
import time
sys.path.append("C://unittest_pom_html_reports")

import Pages.LoginPage


class LoginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def Test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.loginButton()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../Reports"))





