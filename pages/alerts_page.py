from .base_page import BasePage
from playwright.sync_api import Locator

class AlertsPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/alerts"
        self.title = self.page.locator('h3')
        self.alert_button = self.page.locator("#alertButton")
        self.confirm_button = self.page.locator("#confirmButton")
        self.prompt_button = self.page.locator("#promptButton")
        
    def navigate(self) -> None:
        super().navigate(self.path)

    def click_button(self) -> None:
        try:
            self.button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")