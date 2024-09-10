"""
Script Name: test_click_page.py
Description: This script tests the "Click" page at http://www.uitestingplayground.com/click.
Challenge: Ensure that the button can be clicked without using an event based click.
"""

import pytest
from playwright.sync_api import expect
from pages.click_page import ClickPage

@pytest.fixture
def click_page(page) -> ClickPage:
    click_page = ClickPage(page)
    click_page.navigate()
    return click_page

@pytest.mark.click
def test_click_page_title(click_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Click' page,
        When the page is loaded,
        Then the page title should be 'Click'.
    """
    expect(click_page.title).to_have_text("Click")

@pytest.mark.click
def test_emulated_mouse_click(click_page) -> None:
    """
    Test Scenario: Test Emulated Mouse Click
        Given the user navigates to the 'Click' page,
        When the page is loaded,
        Then the user should be able to click the button.
    """
    click_page.click_button()
    expect(click_page.button).to_have_class('btn btn-success')