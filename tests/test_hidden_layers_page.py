"""
Script Name: test_hidden_layers_page.py
Description: This script tests the "Hidden Layers" subpage at http://www.uitestingplayground.com/hiddenlayers.
Challenge: Make sure that the test can not interact with the green button after it has been clicked.
Comment: Not happy with this solution using 'try', but since the green button doesn't actually change state, I see no other way.
"""

import pytest
from playwright.sync_api import expect
from pages.hidden_layers_page import HiddenLayersPage

""" Test Scenario: Verify that he page title is 'Hidden Layers'. """
@pytest.mark.hiddenlayers

def test_hidden_layers_page_title(page) -> None:
    hidden_layers_page = HiddenLayersPage(page)
    hidden_layers_page.navigate()
    expect(hidden_layers_page.title).to_have_text("Hidden Layers")

""" Test Scenario: Verify that the green button can not be clicked twice. """
@pytest.mark.hiddenlayers

def test_green_button(page) -> None:
    hidden_layers_page = HiddenLayersPage(page)
    hidden_layers_page.navigate()
    hidden_layers_page.click_green_button()
    try:
        hidden_layers_page.click_green_button()
        # Failure
        raise AssertionError("Green button should not be clickable after the initial click.")
    except:
        # Success
        pass
