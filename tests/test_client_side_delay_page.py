"""
Script Name: test_client_side_delay_page.py
Description: This script tests the "Client Side Delay" page at http://www.uitestingplayground.com/clientdelay.
Challenge: Ensure that the test can handle the delay of the JavaScript calculation on the client side.
"""

import pytest
from playwright.sync_api import expect
from pages.client_side_delay_page import ClientSideDelayPage

""" Test Scenario: Verify that the page title is 'Client Side Delay'. """
@pytest.mark.clientsidedelay

def test_client_side_delay_page_title(page) -> None:
    client_side_delay_page = ClientSideDelayPage(page)
    client_side_delay_page.navigate()
    expect(client_side_delay_page.title).to_have_text("Client Side Delay")

""" Test Scenario: Verify that the JavaScript message appears . """
@pytest.mark.clientsidedelay

def test_javascript_data_delay(page) -> None:
    client_side_delay_page = ClientSideDelayPage(page)
    client_side_delay_page.navigate()
    client_side_delay_page.click_javascript_button()
    expect(client_side_delay_page.javascript_message).to_be_visible(timeout=20000)