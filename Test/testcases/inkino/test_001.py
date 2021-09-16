from testcases.inkino.base_test_inkino import BaseTest
from pages.inkino_page import InkinoPage


class TestInkino(BaseTest):

    def test_001(self):
        home_page = InkinoPage(self.driver)
        home_page.search()
