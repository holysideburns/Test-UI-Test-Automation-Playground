"""
Script Name: test_mouse_over_page.py
Description: This script tests the "Mouse Over" page at http://www.uitestingplayground.com/mouseover.
Challenge: Click a link that changes to another element in the DOM on mouseover.
"""

import pytest
from playwright.sync_api import expect
from pages.mouse_over_page import MouseOverPage

@pytest.fixture
def mouse_over_page(page) -> MouseOverPage:
    mouse_over_page = MouseOverPage(page)
    mouse_over_page.navigate()
    return mouse_over_page

@pytest.mark.mouseover
def test_mouse_over_page_title(mouse_over_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Mouse Over' page,
        When the page is loaded,
        Then the page title should be 'Mouse Over'.
    """
    expect(mouse_over_page.title).to_have_text("Mouse Over")

@pytest.mark.mouseover
def test_dynamic_link_click(mouse_over_page) -> None:
    """
    Test Scenario: Test Dynamic Link Click
        Given the user navigates to the 'Mouse Over' page,
        When the user tries to click the link "Click me" two times,
        Then the counter should say "The link clicked 2 times".
    """
    mouse_over_page.click_link()
    mouse_over_page.click_link()
    expect(mouse_over_page.click_count).to_have_text("2")
