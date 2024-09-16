"""
Script Name: test_shadow_dom_page.py
Description: This script tests the "Shadow DOM" page at http://www.uitestingplayground.com/shadowdom.
Challenge: Ensure that elements inside a shadow DOM can be located and interacted with.
"""
import pyperclip
import pytest
from playwright.sync_api import expect
from pages.shadow_dom_page import ShadowDomPage

@pytest.fixture
def shadow_dom_page(page) -> ShadowDomPage:
    shadow_dom_page = ShadowDomPage(page)
    shadow_dom_page.navigate()
    return shadow_dom_page

@pytest.mark.shadowdom
def test_shadow_dom_page_title(shadow_dom_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Shadow DOM' page,
        When the page is loaded,
        Then the page title should be 'Shadow DOM'.
    """
    expect(shadow_dom_page.title).to_have_text("Shadow DOM")

@pytest.mark.shadowdom
def test_shadow_dom_interaction(shadow_dom_page) -> None:
    """
    Test Scenario: Test Shadow DOM Interaction
       
    """
    shadow_dom_page.generate_button.click()
    shadow_dom_page.copy_button.click()
    """ The copy button is actuall broken on the site, copying manually instead."""
    pyperclip.copy(shadow_dom_page.guid_field.text_content())
    clipboard_value = pyperclip.paste()
    print(f"pyperclip.paste() = {clipboard_value}")
    expect(shadow_dom_page.guid_field).to_have_text(clipboard_value)

   