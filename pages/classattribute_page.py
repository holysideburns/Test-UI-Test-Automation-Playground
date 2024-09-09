from .base_page import BasePage
from playwright.sync_api import Locator

class ClassAttributePage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "classattr"
        self.title = self.page.locator("h3")
        self.blue_button = self.page.locator(".btn-primary")
        
    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title
    
    def click_blue_button(self) -> None:
        # Define a callback function to handle the alert
        def on_dialog(dialog):
            dialog.accept()  # Click 'OK' on the alert

        # Register the dialog handler
        self.page.on('dialog', on_dialog)

        try:
            # Click the button that triggers the alert
            self.blue_button.click()
            assert self.page.is_visible("h3"), "Failed to close the alert, interaction with the page blocked"
        finally:
            # Ensure the dialog handler is cleaned up after use
            self.page.remove_listener('dialog', on_dialog)