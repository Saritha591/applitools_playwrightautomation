from libs.searchpage import Applitool
from libs.createaccountpage import Createpage
from playwright.sync_api import Page


class Testcreateappliaccount:

    def test_createaccountpage(self, page: Page):
        search = Applitool(page)
        account = Createpage(page)
        search.navigate()
        search.gotowebsite()
        account.createaccout()
