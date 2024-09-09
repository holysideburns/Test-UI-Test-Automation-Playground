"""
Script Name: test_loaddelays.py
Description: This script tests the "Load Delays" page at http://www.uitestingplayground.com/loaddelay.
Challenge: Ensure that the test handles long loading times.
"""

import pytest
from playwright.sync_api import expect
from pages.loaddelays_page import LoadDelaysPage

@pytest.mark.loaddelays
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_loaddelays_page_title(page) -> None:
    loaddelays_page = LoadDelaysPage(page)
    loaddelays_page.navigate()
    expect(loaddelays_page.get_title()).to_have_text("Load Delays")

@pytest.mark.loaddelays
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_delayed_button(page) -> None:
    loaddelays_page = LoadDelaysPage(page)
    loaddelays_page.navigate()
    loaddelays_page.click_delayed_button()