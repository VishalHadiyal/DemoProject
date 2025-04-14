from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:
    """
    Page Object Model (POM) class for the Home Page.
    """

    # Locators
    button_login_xpath = "//button[text()='Log In']"
    text_Latest_Opinion_CSS_SELECTOR = ".MuiTypography-root.MuiTypography-body1.css-66ma6b"

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def click_login_button(self):
        """
        Clicks the login button.
        """
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """
        Waits for the specified element to be visible.
        :param locator: Locator tuple (By, value)
        :param timeout: Maximum time to wait for the element to be visible
        :return: WebElement if found, else raises TimeoutException
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_until_element_visible(self, timeout=10):
        """
        Scrolls the page until the 'Latest Opinion' section is displayed or timeout is reached.
        :param timeout: Maximum time to wait for the element to be visible
        :return: WebElement if found and visible, else raises Exception
        """
        locator = (By.CSS_SELECTOR, self.text_Latest_Opinion_CSS_SELECTOR)
        end_time = time.time() + timeout

        while time.time() < end_time:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)  # Small delay to allow rendering
            except:
                pass  # Ignore exceptions and continue scrolling

        raise Exception(f"Element {self.text_Latest_Opinion_CSS_SELECTOR} not found or not visible after scrolling.")
