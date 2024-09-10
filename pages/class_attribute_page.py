from .base_page import BasePage
from playwright.sync_api import Locator

class ClassAttributePage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/classattr"
        self.title = self.page.locator("h3")
        self.blue_button = self.page.locator(".btn-primary")
        
    def navigate(self) -> None:
        super().navigate(self.path)
    
    def click_blue_button(self) -> None:
        def on_dialog(dialog):
            dialog.accept()

        self.page.on('dialog', on_dialog)

        try:
            self.blue_button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")
        finally:
            self.page.remove_listener('dialog', on_dialog)

    
