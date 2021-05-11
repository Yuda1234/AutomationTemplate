from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from SeleniumDriver.ElementsTools.selenium_elements_tools import SeleniumElementsTools as Tools


class WaitForElementTools:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_present(self, selector, driver=None, timeout=60, raise_exception=True):
        driver = driver or self.driver
        try:
            element = WebDriverWait(driver=driver, timeout=timeout).until(ec.presence_of_element_located(selector))
            if not element:
                raise NoSuchElementException
            Tools.take_screenshot(driver=self.driver)
            return element
        except Exception as e:
            Tools.take_screenshot(driver=self.driver, filename='element_not_found')
            print("element {} not found exception: {}".format(selector, e))
            if raise_exception:
                raise e
            return False

    def wait_for_element_to_be_invisible(self, selector, driver=None, timeout=30):
        driver = driver or self.driver
        Tools.take_screenshot(driver=self.driver)
        visibility = WebDriverWait(driver=driver, timeout=timeout). \
            until(ec.invisibility_of_element_located(selector))
        Tools.take_screenshot(driver=self.driver)
        return visibility

    def wait_for_element_to_be_visible(self, selector, driver=None, timeout=30):
        driver = driver or self.driver
        Tools.take_screenshot(driver=self.driver)
        visibility = WebDriverWait(driver=driver, timeout=timeout). \
            until(ec.visibility_of_element_located(selector))
        Tools.take_screenshot(driver=self.driver)
        return visibility

    def wait_for_element_to_be_clickable(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        try:
            Tools.take_screenshot(driver=self.driver)
            element = WebDriverWait(driver=driver, timeout=timeout).until(ec.element_to_be_clickable(selector))
            if not element:
                raise NoSuchElementException
            Tools.take_screenshot(driver=self.driver)
            return element
        except Exception as e:
            Tools.take_screenshot(driver=self.driver, filename='element_not_found')
            print("element {} not found exception: {}".format(selector, e))
            if raise_exception:
                raise e
            return False

    def wait_for_elements_to_be_present(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        try:
            Tools.take_screenshot(driver=self.driver)
            elements = WebDriverWait(driver=driver, timeout=timeout). \
                until(ec.presence_of_all_elements_located(selector))
            if not elements:
                raise NoSuchElementException
            Tools.take_screenshot(driver=self.driver)
            return elements
        except Exception as e:
            Tools.take_screenshot(driver=self.driver, filename='element_not_found')
            print("element {} not found exception: {}".format(selector, e))
            if raise_exception:
                raise e
            return False

    def wait_for_element_contain_text(self, selector, driver=None, text_contain=None, timeout=30, raise_exception=True):
        by, selector_new = selector
        new_selector = (by, selector_new.format(text=text_contain))
        self.wait_for_elements_to_be_present(selector=new_selector, driver=driver, timeout=timeout,
                                             raise_exception=raise_exception)
