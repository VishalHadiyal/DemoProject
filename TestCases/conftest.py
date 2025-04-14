from selenium import webdriver
import pytest


# Pytest fixture to set up the WebDriver based on the selected browser
@pytest.fixture()
def setup(browser):
    driver = None  # Initialize driver with None to avoid variable undefined error

    # Launch the appropriate browser based on the parameter received
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge browser")
    else:
        # Raise an exception if an unsupported browser is provided
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver  # Yield the driver instance for test execution

    # Ensure the driver is quit after the test execution is complete
    if driver:
        driver.quit()


# Pytest hook to add a command-line option for selecting the browser
# This allows specifying the browser via the CLI argument: --browser

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on: chrome, firefox, edge")


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