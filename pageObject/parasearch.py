from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

class ParaSearch:
    """
    This class represents the ParaSearch page and provides methods
    to interact with various ParaSearch elements.
    """

    # XPath locator for the success alert message element
    SUCCESS_ALERT_XPATH = "//div[@role='alert']"
    USER_PROFILE_LOGO_CSS_SELECTOR = "div[class='MuiBox-root css-zr834m'] div[class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-12og7yj']"

    def __init__(self, driver: WebDriver):
        """
        Constructor to initialize the WebDriver instance and set up an explicit wait.

        :param driver: WebDriver instance used for browser interaction.
        """
        self.driver = driver  # WebDriver instance for interacting with the browser
        self.wait = WebDriverWait(driver, 10)  # Explicit wait with a timeout of 10 seconds

    def get_success_alert_text(self) -> str:
        """
        Retrieves the text content of the success alert message on the page.

        :return: Text content of the success alert message, or an empty string if not found.
        """
        try:
            # Wait until the success alert element is visible on the page
            alert_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.SUCCESS_ALERT_XPATH))
            )
            return alert_message.text.strip()  # Return trimmed text content of the alert message

        except TimeoutException:
            # Log a warning if the element is not found within the specified wait time
            logging.warning("Timeout: Success alert message not found within the wait time.")
            return ""

        except NoSuchElementException:
            # Log a warning if the success alert element is not present in the DOM
            logging.warning("NoSuchElementException: Success alert message element not found.")
            return ""

        except Exception as e:
            # Log any unexpected exceptions that occur during execution
            logging.error(f"Unexpected error while fetching success alert text: {e}")
            return ""

    def clicks_user_profile_logo(self):
        self.driver.find_element(By.CSS_SELECTOR, self.USER_PROFILE_LOGO_CSS_SELECTOR).click()