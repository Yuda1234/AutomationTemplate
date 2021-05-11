from selenium.common.exceptions import NoSuchElementException

from SeleniumDriver.ElementsTools.selenium_elements_tools import SeleniumElementsTools
from selenium.webdriver.support.ui import Select


class SelectElement(SeleniumElementsTools):
    selected_element = None

    def __init__(self, driver, wait_element, selector, timeout=30):
        SeleniumElementsTools.__init__(self, driver=driver, wait_element=wait_element)
        self.selected_element = Select(self.wait.wait_for_element_to_be_present(selector=selector, timeout=timeout))

    def find_select_element(self, selector):
        self.selected_element = Select(self.wait.wait_for_element_to_be_present(selector=selector, timeout=60))

    def choose_all_options(self):
        for option in self.selected_element.options:
            option.click()

    def choose_option_by_text(self, text, raise_exception=True):
        try:
            self.selected_element.select_by_visible_text(text=text)
        except NoSuchElementException as e:
            if raise_exception:
                raise e
            return False

    def get_all_options(self):
        return self.selected_element.options

    def get_all_options_text(self):
        options_text = []
        for option in self.selected_element.options:
            options_text.append(option.text.strip())
        print(options_text)
        return options_text
