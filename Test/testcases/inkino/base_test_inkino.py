import time
import unittest
from appium import webdriver
from data.data import Data
import unittest
from appium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.data = Data
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  # 'deviceName': 'emulator-5554',
                                  # 'platformVersion': '11',
                                  # 'deviceName': 'c9c5976',
                                  'automationName': 'UiAutomator2',
                                  'newCommandTimeout': '240',
                                  'appPackage': self.data.inkino_app_package,
                                  'appActivity': self.data.inkino_app_activity,
                                  # 'app': self.data.watermaniac,
                                  'appWaitPackage': self.data.inkino_app_package,
                                  'appWaitActivity': self.data.inkino_app_activity,
                                  'appWaitDuration': '30000',
                                  'noReset': True,
                                  'fullReset': False,
                                  # 'autoGrantPermissions': True,
                                  })

    # def test_0001(self):
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View").click()
        # time.sleep(15)
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[5]').click()
        # time.sleep(5)
        # self.driver.hide_keyboard()

    def tearDown(self):
        self.driver.quit()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
