import os

from ConfigTest.config import TestData
from SeleniumDriver.selenium_driver import Driver



class BaseTestClass:
    driver = None
    # if remove logs and screenshots dir of current test(in case of success test)
    remove_logs_dir = False

    def setup(self):
        pass

    def setup_method(self, method):
        self.remove_logs_dir = False
        test_name = method.__name__
        # make current test logs and screenshots dir
        # log_reports.create_test_log_dir(dir_name=test_name)
        self.init_driver()

    @staticmethod
    def get_base_url(default_url=TestData.BASE_URL):
        base_url = os.environ.get("BASE_URL", None)
        if base_url and "http" in base_url:
            return base_url
        else:
            return default_url

    def teardown_method(self):
        # stop webdriver for current test
        self.driver.driver.quit()
        # check if need to remove test in case of success test
        # if self.remove_logs_dir:
            # log_reports.remove_current_test_dir()

    def init_driver(self):
        if os.environ.get("REMOTE_SELENIUM", "False") == "True":
            self.driver = Driver(address="http://selenium:4444/wd/hub", browser_profile="chrome", remote=True)
        elif os.environ.get("HEADLESS", "False") == "True":
            self.driver = Driver(browser_profile="chrome", remote=False)
        else:
            self.driver = Driver(browser_profile="chrome", remote=False)

        # self.driver.driver.set_window_size(1920, 1080)
        self.driver.driver.maximize_window()
        self.driver.driver.get(self.get_base_url())

    def restart_driver(self):
        self.driver.driver.quit()
        self.init_driver()

