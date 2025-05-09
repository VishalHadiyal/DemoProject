import time

import pytest
from selenium.common import NoSuchElementException

from pageObject.parasearch import ParaSearch
from pageObject.homepage import HomePage
from pageObject.loginPage import LoginPage
from pageObject.profilepage import ProfilePage
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
        Regression Test Case:
        Verifies the successful login functionality and paragraph search feature.
        """

        self.logger.info("========== [TEST STARTED] test_para_search_functionality ==========")

        # Setup WebDriver and open the application
        self.driver = setup
        self.logger.info("Initializing WebDriver and launching application.")
        self.driver.implicitly_wait(60)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info(f"Application launched: {self.baseURL}")

        # Initialize Page Object Model classes
        self.logger.info("Initializing Page Objects: HomePage, LoginPage, ParaSearch, ProfilePage.")
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        parasearch = ParaSearch(self.driver)
        profilepage = ProfilePage(self.driver)

        # Click on the login button on the homepage
        self.logger.info("Clicking 'Login' button on HomePage.")
        homepage.click_login_button()

        # Enter login credentials
        self.logger.info("Filling in login credentials.")
        loginpage.set_username(ReadConfig.get_user_email())
        loginpage.set_password(ReadConfig.get_user_password())

        # Submit login form
        self.logger.info("Submitting login form.")
        loginpage.click_login()

        # Verify login success
        self.logger.info("Verifying login success alert message.")
        success_message = parasearch.get_success_alert_text()
        if success_message == "Login Successful !":
            self.logger.info("Login successful: 'Login Successful !'")
        else:
            self.logger.error(f"Login failed. Received message: '{success_message}'")
            self.driver.save_screenshot("./Screenshots/test_para_search_functionality_login_failure.png")
            assert False

        # Define expected success message globally
        expected_message = ReadConfig.get_new_chat_create_text()
        success_message = ""

        # Handle new chat creation flow
        try:
            if parasearch.click_if_displayed_pera_search_create_first_chat():
                self.logger.info("Clicked 'Create First Chat' button.")
                success_message = parasearch.get_text_on_success_popup_message()
                assert success_message == expected_message, f"Expected '{expected_message}', got '{success_message}'"
                self.logger.info("New chat created successfully using 'Create First Chat'.")
            else:
                self.logger.info("'Create First Chat' not present. Falling back to sidebar method.")
                parasearch.clicks_side_bar_button()
                parasearch.clicks_add_new_chat_button()
                success_message = parasearch.get_text_on_success_popup_message()
                assert success_message == expected_message, f"Expected '{expected_message}', got '{success_message}'"
                self.logger.info("New chat created successfully using sidebar buttons.")
        except NoSuchElementException:
            self.logger.warning("'Create First Chat' not found. Using sidebar fallback.")
            parasearch.clicks_side_bar_button()
            parasearch.clicks_add_new_chat_button()
            success_message = parasearch.get_text_on_success_popup_message()
            assert success_message == expected_message, f"Expected '{expected_message}', got '{success_message}'"
            self.logger.info("New chat created via fallback sidebar method.")

        # Perform paragraph search
        search_text = ReadConfig.enter_para_search_text()
        self.logger.info(f"Inputting paragraph search text: '{search_text}'")
        parasearch.set_search_bar_text(search_text)

        self.logger.info("Triggering paragraph search.")
        parasearch.clicks_search_button()

        # Scroll for visibility of response
        self.logger.info("Scrolling to bottom of page to view response.")
        self.driver.execute_script("""
            window.scrollTo({
                top: document.body.scrollHeight,
                behavior: 'smooth'
            });
        """)

        # Retrieve response
        self.logger.info("Retrieving paragraph search response text.")
        response_text_data = parasearch.get_response_text()
        print("Response Text from Para Search:", response_text_data)

        if response_text_data:
            self.logger.info("Paragraph search successful. Response received.")
            assert True
        else:
            self.logger.error("Paragraph search failed. No response text.")
            self.driver.save_screenshot("./Screenshots/test_para_search_functionality_search_failure.png")
            assert False

        time.sleep(2)  # Optional wait

        # Logout process
        self.logger.info("Initiating logout sequence.")
        parasearch.clicks_user_profile_logo()
        profilepage.click_profile_icon_on_profile_page()
        profilepage.click_logout_button_on_profile_page()
        self.logger.info("Logout completed successfully.")

        # Validate page title after logout
        act_title = self.driver.title
        self.logger.info(f"Validating page title after logout: '{act_title}'")

        if act_title == "Para":
            self.logger.info("Page title verification passed.")
            assert True
        else:
            self.logger.error("Page title verification failed.")
            self.driver.save_screenshot("./Screenshots/test_para_search_functionality_homepage_title.png")
            assert False

        # Cleanup
        self.logger.info("Closing browser and completing test.")
        self.driver.quit()

        self.logger.info("========== [TEST COMPLETED] test_para_search_functionality ==========")
