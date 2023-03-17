from libs.searchpage import Applitool
from libs.createaccountpage import Createpage
from libs.siginaccountpage import signinpage
from playwright.sync_api import Page

class Testsiginapplitool:
    

    def test_signinpage(self,page: Page):
        search = Applitool(page)
        account = Createpage(page)
        sign = signinpage(page)
        search.navigate()
        search.gotowebsite()
        account.createaccout()
        sign.login()
