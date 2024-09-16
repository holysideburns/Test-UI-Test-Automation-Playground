"""
Script Name: test_alerts_page.py
Description: This script tests the "Alerts" page at http://www.uitestingplayground.com/alerts.
Challenge: Handle three different type of dialogs (alert, confirm & prompt).
"""

import pytest
from playwright.sync_api import expect
from pages.alerts_page import AlertsPage

@pytest.fixture
def alerts_page(page) -> AlertsPage:
    alerts_page = AlertsPage(page)
    alerts_page.navigate()
    return alerts_page

@pytest.mark.alerts
def test_alerts_page_title(alerts_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Alerts' page,
        When the page is loaded,
        Then the page title should be 'Alerts'.
    """
    expect(alerts_page.title).to_have_text("Alerts")

@pytest.mark.alerts
def test_alert_button(alerts_page) -> None:
    """
    Test Scenario: Test Alerts Button
       Given the user navigates to the 'Alerts' page,
       When the user clicks the "Alert" button,
       Then a prompt should be shown,
       And the alert button should be clickable.
    """
    def handle_alert(dialog):
        dialog.accept()

    alerts_page.page.on("dialog", handle_alert)
    alerts_page.alert_button.click()

@pytest.mark.alerts
def test_confirm_button_accept(alerts_page) -> None:
    """
    Test Scenario: Test Confirm Button
       Given the user navigates to the 'Alerts' page,
       When the user clicks the "Confirm" button,
       And then clicks the "Okay" button in the prompt,
       Then an alert should display "Yes".
    """
    alert_message = []

    def handle_confirm(dialog):
        dialog.accept()

    def handle_alert(dialog):
        alert_message.append(dialog.message)
        dialog.accept()
    
    alerts_page.page.on("dialog", lambda dialog: handle_confirm(dialog) if dialog.type == "confirm" else handle_alert(dialog))
    alerts_page.confirm_button.click()
    alerts_page.page.wait_for_event("dialog")    
    assert alert_message[0] == "Yes", f"Expected alert message to be \"Yes\", but got {alert_message}."

@pytest.mark.alerts
def test_confirm_button_dismiss(alerts_page) -> None:
    """
    Test Scenario: Test Confirm Button
       Given the user navigates to the 'Alerts' page,
       When the user clicks the "Confirm" button,
       And then clicks the "Cancel" button in the prompt,
       Then an alert should display "No".
    """
    alert_message = []

    def handle_confirm(dialog):
        dialog.dismiss()

    def handle_alert(dialog):
        alert_message.append(dialog.message)
        dialog.accept()
    
    alerts_page.page.on("dialog", lambda dialog: handle_confirm(dialog) if dialog.type == "confirm" else handle_alert(dialog))
    alerts_page.confirm_button.click()
    alerts_page.page.wait_for_event("dialog")
    assert alert_message[0] == "No", f"Expected alert message to be \"No\", but got {alert_message}."

@pytest.mark.alerts
def test_prompt_button_accept(alerts_page) -> None:
    """
    Test Scenario: Test Prompt Button
       Given the user navigates to the 'Alerts' page,
       When the user clicks the "Prompt" button,
       And enters a value in the prompt,
       And clicks the "Okay" button,
       Then an alert showing the value should be shown.
    """
    test_value = "dolphins"
    alert_message = []

    def handle_prompt(dialog):
        dialog.accept(test_value)
    
    def handle_alert(dialog):
        alert_message.append(dialog.message)
        dialog.accept()

    alerts_page.page.on("dialog", lambda dialog: handle_prompt(dialog) if dialog.type == "prompt" else handle_alert(dialog))
    alerts_page.prompt_button.click()
    alerts_page.page.wait_for_event("dialog")
    assert alert_message[0] == f"User value: {test_value}", f"Expected alert message to be \"User value: {test_value}\", but got {alert_message}."
    
@pytest.mark.alerts
def test_prompt_button_dismiss(alerts_page) -> None:
    """
    Test Scenario: Test Prompt Button
       Given the user navigates to the 'Alerts' page,
       When the user clicks the "Prompt" button,
       And clicks the "Cancel" button,
       Then an alert showing "no answer" should be shown.
    """
    alert_message = []

    def handle_prompt(dialog):
        dialog.dismiss()
    
    def handle_alert(dialog):
        alert_message.append(dialog.message)
        dialog.accept()

    alerts_page.page.on("dialog", lambda dialog: handle_prompt(dialog) if dialog.type == "prompt" else handle_alert(dialog))
    alerts_page.prompt_button.click()
    alerts_page.page.wait_for_event("dialog")
    assert alert_message[0] == "User value: no answer", f"Expected alert message to be \"User value: no answer\", but got {alert_message}."  