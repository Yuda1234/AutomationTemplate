import os
from pathlib import Path
from time import ctime, time, sleep
from selenium.webdriver.common.keys import Keys


class SeleniumElementsTools:

    def __init__(self, driver, wait_element):
        self.driver = driver
        self.wait = wait_element

    def wait_and_click(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_clickable(selector=selector, driver=driver, timeout=timeout,
                                                             raise_exception=raise_exception)
        self.take_screenshot(driver=self.driver)
        if element:
            return element.click()

    def wait_and_click_by_enter(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_clickable(selector=selector, driver=driver, timeout=timeout,
                                                             raise_exception=raise_exception)
        self.take_screenshot(driver=self.driver)
        if element:
            return element.send_keys(Keys.ENTER)


    def get_text_from_element(self, selector, driver=None, timeout=30):
        driver = driver or self.driver
        element_text = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout).text
        self.take_screenshot(driver=self.driver)
        return element_text

    def set_text(self, selector, text, driver=None, timeout=30):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout)
        element.send_keys(text)
        self.take_screenshot(driver=self.driver)

    def clear_and_set_text(self, selector, text, driver=None, timeout=30):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout)
        element.clear()
        element.send_keys(text)
        self.take_screenshot(driver=self.driver)

    def refresh_the_page(self, driver=None):
        driver = driver or self.driver
        self.take_screenshot(driver=self.driver)
        self.driver.refresh()

    def clear_value(self, selector, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout,
                                                           raise_exception=raise_exception)
        value = self.wait_for_element_and_get_attribute(selector=selector, attribute="value", driver=driver,
                                                        timeout=timeout, raise_exception=raise_exception)
        for character in range(len(value)):
            element.send_keys(Keys.BACK_SPACE)
        self.take_screenshot(driver=self.driver)

    def clear_value_and_set_text(self, selector, text, driver=None, timeout=30, raise_exception=True):
        self.clear_value(selector=selector, driver=driver, timeout=timeout, raise_exception=raise_exception)
        self.set_text(selector=selector, text=text, driver=driver, timeout=timeout)

    @staticmethod
    def take_screenshot(driver, filename=None):
        pic_path = Path(os.environ.get('CURRENT_LOGS_DIR', '_'.join(ctime().replace(':', '.').split())))
        filename = pic_path / "{}.png".format(filename) if filename else pic_path / "{}.png". \
            format('_'.join(ctime().replace(':', '.').split()))
        driver.save_screenshot(filename=str(filename))

    def make_list_of_strings_from_elements(self, selector, driver=None, timeout=30):
        driver = driver or self.driver
        elements = self.wait.wait_for_elements_to_be_present(selector=selector, driver=driver, timeout=timeout)
        elements_text = []
        for element in elements:
            elements_text.append(element.text)
        return elements_text

    def element_contain_text(self, text, selector, driver=None, timeout=30):
        driver = driver or self.driver
        if text in self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout).text:
            self.take_screenshot(driver=self.driver)
            return True
        return False

    def wait_and_js_click(self, selector, driver=None, timeout=60, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_clickable(selector=selector, driver=driver, timeout=timeout,
                                                             raise_exception=raise_exception)
        self.take_screenshot(driver=self.driver)
        if element:
            return driver.execute_script("arguments[0].click();", element)

    def wait_for_element_and_get_attribute(self, selector, attribute, driver=None, timeout=60, raise_exception=True):
        driver = driver or self.driver
        element = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout,
                                                           raise_exception=raise_exception)
        self.take_screenshot(driver=self.driver)
        if element:
            try:
                return element.get_attribute(attribute)
            except Exception as e:
                if raise_exception:
                    raise e
                else:
                    return False
        return False

    def click_on_web_element_by_js(self, web_element, driver=None):
        driver = driver or self.driver

        self.take_screenshot(driver=self.driver)
        return driver.execute_script("arguments[0].click();", web_element)

    def wait_and_get_attribute_when_present(self, selector, attribute, driver=None, timeout=30, raise_exception=True):
        driver = driver or self.driver
        start_time = time()
        while start_time + timeout > time():
            element = self.wait_for_element_and_get_attribute(selector=selector, attribute=attribute, driver=driver,
                                                              timeout=timeout, raise_exception=False)
            if element:
                self.take_screenshot(driver=self.driver)
                return element
            else:
                sleep(.1)
        if raise_exception:
            raise "element {} not coming from data base or element not found".format(selector)
        return False

    def switch_window(self, window_position, driver=None):
        driver = driver or self.driver
        self.take_screenshot(driver=self.driver)
        driver.switch_to_window(driver.window_handles[window_position])

    # work only with appium driver not selenium
    def scroll_from_element_to_element_by_selector(self, from_element_selector=None, to_element_selector=None):
        # TODO make this func for selenium
        pass

    # work only with appium driver not selenium
    def scroll_from_element_to_element(self, from_element=None, to_element=None):
        # TODO make this func for selenium
        pass

    # noinspection PyBroadException
    def scroll_to_element(self, selector, from_x=100, from_y=900, to_x=100, to_y=400):
        # TODO make this func for selenium
        pass

    def scroll_to_end_of_page(self, from_x=100, from_y=900, to_x=100, to_y=400):
        # TODO make this func for selenium
        pass
