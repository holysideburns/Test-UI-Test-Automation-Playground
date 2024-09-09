"""
Script Name: test_click_page.py
Description: This script tests the "Click" page at http://www.uitestingplayground.com/click.
Challenge: Ensure that the button can be clicked without using an event based click.
"""

import pytest
from playwright.sync_api import expect
from pages.click_page import ClickPage

@pytest.mark.click
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_click_page_title(page) -> None:
    click_page = ClickPage(page)
    click_page.navigate()
    expect(click_page.get_title()).to_have_text("Click")

@pytest.mark.click
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_emulated_mouse_click(page) -> None:
    click_page = ClickPage(page)
    click_page.navigate()
    expect(click_page.get_button()).to_have_class('btn btn-primary')
    click_page.click_button()
    expect(click_page.get_button()).to_have_class('btn btn-success')