"""
Script Name: test_verify_text_page.py
Description: This script tests the "Verify Text" page at http://www.uitestingplayground.com/verifytext.
Challenge: Ensure that the welcome message that has a <span> element in it can be found by the test.
"""

import pytest
from playwright.sync_api import expect
from pages.verify_text_page import VerifyTextPage

@pytest.fixture
def verify_text_page(page) -> VerifyTextPage:
    verify_text_page = VerifyTextPage(page)
    verify_text_page.navigate()
    return verify_text_page

@pytest.mark.verifytext
def test_verify_text_title(verify_text_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Verify Text' page,
        When the page is loaded,
        Then the page title should be 'Verify Text'.
    """
    expect(verify_text_page.title).to_have_text("Verify Text")

@pytest.mark.verifytext
def test_verify_welcome_message(verify_text_page) -> None:
    """
    Test Scenario: Verify that the message is displayed
        Given the user navigates to the 'Verify Text' page,
        When the page is loaded,
        Then there should be a message stating "Welcome UserName!".
    """
    expect(verify_text_page.welcome_message).to_be_visible()