import time

import requests
from selenium import webdriver
from SeleniumDriver.ElementsTools.selenium_elements_tools import SeleniumElementsTools
from SeleniumDriver.wait_for_elements_tools import WaitForElementTools


class Driver:

    def __init__(self, address='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None,
                 remote=True):

        if browser_profile == "chrome" and not remote:
            self.driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
            self.wait = WaitForElementTools(self.driver)
            self.tools = SeleniumElementsTools(self.driver, self.wait)

        elif browser_profile == "firefox" and not remote:
            self.driver = webdriver.Firefox()
            self.wait = WaitForElementTools(self.driver)
            self.tools = SeleniumElementsTools(self.driver, self.wait)

        elif browser_profile and remote:
            if not address:
                address = 'http://127.0.0.1:4444/wd/hub'

            self.check_health_selenium_remote_server(server_url=address)
            self.driver = webdriver.Remote(command_executor=address, desired_capabilities=desired_capabilities)
            self.wait = WaitForElementTools(self.driver)
            self.tools = SeleniumElementsTools(self.driver, self.wait)

    @staticmethod
    def check_health_selenium_remote_server(server_url="http://localhost:4444/wd/hub", timeout=120):

        start_time = time.time()
        while start_time + timeout > time.time():
            try:
                print("wait for selenium server to be ready")
                selenium_server_response = requests.get(server_url+"/status")
                if selenium_server_response.json()['value']['ready']:
                    print("selenium server is ready")
                    return True
                time.sleep(1)
                print("selenium server is not ready yet")
            except Exception as e:
                print("selenium server is not ready yet")
                time.sleep(1)
        raise RuntimeError(f"selenium server is not ready after {timeout}")
