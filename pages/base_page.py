"""
Module: base_page.py

This module contains the implementation of the BasePage class, which serves as a base class for other page classes.

Classes:
    - BasePage: A base class for page classes with common methods.

Attributes:
    - driver: WebDriver instance.
    - url: URL of the page.

Functions:
    - __init__(self, driver, url): Constructor for the BasePage class.
    - get_driver(self): Returns the WebDriver instance.
    - open(self): Opens the page in the browser.
    - get_url(self): Returns the URL of the page.
"""
class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_driver(self):
        """
        Returns the WebDriver instance.

        Returns:
            WebDriver: Instance of the WebDriver.
        """
        return self.driver

    def open(self):
        """Opens the page in the browser."""
        self.driver.get(self.url)

    def get_url(self):
        """
        Returns the URL of the page.

        Returns:
            str: URL of the page.
        """
        return self.url
