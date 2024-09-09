from .base_page import BasePage
from playwright.sync_api import Locator

class DynamicIdPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "dynamicid"
        self.title = self.page.locator("h3")
        self.dynamicid_button = self.page.locator("button.btn.btn-primary")

    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title