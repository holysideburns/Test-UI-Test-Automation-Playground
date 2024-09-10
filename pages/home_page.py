from .base_page import BasePage
from playwright.sync_api import Locator

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.path = "/"
        self.alternate_path = "/home"
        self.title = self.page.locator("h1")

    def navigate(self) -> None:
        super().navigate(self.path)

    def navigate_alternate_path(self) -> None:
        super().navigate(self.alternate_path)