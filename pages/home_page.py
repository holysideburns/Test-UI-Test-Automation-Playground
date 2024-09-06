from .base_page import BasePage
from playwright.sync_api import Locator

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.path = ""
        self.title = self.page.locator("h1")

    def navigate(self):
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title