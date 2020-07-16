"""Fetch title and url all feed.

This script uses selenium to fetch title and URL of all feed in Feedly RSS web applications
and put it into a feed.txt file.

Before using it:
    - change login / password : complete_login_feedly_form_and_connect function

To use it:
    $ python fetch_tilte_and_url_all_feed.py
"""
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def click_css_selector(css_selector: str):
    """Wait element with css selector to be clickable then click."""
    element = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    element.click()


def goto_login_page():
    """Click on the button login."""
    driver.find_element_by_css_selector('.LandingHeaderBar__action').click()


def goto_login_feedly_page():
    """Click on the button Continue with feedly."""
    driver.find_element_by_css_selector('a.primary:nth-child(4)').click()


def complete_login_feedly_form_and_connect():
    """Fill the login and password fields, then click on login button to confirm."""
    login = "your@email.dom"
    password = "yourpassword"  # Maybe incorrect
    driver.find_element_by_css_selector('input.input-text:nth-child(1)').send_keys(login)
    driver.find_element_by_css_selector('input.input-text:nth-child(2)').send_keys(password)
    driver.find_element_by_css_selector('.button').click()


def select_all_feed():
    """Click on the all label on the right to display all feed."""
    click_css_selector('.LeftnavList__feed-list > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)')


def in_finish_scroll_feed(value: int):
    """Select the feed frame then try to find the "End of feed" element to stop scrolling."""
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.ID, "feedlyFrame")))
    value_increase = value
    while True:
        try:
            driver.find_element_by_class_name('EntryList__heading')
            break
        except NoSuchElementException:
            driver.execute_script("document.getElementById('feedlyFrame').scroll(0," + str(value) + ")")
            value = value + value_increase
    driver.execute_script("document.getElementById('feedlyFrame').scroll(0," + str(value) + ")")
    time.sleep(0.5)


if __name__ == "__main__":
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("https://feedly.com/i/welcome")
    goto_login_page()
    goto_login_feedly_page()
    complete_login_feedly_form_and_connect()
    select_all_feed()
    in_finish_scroll_feed(2000)
    elements = driver.find_elements_by_css_selector('div.content > a')  # fetch all feed link
    with open("feed.txt", 'w', encoding="utf8") as f:
        f.writelines([''.join([elt.text, " ", elt.get_attribute('href'), "\n"]) for elt in elements])
    driver.close()
