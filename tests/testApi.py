"""
Module: testApi.py
Test class: TestPage

This module contains test cases for validating the functionality of the GCore hosting webpage.

Attributes:
    URL (str): The URL of the GCore hosting webpage.
    EUR (int): Constant representing Euro currency.
    USD (int): Constant representing US Dollar currency.
    DEDICATED (int): Constant representing dedicated servers.
    VIRTUAL (int): Constant representing virtual servers.
    cookies_accepted (bool): Flag indicating whether cookies have been accepted.
    main_page (MainPage): An instance of the MainPage class for interacting with the webpage.
    current_currency (str): The current currency being used.

Test Cases:
    - test_prepare_environment: This function loads the webpage for the first time and accepts all cookies.

    - test_dedicated_eur: Checks dedicated servers' prices for both EUR and USD based on predefined input values.
      It validates if the displayed prices are within the expected range.

    - ... (commented out test cases)

"""

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from time import sleep

MIN_VALUE = -1
MAX_VALUE = -1


class TestPage:
    URL = "https://gcore.com/hosting"
    EUR = 1
    USD = 2
    DEDICATED = 3
    VIRTUAL = 4
    cookies_accepted = False
    main_page: MainPage
    current_currency: str

    @allure.title("Page loading")
    @allure.description("This function loads the pages the first time, accepts all cookies and saves default values")
    def test_prepare_environment(self, browser):
        global MIN_VALUE, MAX_VALUE
        self.main_page = MainPage(browser, self.URL)
        self.main_page.open()
        with allure.step("Connection"):
            assert self.main_page.check_connection(), "Page was not loaded"
        with allure.step("Cookies Acceptation"):
            self.cookies_accepted = self.main_page.accept_cookies()
            assert self.cookies_accepted, "Page was not loaded"
        with allure.step("Saving default values"):
            MIN_VALUE, MAX_VALUE = self.main_page.save_default_values()
            assert MIN_VALUE != -1 and MAX_VALUE != -1, "Default values are not saved"

    @allure.title("Test valid input functionality")
    @allure.description("Check input range")
    def test_valid_input(self, browser):
        global MIN_VALUE, MAX_VALUE

        self.main_page = MainPage(browser, self.URL)
        self.main_page.open()
        sleep(3)
        if not self.cookies_accepted:
            self.cookies_accepted = self.main_page.accept_cookies()
        with allure.step("Validation input values"):
            MIN_VALUE, MAX_VALUE = self.main_page.save_default_values()
            values = [(0, 0), (1, 0), (0, -1), (1, -1), (10, 10), (20, 20)
                      ]
            for value in values:
                self.main_page.change_min_value(MIN_VALUE + value[0])
                if MIN_VALUE + value[0] >= MIN_VALUE:
                    assert not self.main_page.get_out_of_range(), "Wrong min value"
                else:
                    try:
                        assert self.main_page.get_out_of_range(), "Wrong min value"
                    except:
                        raise AssertionError(f"Wrong input value {MIN_VALUE + value[0]}")
                self.main_page.change_max_value(MAX_VALUE + value[1])
                if MAX_VALUE + value[1] <= MAX_VALUE:
                    assert not self.main_page.get_out_of_range(), "Wrong max value"
                else:
                    try:
                        assert self.main_page.get_out_of_range(), "Wrong max value"
                    except:
                        raise AssertionError(f"Wrong max value {MAX_VALUE + value[1]}")

    @allure.title("Test dedicated servers prices")
    @allure.description("Check EUR and USD price")
    @pytest.mark.parametrize("_min, _max, _ser, _cur", [(0, 0, DEDICATED, USD),
                                                        (5, 5, DEDICATED, USD),
                                                        (10, 10, DEDICATED, USD),
                                                        (0, 0, DEDICATED, EUR),
                                                        (5, 5, DEDICATED, EUR),
                                                        (10, 10, DEDICATED, EUR),
                                                        (0, 0, VIRTUAL, USD),
                                                        (5, 5, VIRTUAL, USD),
                                                        (10, 10, VIRTUAL, USD),
                                                        (0, 0, VIRTUAL, EUR),
                                                        (5, 5, VIRTUAL, EUR),
                                                        (10, 10, VIRTUAL, EUR),
                                                        ])
    def test_dedicated_eur(self, browser, _min, _max, _ser, _cur):
        self.main_page = MainPage(browser, self.URL)
        self.main_page.open()
        sleep(3)
        if not self.cookies_accepted:
            self.cookies_accepted = self.main_page.accept_cookies()
        with allure.step('Prepare default values'):
            self.main_page.switch_to_servers(self.DEDICATED)
            self.current_currency = self.main_page.switch_to_currency(_cur)
            MIN_VALUE, MAX_VALUE = self.main_page.save_default_values()
        with allure.step('Check cards'):
            self.main_page.change_min_value(MIN_VALUE + _min)
            self.main_page.change_max_value(MAX_VALUE - _max)
            cards = self.main_page.watch_cards()
            for card in cards:
                elements = card.split(" ")
                assert self.current_currency == elements[0], "Wrong currency"
                if "," in elements[1]:
                    elements[1] = elements[1].replace(",", "")
                assert MIN_VALUE + _min <= float(elements[1]) <= MAX_VALUE - _max, "Wrong range"
        sleep(10)
