from .base_page import BasePage
from playwright.sync_api import Locator

class LoadDelaysPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/loaddelay"
        self.title = self.page.locator("h3")
        self.button = self.page.get_by_role("button", name="Button Appearing After Delay")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def click_button(self) -> None:
        try:
            self.button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")