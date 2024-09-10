from .base_page import BasePage
from playwright.sync_api import Locator

class ClientSideDelayPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/clientdelay"
        self.title = self.page.locator("h3")
        self.button = self.page.locator("#ajaxButton")
        self.message = self.page.get_by_text("Data calculated on the client side.")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def click_button(self) -> None:
        try:
            self.button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")
