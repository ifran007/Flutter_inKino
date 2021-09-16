from testcases.inkino.base_test_inkino import BaseTest
from pages.inkino_page import InkinoPage
from appium import webdriver

class TestInkino(BaseTest):

    def test_002(self):
        home_page = InkinoPage(self.driver)
        home_page.location()
