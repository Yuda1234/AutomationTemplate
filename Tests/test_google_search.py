from Tests.base_project_test_class import *


class TestLogin(BaseProjectTestClass):

    def test_login(self):
        self.search_in_google()
        # self.driver.wait.wait_for_element_to_be_visible()
        # self.remove_logs_dir = True