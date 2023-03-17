from playwright.sync_api import Page


class Applitool:

    link = "//h3[normalize-space()='Applitools: AI-Powered Test Automation Platform']"
    search = "//input[@title='Search']"
    getstarted = "//a[@class='btn']"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.google.com")

    def gotowebsite(self):
        self.page.locator(Applitool.search).fill("applitool")
        self.page.locator(Applitool.search).press("Enter")
        self.page.locator(Applitool.link).click()
        self.page.locator(Applitool.getstarted).click()
