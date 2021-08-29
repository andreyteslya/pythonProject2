from playwright.sync_api import Playwright
from .test_cases import TestCases


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url
        self.test_cases = TestCases(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
           self.page.goto (self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def navigate_to(self, menu: str):
        self.page.click(f"css=header >> text=\"{menu}\"")

    def login(self, login: str, password: str):
        self.page.fill("input[name=\"username\"]", login)
        self.page.fill("input[name=\"password\"]", password)
        self.page.click("text=Login")

    def create_test(self, test_name: str, test_description: str):
        self.page.click("text=Create new test")
        self.page.fill("input[name=\"name\"]", test_name)
        self.page.fill("textarea[name=\"description\"]", test_description)
        self.page.click("input:has-text(\"Create\")")

    # def open_test(self):
    #     self.page.click("text=Test Cases")

    # def check_test_exists(self, test_name: str):
    #     return self.page.query_selector(f'css=tr >> text=\"{test_name}\"') is not None
    #
    # def delete_test_by_name(self, test_name: str):
    #     row = self.page.query_selector(f'*css=tr >> text=\"{test_name}\"')
    #     row.query_selector('.deleteBtn').click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
        # self.page.goto("http://127.0.0.1:8000/login/?next=/")