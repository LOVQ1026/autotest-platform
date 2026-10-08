from playwright.sync_api import Page

class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL, wait_until="domcontentloaded", timeout=60000)
        return self

    def login(self, username: str, password: str):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()
        return self

    def error_message(self):
        return self.page.locator("[data-test='error']")
