"""
Module: main_page.py

This module contains the implementation of the MainPage class, which represents the main page of the GCore hosting website.

Classes:
    - MainPage: A class that inherits from BasePage and provides methods to interact with the main page.

Attributes:
    - EUR (str): Symbol for Euro currency.
    - USD (str): Symbol for US Dollar currency.
    - wait (WebDriverWait): WebDriverWait instance for handling explicit waits.
"""

import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pages.utils.hosting_locators as hosting


class MainPage(BasePage):

    EUR = '€'
    USD = '$'

    wait = None

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.wait = WebDriverWait(self.driver, 10)

    def check_connection(self, timeout=20):
        """
        Checks if the server configurator element is visible within the specified timeout.

        Args:
            timeout (int): Maximum time to wait for the element to become visible.

        Returns:
            bool: True if the element is visible, False otherwise.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(hosting.GC_CONFIGURATOR_LOCATOR))
            return True
        except TimeoutException:
            return False

    def accept_cookies(self):
        """
        Accepts cookies by clicking the 'Accept all cookies' button.

        Returns:
            bool: True if cookies are accepted successfully, False otherwise.
        """
        # self.driver.execute_script("document.body.style.zoom='25%'")
        time.sleep(3)
        try:
            cookie_popup = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(hosting.ACCEPT_COOKIES_LOCATOR)
            )
            cookie_popup.click()
        except Exception as e:
            print("Cookies are not found", e)
            return False
        else:
            self.driver.execute_script("window.scrollTo(0, 0);")
            return True

    def save_default_values(self):
        """
        Retrieves default minimum and maximum values from the input fields.

        Returns:
            tuple: Minimum and maximum values (int) as a tuple.
        """
        min_input_field = self.driver.find_element(*hosting.MIN_INPUT_FIELD_LOCATOR)
        min_value = int(min_input_field.find_element(*hosting.MIN_INPUT_LOCATOR).get_attribute('placeholder'))
        max_input_field = self.driver.find_element(*hosting.MAX_INPUT_FIELD_LOCATOR)
        max_value = int(max_input_field.find_element(*hosting.MAX_INPUT_LOCATOR).get_attribute('placeholder'))
        return min_value, max_value

    def switch_to_servers(self, server: int):
        """
        Switches to the specified server type.

        Args:
            server (int): Index of the server type to switch to.
        """
        buttons = self.driver.find_elements(*hosting.SERVERS_SWITCHER_LOCATOR)
        buttons[server].click()

    def switch_to_currency(self, currency: int):
        """
        Switches to the specified currency and returns the currency symbol.

        Args:
            currency (int): Currency type index.

        Returns:
            str: Currency symbol ('€' for Euro, '$' for US Dollar).
        """
        if currency == 1:
            self.wait.until(EC.visibility_of_element_located(hosting.EUR_SWITCHER_LOCATOR)).click()
            return self.EUR
        else:
            self.wait.until(EC.visibility_of_element_located(hosting.USD_SWITCHER_LOCATOR)).click()
            return self.USD

    def change_min_value(self, value: int):
        """
        Changes the value in the minimum input field.

        Args:
            value (int): New value for the minimum input.
        """
        min_input_field = self.driver.find_element(*hosting.MIN_INPUT_FIELD_LOCATOR)
        min_input = min_input_field.find_element(*hosting.MIN_INPUT_LOCATOR)
        min_input.clear()
        min_input.send_keys(value)
        min_input.send_keys(Keys.ENTER)

    def change_max_value(self, value: int):
        """
        Changes the value in the maximum input field.

        Args:
            value (int): New value for the maximum input.
        """
        # Нахождение элемента <gcore-input-field>
        max_input_field = self.driver.find_element(*hosting.MAX_INPUT_FIELD_LOCATOR)
        # Нахождение вложенного элемента <input>
        max_input = max_input_field.find_element(*hosting.MAX_INPUT_LOCATOR)
        max_input.clear()
        max_input.send_keys(value)
        max_input.send_keys(Keys.ENTER)

    def watch_cards(self):
        """
        Expands the grid by clicking 'Show more' until no more cards are available, then retrieves prices.

        Returns:
            list: List of prices extracted from the cards.
        """
        while True:
            button = self.wait.until(EC.element_to_be_clickable(hosting.SHOW_MORE_LOCATOR))
            button_text = button.text
            if "more" in button_text:
                button.click()
            else:
                break

        gc_grid = self.wait.until(EC.presence_of_element_located(hosting.GC_GRID_LOCATOR))
        price_cards = gc_grid.find_elements(*hosting.PRICE_CARD_LOCATOR)
        prices_list = []

        for price_card in price_cards:
            price_element = price_card.find_element(*hosting.PRICE_LOCATOR)
            price_text = price_element.text
            prices_list.append(price_text)

        return prices_list

    def get_out_of_range(self):
        """
    Checks if the 'Out of range' validation message is visible.

    Returns:
        bool: True if the validation message is visible, False otherwise.
    """
        try:
            elements = self.driver.find_elements(*hosting.OUT_OF_RANGE_LOCATOR)
            time.sleep(1)
        except NoSuchElementException:
            return True
        except:
            return True
        else:
            return False

