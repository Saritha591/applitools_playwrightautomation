from playwright.sync_api import Page


class signinpage:

    sigin = "//a[normalize-space()='Sign in.']"

    def __init__(self, page: Page):
        self.page = page

    def login(self):
        self.page.locator("//a[normalize-space()='Sign in.']").click()
