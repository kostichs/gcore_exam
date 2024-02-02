import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()  # Chrome_options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "120.0")
    # driver = webdriver.Chrome(options)
    driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub",
                              options=options,
                              )

    '''driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub",
                              options=options,
                              )'''
    driver.maximize_window()

    yield driver

    driver.quit()