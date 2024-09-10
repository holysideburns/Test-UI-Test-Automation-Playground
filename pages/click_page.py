from .base_page import BasePage
from playwright.sync_api import Locator

class ClickPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/click"
        self.title = self.page.locator("h3")
        self.button = self.page.locator("#badButton")

    def navigate(self) -> None:
        super().navigate(self.path)

    def click_button(self) -> None:
        self.button.click()