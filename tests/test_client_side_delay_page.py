"""
Script Name: test_client_side_delay_page.py
Description: This script tests the "Client Side Delay" page at http://www.uitestingplayground.com/clientdelay.
Challenge: Ensure that the test can handle the delay of the JavaScript calculation on the client side.
"""

import pytest
from playwright.sync_api import expect
from pages.client_side_delay_page import ClientSideDelayPage

@pytest.fixture
def client_side_delay_page(page) -> ClientSideDelayPage:
    client_side_delay_page = ClientSideDelayPage(page)
    client_side_delay_page.navigate()
    return client_side_delay_page

@pytest.mark.clientsidedelay
def test_client_side_delay_page_title(client_side_delay_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Client Side Delay' page,
        When the page is loaded,
        Then the page title should be 'Client Side Delay'.
    """
    expect(client_side_delay_page.title).to_have_text("Client Side Delay")

""" Test Scenario: Verify that the JavaScript message appears . """
@pytest.mark.clientsidedelay
def test_javascript_data_delay(client_side_delay_page) -> None:
    """
    Test Scenario: Test Delayed Message
        Given the user navigates to the 'Client Side Delay' page,
        When the user clicks the button,
        Then a message should appear after about 15 seconds.
    """
    client_side_delay_page.click_javascript_button()
    expect(client_side_delay_page.javascript_message).to_be_visible(timeout=20000)