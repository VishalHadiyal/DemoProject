from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup(request, browser):
    browser = request.param
    headless = request.config.getoption("--headless")
    driver = None

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            print("Launching Chrome in headless mode")
        else:
            print("Launching Chrome")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            print("Launching Firefox in headless mode")
        else:
            print("Launching Firefox")
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
            print("Launching Edge in headless mode")
        else:
            print("Launching Edge")
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    if driver:
        driver.quit()


# Pytest hook to add a command-line option for selecting the browser
# This allows specifying the browser via the CLI argument: --browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, firefox, edge")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")


# Pytest fixture to retrieve the browser value from command-line options
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


####################### Pytest HTML Report Configuration ###########################

# Hook to add custom environment info to the HTML test report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'nop Commerce'  # Define project name
        config._metadata['Module Name'] = 'customer'  # Define module name
        config._metadata['Tester'] = 'khemlall'  # Define tester name


# Hook to remove unwanted metadata from the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # Remove JAVA_HOME if present
    metadata.pop("Plugin", None)  # Remove Plugin metadata if present