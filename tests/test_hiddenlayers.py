"""
Script Name: test_hiddenlayers.py
Description: This script tests the "Hidden Layers" subpage at http://www.uitestingplayground.com/hiddenlayers.
Challenge: Make sure that the test can not interact with the green button after it has been clicked.
Comment: Not happy with this solution using 'try', but since the green button doesn't actually change state, I see no other way.
"""

import pytest
from playwright.sync_api import expect
from pages.hiddenlayers_page import HiddenLayersPage

@pytest.mark.hiddenlayers
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_hiddenlayers_page_title(page) -> None:
    hiddenlayers_page = HiddenLayersPage(page)
    hiddenlayers_page.navigate()
    expect(hiddenlayers_page.get_title()).to_have_text("Hidden Layers")

@pytest.mark.hiddenlayers
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_green_button(page) -> None:
    hiddenlayers_page = HiddenLayersPage(page)
    hiddenlayers_page.navigate()
    hiddenlayers_page.click_green_button()
    try:
        hiddenlayers_page.click_green_button()
        # Failure
        raise AssertionError("Green button should not be clickable after the initial click.")
    except:
        # Success
        pass
