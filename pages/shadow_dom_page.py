from .base_page import BasePage
from playwright.sync_api import Locator

class ShadowDomPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/shadowdom"
        self.title = self.page.locator('h3')
        self.guid_field = self.page.locator("#editField")
        self.generate_button = self.page.locator("#buttonGenerate")
        self.copy_button = self.page.locator("#buttonCopy")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def click_button(self) -> None:
        try:
            self.generate_button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")