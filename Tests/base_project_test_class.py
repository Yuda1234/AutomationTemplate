from SeleniumDriver.base_test_class import BaseTestClass
from import_pages import *


class BaseProjectTestClass(BaseTestClass):

    def search_in_google(self):
        self.driver.tools.set_text(GooglePage.SEARCH_INPUT, TestData.SOME_TEXT)