"""
Script Name: test_load_delays_page.py
Description: This script tests the "Load Delays" page at http://www.uitestingplayground.com/loaddelay.
Challenge: Ensure that the test handles long loading times.
"""

import pytest
from playwright.sync_api import expect
from pages.load_delays_page import LoadDelaysPage

@pytest.mark.loaddelays
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_load_delays_page_title(page) -> None:
    load_delays_page = LoadDelaysPage(page)
    load_delays_page.navigate()
    expect(load_delays_page.get_title()).to_have_text("Load Delays")

@pytest.mark.loaddelays
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_delayed_button(page) -> None:
    load_delays_page = LoadDelaysPage(page)
    load_delays_page.navigate()
    load_delays_page.click_delayed_button()