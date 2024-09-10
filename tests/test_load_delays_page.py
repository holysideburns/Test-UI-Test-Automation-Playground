"""
Script Name: test_load_delays_page.py
Description: This script tests the "Load Delays" page at http://www.uitestingplayground.com/loaddelay.
Challenge: Ensure that the test handles long loading times.
"""

import pytest
from playwright.sync_api import expect
from pages.load_delays_page import LoadDelaysPage

""" Test Scenario: Verify that he page title is 'Load Delays'. """
@pytest.mark.loaddelays

def test_load_delays_page_title(page) -> None:
    load_delays_page = LoadDelaysPage(page)
    load_delays_page.navigate()
    expect(load_delays_page.title).to_have_text("Load Delays")

""" Test Scenario: Verify that the button can be clicked once it finishes loading. """
@pytest.mark.loaddelays

def test_delayed_button(page) -> None:
    load_delays_page = LoadDelaysPage(page)
    load_delays_page.navigate()
    load_delays_page.click_delayed_button()