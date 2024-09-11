from .base_page import BasePage
from playwright.sync_api import Locator

class VerifyTextPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/verifytext"
        self.title = self.page.locator("h3")
        self.welcome_message = self.page.locator("//span[normalize-space(.)='Welcome UserName!']")

    def navigate(self) -> None:
        super().navigate(self.path)
