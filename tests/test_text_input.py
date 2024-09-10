"""
Script Name: test_text_input_page.py
Description: This script tests the "Text Input" page at http://www.uitestingplayground.com/textinput.
Challenge: Ensure that the text box can be interacted with without using an event based input.
"""

import pytest
from playwright.sync_api import expect
from pages.text_input_page import TextInput

""" Test Scenario: Verify that the page title is 'Text Input'. """
@pytest.mark.textinput
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_text_input_page_title(page) -> None:
    text_input_page = TextInput(page)
    text_input_page.navigate()
    expect(text_input_page.title).to_have_text("Text Input")

""" Test Scenario: Verify that text can be entered into the textbox 
    and that clicking the button sets the button name to the text. """
@pytest.mark.textinput
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_text_input(page) -> None:
    text_input_page = TextInput(page)
    text_input_page.navigate()
    input_value = "Test Value"
    expect(text_input_page.button).not_to_have_text(input_value)
    text_input_page.enter_text(input_value)
    text_input_page.click_button()
    expect(text_input_page.button).to_have_text(input_value)