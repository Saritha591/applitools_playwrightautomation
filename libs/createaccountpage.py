from playwright.sync_api import Page

class Createpage:

    firstname = "//input[@id='first-name']"
    lastname = "//input[@id='last-name']"
    email = "//input[@id='email']"
    password = "//input[@id='password']"
    company = "//input[@id='company']"
    country = "//select[@id='country']"
    create_button = "//button[normalize-space()='Create Account']"

    def __init__(self, page: Page):
        self.page = page

    def createaccout(self):
        self.page.locator(Createpage.firstname).fill("sari")
        self.page.locator(Createpage.lastname).fill("ritha")
        self.page.locator(Createpage.email).fill("sarithakatta08@gmail.com")
        self.page.locator(Createpage.password).fill("Saritha@123")
        self.page.locator(Createpage.company).fill("softworld")
        self.page.locator(Createpage.country).click()
        self.page.wait_for_timeout(4000)
        self.page.locator(Createpage.country).select_option("India")
        self.page.locator(Createpage.create_button).click()
        