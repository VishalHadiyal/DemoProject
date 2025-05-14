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
    TEXT_CONFIRM_POPUP_XPATH = "//p[@id='modal-modal-description']"
    BUTTON_CONFIRM_POPUP_XPATH = "//button[normalize-space()='Ok']"
    BUTTON_PERA_SEARCH_CREATE_FIRST_CHAT_XPATH = "//div[@aria-label='Please create first chat']"
    SEARCH_BAR_CSS_SELECTOR = "div[class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation2 css-hs986'] input[placeholder='Ask any Question']"
    BUTTON_SEARCH_CSS_SELECTOR = "div[class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation2 css-hs986'] img[class='MuiBox-root css-0']"
    RESPONSE_TEXT_CSS_SELECTOR = "div[class='MuiBox-root css-j7qwjs'] div[class='MuiBox-root css-0'] span span"
    BUTTON_SIDE_BAR_CSS_SELECTOR = ".MuiBox-root.css-19zr93t"
    BUTTON_ADD_NEW_CHAT_CSS_SELECTOR = ".MuiBox-root.css-ibs9f4"
    TEXT_SUCCESS_POPUP_MESSAGE_XPATH = "//div[@class='Toastify__toast-container Toastify__toast-container--top-right']"

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

    def get_text_on_confirm_register_popup(self, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, self.TEXT_CONFIRM_POPUP_XPATH))
        )
        return element.text

    def clicks_ok_button_on_confirm_register_popup(self):
        """
        Clicks the 'OK' button on the confirmation register popup.
        """
        # Locate the 'OK' button using its XPath and click it
        self.driver.find_element(By.XPATH, self.BUTTON_CONFIRM_POPUP_XPATH).click()

    def click_if_displayed_pera_search_create_first_chat(self):
        """
        Checks if the 'Create First Chat' button in the Pera Search is displayed and clicks it if it is.
        Returns True if clicked, False otherwise.
        """
        try:
            button = self.driver.find_element(By.XPATH, self.BUTTON_PERA_SEARCH_CREATE_FIRST_CHAT_XPATH)
            if button.is_displayed():
                button.click()
                return True
            return False
        except NoSuchElementException:
            return False

    def set_search_bar_text(self, text):
        """
        Sets the text in the search bar.

        :param text: The text to be entered in the search bar.
        """
        search_bar = self.driver.find_element(By.CSS_SELECTOR, self.SEARCH_BAR_CSS_SELECTOR)
        search_bar.clear()
        search_bar.send_keys(text)

    def clicks_search_button(self):
        """
        Clicks the search button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.BUTTON_SEARCH_CSS_SELECTOR).click()

    def get_response_text(self):
        """
        Retrieves the response text from the search results and scrolls to it if present.
        :return: str
        """
        try:
            # Wait until the response text element is visible on the page
            response_text = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.RESPONSE_TEXT_CSS_SELECTOR))
            )

            # Scroll the element into view
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                       response_text)

            return response_text.text.strip()  # Return trimmed text content of the response

        except TimeoutException:
            logging.warning("Timeout: Response text not found within the wait time.")
            return ""

        except NoSuchElementException:
            logging.warning("NoSuchElementException: Response text element not found.")
            return ""

        except Exception as e:
            logging.error(f"Unexpected error while fetching response text: {e}")
            return ""

    def clicks_side_bar_button(self):
        """
        Clicks the side bar button if it is visible and interactable.
        """
        try:
            sidebar_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.BUTTON_SIDE_BAR_CSS_SELECTOR)))
            sidebar_button.click()
        except TimeoutException:
            logging.error("Sidebar button not found or not clickable.")
            raise

    def clicks_add_new_chat_button(self):
        """
        Clicks the add new chat button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.BUTTON_ADD_NEW_CHAT_CSS_SELECTOR).click()

    def get_text_on_success_popup_message(self, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, self.TEXT_SUCCESS_POPUP_MESSAGE_XPATH))
        )
        WebDriverWait(self.driver, timeout).until(
            lambda driver: element.text.strip() != ""
        )
        return element.text

    def wait_for_search_bar_ready(self, driver, parasearch, timeout=10):
        """
        Waits until the search bar is clickable and interactable.
        """
        wait = WebDriverWait(driver, timeout)
        return wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, parasearch.SEARCH_BAR_CSS_SELECTOR))
        )

