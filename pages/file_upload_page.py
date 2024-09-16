from .base_page import BasePage
from playwright.sync_api import Locator

class FileUploadPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/upload"
        self.title = self.page.locator("h3")
        self.frame = self.page.frame_locator("iframe")
        self.file_input = self.frame.locator("input[type='file']")
        self.file_info = self.frame.locator(".file-info")

    def navigate(self) -> None:
        super().navigate(self.path)
