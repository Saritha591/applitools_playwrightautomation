from libs.searchpage import Applitool
from playwright.sync_api import Page


class Testsearchapplitool:

    def test_applisearchpage(self, page: Page):
        search = Applitool(page)
        search.navigate()
        search.gotowebsite()
