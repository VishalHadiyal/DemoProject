import time
import pytest

from pageObject.parasearch import ParaSearch
from pageObject.homepage import HomePage
from pageObject.loginPage import LoginPage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class TestParaSearchPage:
    """
    This class contains test cases for verifying the login and paragraph search functionality
    on the Parasors panel.
    """

    baseURL = ReadConfig.get_application_url()  # Application base URL from config file
    logger = LogGen.loggen()  # Logger instance for recording test execution steps

    @pytest.mark.regression
    def test_para_search_functionality(self, setup):
        """
        Test case to verify successful login and paragraph search functionality.
        """

        self.logger.info("========== Test: Para Search Functionality Started ==========")

        # Setup WebDriver and open the application
        self.driver = setup
        self.logger.info("Initializing WebDriver and opening application URL.")
        self.driver.implicitly_wait(30)  # Apply implicit wait globally for element loading
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info(f"Application URL opened: {self.baseURL}")

        # Initialize Page Object Models
        self.logger.info("Initializing Page Object classes.")
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        parasearch = ParaSearch(self.driver)

        # Click login button on homepage
        self.logger.info("Clicking 'Login' button on the homepage.")
        homepage.click_login_button()

        # Enter login credentials
        self.logger.info("Entering login credentials (username & password).")
        loginpage.set_username(ReadConfig.get_user_email())
        loginpage.set_password(ReadConfig.get_user_password())

        # Click login
        self.logger.info("Submitting login form.")
        loginpage.click_login()

        # Verify login success alert
        self.logger.info("Verifying login success message.")
        success_message = parasearch.get_success_alert_text()
        if success_message == "Login Successful !":
            self.logger.info("Login successful. Message received: 'Login Successful !'")
        else:
            self.logger.error(f"Login failed. Unexpected message: '{success_message}'")
            self.driver.save_screenshot("./Screenshots/test_login_failure.png")
            assert False  # Fail the test

        # Click on 'Create First Chat' button
        self.logger.info("Clicking on 'Create First Chat' button.")
        parasearch.clicks_pera_search_create_first_chat()

        # Enter paragraph search text
        search_text = ReadConfig.enter_para_search_text()
        self.logger.info(f"Entering paragraph search text: {search_text}")
        parasearch.set_search_bar_text(search_text)

        # Click search button
        self.logger.info("Clicking the search button to start paragraph search.")
        parasearch.clicks_search_button()

        # Wait for the response to load
        self.logger.info("Waiting for response to load (sleeping for 30 seconds).")
        time.sleep(30)  # Ideally replaced with WebDriverWait in real scenarios

        # Scroll down to view complete response
        self.logger.info("Scrolling down to ensure full response is visible.")
        self.driver.execute_script("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        """)

        # Fetch response text
        self.logger.info("Fetching the paragraph search response text.")
        response_text_data = parasearch.get_response_text()
        print("Response Text from Para Search:", response_text_data)  # Console output

        # Verify and log result based on response presence
        if response_text_data:
            self.logger.info("Search successful. Response text is displayed.")
            assert True
        else:
            self.logger.error("Search failed. No response text found.")
            self.driver.save_screenshot("./Screenshots/test_search_failure.png")
            assert False  # Fail the test

        # Clean up and close the browser
        self.logger.info("Closing the browser after test execution.")
        self.driver.quit()

        self.logger.info("========== Test: Para Search Functionality Completed ==========")
