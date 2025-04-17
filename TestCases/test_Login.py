import pytest

from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig
from pageObject.loginPage import LoginPage
from pageObject.parasearch import ParaSearch
from pageObject.homepage import HomePage
from pageObject.profilepage import ProfilePage


class Test001Login:
    """
    This class contains test cases for verifying the login functionality on the Parasors panel.
    """

    # Retrieve configuration details from ReadConfig class
    baseURL = ReadConfig.get_application_url()  # Application URL
    username = ReadConfig.get_user_email()  # Admin username
    password = ReadConfig.get_user_password()  # Admin password
    logger = LogGen.loggen()  # Logger instance for logging test execution details

    @pytest.mark.ui
    def test_homepage_title(self, setup):
        """
        Test case to verify the homepage title of the application.
        """
        self.logger.info("********** Test_001_Login: Verifying HomePage Title **********")

        self.driver = setup  # Setup WebDriver instance
        self.driver.get(self.baseURL)  # Navigate to the base URL
        act_title = self.driver.title  # Capture the actual page title

        # Validate if the title matches the expected value
        if act_title == "Para":
            self.logger.info("HomePage Title Verification Passed")
            assert True  # Test passes if the title is correct
        else:
            self.logger.error("HomePage Title Verification Failed")
            self.driver.save_screenshot("./Screenshots/test_homepage_title.png")  # Capture a screenshot on failure
            assert False  # Fail the test case

        self.driver.quit()  # Ensure browser closure after test execution

    @pytest.mark.functional
    def test_login(self, setup):
        """
        Test case to verify successful login functionality.
        """
        self.logger.info("********** Test_001_Login: Login Test Started **********")

        self.driver = setup
        self.driver.get(self.baseURL)  # Navigate to the application URL

        # Create instances of page object classes
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        parasearch = ParaSearch(self.driver)

        # Perform login actions
        self.logger.info("Clicking login button on the homepage")
        homepage.click_login_button()

        self.logger.info("Entering username")
        loginpage.set_username(self.username)

        self.logger.info("Entering password")
        loginpage.set_password(self.password)

        self.logger.info("Clicking login button")
        loginpage.click_login()

        # Allow time for the login process to complete
        self.driver.implicitly_wait(10)

        # Retrieve the success message from the application UI
        success_message = parasearch.get_success_alert_text()

        # Validate the login success message
        if success_message == "Login Successful !":
            self.logger.info("Login Test Passed: Toaster message - Login Successful!")
            assert True
        else:
            self.logger.error(f"Login Test Failed: Unexpected Toaster Message - {success_message}")
            self.driver.save_screenshot("./Screenshots/test_login_failure.png")
            assert False  # Fail the test case

        self.driver.quit()  # Ensure browser closure after test execution

    @pytest.mark.functional
    def test_login_to_logout_flow(self, setup):
        """
        Test case to verify successful login and logout functionality.
        """
        self.logger.info("********** Test_001_Login: Login to Logout Flow Test Started **********")

        self.driver = setup
        self.driver.get(self.baseURL)

        # Create instances of page object classes
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        parasearch = ParaSearch(self.driver)
        profilepage = ProfilePage(self.driver)

        # Perform login actions
        self.logger.info("Clicking login button on the homepage")
        homepage.click_login_button()

        self.logger.info("Entering username")
        loginpage.set_username(self.username)

        self.logger.info("Entering password")
        loginpage.set_password(self.password)

        self.logger.info("Clicking login button")
        loginpage.click_login()

        # Allow time for the login process to complete
        self.driver.implicitly_wait(10)

        # Retrieve and validate the login success message
        success_message = parasearch.get_success_alert_text()
        if success_message == "Login Successful !":
            self.logger.info("Login Test Passed: Toaster message - Login Successful!")
        else:
            self.logger.error(f"Login Test Failed: Unexpected Toaster Message - {success_message}")
            self.driver.save_screenshot("./Screenshots/test_login_failure.png")
            assert False  # Fail the test case

        # Perform logout actions
        self.logger.info("Logging out of the application")
        parasearch.clicks_user_profile_logo()
        profilepage.click_profile_icon_on_profile_page()
        profilepage.click_logout_button_on_profile_page()

        self.logger.info("Logout successful")

        # Validate if the title matches the expected value
        act_title = self.driver.title  # Capture the actual page title

        if act_title == "Para":
            self.logger.info("HomePage Title Verification Passed")
            assert True  # Test passes if the title is correct
        else:
            self.logger.error("HomePage Title Verification Failed")
            self.driver.save_screenshot("./Screenshots/test_homepage_title.png")  # Capture a screenshot on failure
            assert False  # Fail the test case

        self.driver.quit()  # Ensure browser closure after test execution
