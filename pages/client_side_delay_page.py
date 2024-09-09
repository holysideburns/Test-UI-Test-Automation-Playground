from .base_page import BasePage
from playwright.sync_api import Locator

class ClientSideDelay(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "clientdelay"
        self.title = self.page.locator("h3")
        self.javascript_button = self.page.locator("#ajaxButton")
        self.javascript_message = self.page.get_by_text("Data calculated on the client side.")

    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title
    
    def click_javascript_button(self) -> None:
        self.javascript_button.click()

    def get_javascript_message(self) -> Locator:
        return self.javascript_message