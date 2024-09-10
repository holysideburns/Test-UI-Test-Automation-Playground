"""
Script Name: test_load_delays_page.py
Description: This script tests the "Load Delays" page at http://www.uitestingplayground.com/loaddelay.
Challenge: Ensure that the test handles long loading times.
"""

import pytest
from playwright.sync_api import expect
from pages.load_delays_page import LoadDelaysPage

@pytest.fixture
def load_delays_page(page) -> LoadDelaysPage:
    load_delays_page = LoadDelaysPage(page)
    load_delays_page.navigate()
    return load_delays_page

@pytest.mark.loaddelays
def test_load_delays_page_title(load_delays_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Load Delays' page,
        When the page is loaded,
        Then the page title should be 'Load Delays'.
    """
    expect(load_delays_page.title).to_have_text("Load Delays")

@pytest.mark.loaddelays
def test_delayed_button(load_delays_page) -> None:
    """
    Test Scenario: Test Delayed Button
        Given the user is on the 'Load Delays' page,
        When the page is loaded,
        Then the button should be clickable.
    """
    load_delays_page.click_button()