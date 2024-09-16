from .base_page import BasePage
from playwright.sync_api import Locator

class OverlappedElementPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/overlapped"
        self.title = self.page.locator("h3")
        self.name_input = self.page.locator("#name")

    def navigate(self) -> None:
        super().navigate(self.path)