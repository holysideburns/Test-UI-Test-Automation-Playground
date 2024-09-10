"""
Script Name: test_click_page.py
Description: This script tests the "Click" page at http://www.uitestingplayground.com/click.
Challenge: Ensure that the button can be clicked without using an event based click.
"""

import pytest
from playwright.sync_api import expect
from pages.click_page import ClickPage

""" Test Scenario: Verify that the page title is 'Click'. """
@pytest.mark.click

def test_click_page_title(page) -> None:
    click_page = ClickPage(page)
    click_page.navigate()
    expect(click_page.title).to_have_text("Click")

""" Test Scenario: Verify the button can be clicked. """
@pytest.mark.click

def test_emulated_mouse_click(page) -> None:
    click_page = ClickPage(page)
    click_page.navigate()
    click_page.click_button()
    expect(click_page.button).to_have_class('btn btn-success')