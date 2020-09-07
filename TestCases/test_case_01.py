import sys
sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from TestCases.base_test import BaseTest
from TestData.TestData import TestData

class HerokuAppLogin1(BaseTest):
    """A sample test class to show how page object works"""
    @classmethod
    def setUp(self):
        super().setUp(TestData.BROWSER)

    @classmethod
    def tearDown(self):
         super().tearDown()

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)

if __name__ == "__main__":
    unittest.main()
