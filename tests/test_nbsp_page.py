"""
Script Name: test_nbsp_page.py
Description: This script tests the "Click" page at http://www.uitestingplayground.com/nbsp.
Challenge: Ensure that the button can be clicked eventhough it has a non-breaking space in its text.
"""

import pytest
from playwright.sync_api import expect
from pages.nbsp_page import NbspPage

@pytest.fixture
def nbsp_page(page) -> NbspPage:
    nbsp_page = NbspPage(page)
    nbsp_page.navigate()
    return nbsp_page

@pytest.mark.nbsp
def test_nbsp_page_title(nbsp_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Non-Breaking Space' page,
        When the page is loaded,
        Then the page title should be 'Non-Breaking Space'.
    """
    expect(nbsp_page.title).to_have_text("Non-Breaking Space")

@pytest.mark.nbsp
def test_emulated_mouse_click(nbsp_page) -> None:
    """
    Test Scenario: Test Non-Breaking Space Button
       Given the user navigates to the 'Non-Breaking Space' page,
       When the user clicks the "My Button" button,
       Then the button should be clickable.
    """
    nbsp_page.click_button()

   