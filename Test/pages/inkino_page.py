from data.locators import InkinoPageLocator
from pages.base_page import BasePage
from data.data import *
from time import sleep


class InkinoPage(BasePage):

    def __init__(self, driver):
        self.locator = InkinoPageLocator
        self.data = Data
        self.inkino = Inkino
        super().__init__(driver)

    def search(self):
        self.click(self.locator.search)
        self.driver.hide_keyboard()
        sleep(5)
        self.send_data(self.locator.search_movies)
        sleep(5)

    def location(self):
        self.click(self.locator.location)
        sleep(5)
        self.click(self.locator.paakapunkiseutu)
        sleep(5)

    def coming_soon(self):
        self.click(self.locator.coming_soon)

    def inkino(self):
        self.find_elements(self.locator.location)


