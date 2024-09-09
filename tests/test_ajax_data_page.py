"""
Script Name: test_ajax_data_page.py
Description: This script tests the "AJAX Data" page at http://www.uitestingplayground.com/ajax.
Challenge: Ensure that the test can handle the delay of the AJAX request to the web server.
"""

import pytest
from playwright.sync_api import expect
from pages.ajax_data_page import AjaxData

@pytest.mark.ajaxdata
@pytest.mark.skip(reason="Skipping this test for now.")
def test_ajax_data_page_title(page) -> None:
    ajax_data_page = AjaxData(page)
    ajax_data_page.navigate()
    expect(ajax_data_page.get_title()).to_have_text("AJAX Data")

@pytest.mark.ajaxdata
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_ajax_data_delay(page) -> None:
    ajax_data_page = AjaxData(page)
    ajax_data_page.navigate()
    ajax_data_page.click_ajax_button()
    expect(ajax_data_page.get_ajax_message()).to_be_visible(timeout=20000)