"""
Script Name: test_scrollbars_page.py
Description: This script tests the "Scrollbars" page at http://www.uitestingplayground.com/scrollbars.
Challenge: Scroll the button into a visible area before clicking.
"""
import pytest
from playwright.sync_api import expect
from pages.scrollbars_page import Scrollbars


@pytest.fixture
def scrollbars_page(page) -> Scrollbars:
    scrollbars_page = Scrollbars(page)
    scrollbars_page.navigate()
    return scrollbars_page

@pytest.mark.scrollbars
def test_scrollbars_page_title(scrollbars_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Scrollbars' page,
        When the page is loaded,
        Then the page title should be 'Scrollbars'.
    """
    expect(scrollbars_page.title).to_have_text("Scrollbars")

@pytest.mark.scrollbars
def test_scrollable_button(scrollbars_page) -> None:
    """
    Test Scenario: Test Scrollable Button
        Given the user is on the 'Scrollable' page,
        When they scroll the page so the button is visible,
        Then the button should be clickable.
    """
    scrollbars_page.scroll_to_button()
    scrollbars_page.click_button()
