from selenium.webdriver.common.by import By

GC_CONFIGURATOR_LOCATOR = (By.CLASS_NAME, "gc-server-configurator-buttons")
ACCEPT_COOKIES_LOCATOR = (By.XPATH, "//button[contains(@class, 'gc-button') and text()='Accept all cookies']")
INPUT_VALIDATOR_LOCATOR = (By.XPATH, "//p[@class='gc-input-validation' and contains(text(), 'Out of range')]")
SERVERS_SWITCHER_LOCATOR = (By.TAG_NAME, "button")
EUR_SWITCHER_LOCATOR = (By.CSS_SELECTOR, 'label.gc-text[for="left"]')
USD_SWITCHER_LOCATOR = (By.CSS_SELECTOR, 'label.gc-text[for="right"]')
MIN_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, 'gcore-input-field[formcontrolname="min"]')
MAX_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, 'gcore-input-field[formcontrolname="max"]')
MIN_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input.gc-input')
MAX_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input.gc-input')
SHOW_MORE_LOCATOR = (By.CSS_SELECTOR, ".gc-text_16.gc-server-configurator-more")
GC_GRID_LOCATOR = (By.CSS_SELECTOR, "div.gc-grid.gc-grid_3.gc-m-top_xx-large")
PRICE_CARD_LOCATOR = (By.CLASS_NAME, 'price-card')
PRICE_LOCATOR = (By.CLASS_NAME, 'price-card_price')
OUT_OF_RANGE_LOCATOR = (By.XPATH, "//p[@class='gc-input-validation' and contains(text(), 'Out of range')]")