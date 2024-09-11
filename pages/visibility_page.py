from .base_page import BasePage
from playwright.sync_api import Locator

class VisibilityPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/visibility"
        self.title = self.page.locator("h3")
        self.hide_button = self.page.locator("#hideButton")                               
        self.removed_button = self.page.locator("#removedButton")
        self.zero_width_button = self.page.locator("#zeroWidthButton")
        self.overlapped_button = self.page.locator("#overlappedButton")
        self.overlapping_layer = self.page.locator("#hidingLayer")
        self.transparent_button = self.page.locator("#transparentButton")
        self.invisible_button = self.page.locator("#invisibleButton")
        self.not_displayed_button = self.page.locator("#notdisplayedButton")
        self.offscreen_button = self.page.locator("#offscreenButton")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def is_overlapping(self, box1, box2) -> bool:
        return not (
        box1['x'] + box1['width'] <= box2['x'] or
        box2['x'] + box2['width'] <= box1['x'] or
        box1['y'] + box1['height'] <= box2['y'] or
        box2['y'] + box2['height'] <= box1['y']
    )

    def get_opacity(self, element: Locator) -> str:
        return element.evaluate("element => window.getComputedStyle(element).opacity")