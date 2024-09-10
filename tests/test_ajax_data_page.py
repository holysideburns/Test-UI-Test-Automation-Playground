"""
Script Name: test_ajax_data_page.py
Description: This script tests the "AJAX Data" page at http://www.uitestingplayground.com/ajax.
Challenge: Ensure that the test can handle the delay of the AJAX request to the web server.
"""

import pytest
from playwright.sync_api import expect
from pages.ajax_data_page import AjaxDataPage

@pytest.fixture
def ajax_data_page(page) -> AjaxDataPage:
    ajax_data_page = AjaxDataPage(page)
    ajax_data_page.navigate()
    return ajax_data_page

@pytest.mark.ajaxdata
def test_ajax_data_page_title(ajax_data_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'AJAX Data' page,
        When the page is loaded,
        Then the page title should be 'AJAX Data'.
    """
    expect(ajax_data_page.title).to_have_text("AJAX Data")

@pytest.mark.ajaxdata
def test_ajax_data_delay(ajax_data_page) -> None:
    """
    Test Scenario: Test Delayed Message
        Given the user navigates to the 'AJAX Data' page,
        When the user clicks the button,
        Then a message should appear after about 15 seconds.
    """
    ajax_data_page.click_button()
    expect(ajax_data_page.message).to_be_visible(timeout=20000)