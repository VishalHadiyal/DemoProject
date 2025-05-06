import time

import pytest

from pageObject.parasearch import ParaSearch
from utilities.data_generator import *
from pageObject.homepage import HomePage
from pageObject.loginPage import LoginPage
from pageObject.signuppage import SignUPPage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class TestSignupPage:
    """
    This class contains test cases for verifying the signup functionality on the Parasors panel.
    """

    baseURL = ReadConfig.get_application_url()  # Application URL
    logger = LogGen.loggen()  # Logger instance for logging test execution details


    @pytest.mark.regression
    def test_signup_page_with_valid_data(self, setup):
        """
        Test case to verify the signup page functionality.
        """
        test_name = "test_signup_page"
        self.logger.info("********** Test 001 : TestSignupPage: Verifying Signup Page **********")
        self.driver = setup  # Setup WebDriver instance

        try:
            self.driver.get(self.baseURL)  # Navigate to the base URL
            self.logger.info(f"Navigated to {self.baseURL}")
            self.driver.maximize_window()  # Maximize the browser window

            # Initialize page objects
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            signUPPage = SignUPPage(self.driver)
            DG = DataGenerator()
            PS = ParaSearch(self.driver)

            # Generate test data
            email = DG.generate_unique_email()
            mobile_number = DG.generate_mobile_number()
            self.logger.info(f"Generated test email: {email}, mobile: {mobile_number}")

            # Perform Signup flow
            homepage.click_explore_AI_button()
            self.logger.info("Clicked on 'Explore AI' button on homepage")

            login_page.click_signup()
            self.logger.info("Clicked on 'Sign Up' button on login page")

            signUPPage.set_Full_Name(ReadConfig.set_full_name_text())
            signUPPage.set_Email(email)
            signUPPage.set_Mobile_Number(mobile_number)
            signUPPage.set_City(ReadConfig.set_city_text())
            signUPPage.set_password(ReadConfig.set_password_text())
            self.logger.info("Entered user details on signup form")

            signUPPage.click_Join_Now()
            self.logger.info("Clicked on 'Join Now' button")

            expectedtext = ReadConfig.set_confirm_text()
            actuletext = PS.get_text_on_confirm_register_popup()
            self.logger.info(f"Expected confirmation text: {expectedtext}")
            self.logger.info(f"Actual confirmation text: {actuletext}")

            assert expectedtext == actuletext, "Confirmation text mismatch"

            self.logger.info("Text on Confirm Register Popup is correct")
            PS.clicks_ok_button_on_confirm_register_popup()
            self.logger.info("Clicked 'OK' on confirmation popup")

            self.logger.info("********** TestSignupPage: Signup Page Verification Completed Successfully **********")

        except Exception as e:
            self.logger.error("********** TestSignupPage: Signup Page Verification FAILED **********")
            self.logger.error(f"Exception occurred: {e}")

            # Capture screenshot on failure
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to: {screenshot_path}")

            assert False, f"Test failed due to exception: {e}"

        finally:
            self.driver.quit()

    @pytest.mark.regression
    def test_without_entering_data_in_mandatory_fields(self, setup):
        """
        Test case to verify error messages when mandatory fields are left empty on the signup page.
        """
        test_name = "test_signup_page"
        self.logger.info("********** Test 002 : Verifying Signup Page Mandatory Fields **********")
        self.driver = setup

        try:
            self.driver.get(self.baseURL)
            self.logger.info(f"Navigated to {self.baseURL}")
            self.driver.maximize_window()

            # Initialize page objects
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            sign_up_page = SignUPPage(self.driver)

            # Perform Signup flow
            homepage.click_explore_AI_button()
            self.logger.info("Clicked on 'Explore AI' button")

            login_page.click_signup()
            self.logger.info("Clicked on 'Sign Up' button")

            sign_up_page.click_Student_Plan()
            self.logger.info("Clicked on 'Student Plan' button")
            explabel = sign_up_page.get_Label_Text_Select_College()
            self.logger.info(f"Label text for 'Select College': {explabel}")
            expectlabel = ReadConfig.get_student_drop_down_text()
            assert expectlabel == explabel, "Label text mismatch for 'Select College'"
            self.logger.info("Label text for 'Select College' is correct")

            sign_up_page.click_Professional_Plan()
            self.logger.info("Clicked on 'Professional Plan' button")

            sign_up_page.click_Join_Now()
            self.logger.info("Clicked on 'Join Now' button without entering mandatory fields")


            # Get expected and actual error messages
            expected_errors = {
                "full_name": ReadConfig.error_message_full_name(),
                "email": ReadConfig.error_message_email(),
                "mobile": ReadConfig.error_message_mobile_number(),
                "password": ReadConfig.error_message_password()
            }

            actual_errors = {
                "full_name": sign_up_page.get_Error_Message_Full_Name(),
                "email": sign_up_page.get_Error_Message_Email(),
                "mobile": sign_up_page.get_Error_Message_Mobile_Number(),
                "password": sign_up_page.get_Error_Message_Password()
            }

            if expected_errors == actual_errors:
                self.logger.info("All error messages for mandatory fields are displayed correctly")
            else:
                self.logger.error("Mismatch in error messages for mandatory fields")
                self.logger.error(f"Expected: {expected_errors}")
                self.logger.error(f"Actual: {actual_errors}")
                assert False, "Error messages mismatch"

        except Exception as e:
            self.logger.error("********** Signup Page Verification FAILED **********")
            self.logger.error(f"Exception occurred: {e}")
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to: {screenshot_path}")
            assert False, f"Test failed due to exception: {e}"

        finally:
            self.driver.quit()

    @pytest.mark.regression
    def test_verify_page_text(self, setup):
        """
        Test case to verify the text on the signup page.
        """
        test_name = "test_signup_page"
        self.logger.info("********** Test 003 : Verifying Signup Page Text **********")

        # Assign WebDriver instance
        self.driver = setup

        try:
            # Navigate to the base URL
            self.driver.get(self.baseURL)
            self.logger.info(f"Navigated to {self.baseURL}")

            # Maximize the browser window
            self.driver.maximize_window()
            self.logger.info("Browser window maximized")

            # Initialize page object models
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            sign_up_page = SignUPPage(self.driver)
            self.logger.info("Page objects initialized")

            # Click on 'Explore AI' button on the home page
            homepage.click_explore_AI_button()
            self.logger.info("Clicked on 'Explore AI' button")

            # Click on 'Sign Up' button on the login page
            login_page.click_signup()
            self.logger.info("Clicked on 'Sign Up' button")

            # Retrieve actual text from the signup page
            ActualText = sign_up_page.get_Text_of_the_page()
            self.logger.info("Retrieved text from the signup page")

            # Fetch expected text from configuration
            ExpectedText = ReadConfig.get_signup_page_text()
            self.logger.info(f"Expected text: {ExpectedText}")
            self.logger.info(f"Actual text: {ActualText}")

            # Assert that actual text matches expected text
            assert ExpectedText == ActualText, "Text mismatch on signup page"
            self.logger.info("Text on Signup Page is correct")
            self.logger.info("********** Signup Page Text Verification Completed Successfully **********")

        except Exception as e:
            # Log error details and capture screenshot on failure
            self.logger.error("********** Signup Page Text Verification FAILED **********")
            self.logger.error(f"Exception occurred: {e}")
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to: {screenshot_path}")

            # Fail the test explicitly
            assert False, f"Test failed due to exception: {e}"

        finally:
            # Ensure the browser is closed after test execution
            self.driver.quit()
            self.logger.info("Browser closed")

    @pytest.mark.regression
    def test_password_show_functionality(self, setup):
        """
        Test case to verify the password show/hide functionality on the signup page.
        """
        test_name = "test_password_show_functionality"
        self.logger.info("********** Test 004 : Verifying Password Show/Hide Functionality **********")
        self.driver = setup

        try:
            # Launch browser and navigate to base URL
            self.driver.get(self.baseURL)
            self.logger.info(f"Navigated to {self.baseURL}")
            self.driver.maximize_window()

            # Initialize page objects
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            sign_up_page = SignUPPage(self.driver)

            # Navigate to Sign Up page via HomePage and LoginPage
            homepage.click_explore_AI_button()
            self.logger.info("Clicked on 'Explore AI' button")

            login_page.click_signup()
            self.logger.info("Clicked on 'Sign Up' button")
            time.sleep(2)

            # Enter test password
            test_password = ReadConfig.set_password_text()
            sign_up_page.set_password(test_password)
            self.logger.info("Entered password")
            time.sleep(2)

            # Toggle show/hide password functionality
            sign_up_page.click_Password_Show()
            self.logger.info("Clicked on 'Show Password' button")
            time.sleep(2)

            sign_up_page.click_Password_Show()
            self.logger.info("Clicked on 'Show Password' button again to hide")
            time.sleep(2)

            # Check if password is visible
            if sign_up_page.set_password(ReadConfig.set_password_text()) != "text":
                self.logger.info("Password is visible")
            else:
                self.logger.error("Password is not visible")
                assert False, "Password visibility check failed"

            self.logger.info("********** Password Show/Hide Functionality Verification PASSED **********")

        except Exception as e:
            self.logger.error("********** Password Show/Hide Functionality Verification FAILED **********")
            self.logger.error(f"Exception occurred: {e}")
            self.driver.save_screenshot(f"./Screenshots/{test_name}.png")
            assert False, f"Test failed due to exception: {e}"

        finally:
            # Ensure browser is closed after test
            self.logger.info("Closing the browser")
            self.driver.quit()

    @pytest.mark.smoke
    def test_signup_page_with_valid_data_for_student(self, setup):
        """
        Test case to verify the signup page functionality for a student using valid data.
        This includes navigating through the homepage, accessing the signup page,
        filling out the form with generated test data, and verifying the confirmation message.
        """
        test_name = "test_signup_page"
        self.logger.info("********** Test 005 : TestSignupPage: Verifying Signup Page **********")
        self.driver = setup  # Setup WebDriver instance

        try:
            # Navigate to the application base URL
            self.driver.get(self.baseURL)
            self.logger.info(f"Navigated to URL: {self.baseURL}")

            # Maximize the browser window
            self.driver.maximize_window()
            self.logger.info("Browser window maximized")

            # Initialize page object classes
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            signUPPage = SignUPPage(self.driver)
            DG = DataGenerator()
            PS = ParaSearch(self.driver)

            # Generate dynamic test data
            email = DG.generate_unique_email_with_edu()
            mobile_number = DG.generate_mobile_number()
            self.logger.info(f"Generated test email: {email}")
            self.logger.info(f"Generated test mobile number: {mobile_number}")

            # Click on 'Explore AI' from homepage
            homepage.click_explore_AI_button()
            self.logger.info("Clicked on 'Explore AI' button on homepage")

            # Navigate to signup page via login page
            login_page.click_signup()
            self.logger.info("Clicked on 'Sign Up' button on login page")

            # Choose the 'Student Plan'
            signUPPage.click_Student_Plan()
            self.logger.info("Clicked on 'Student Plan' button")

            # Fill the signup form with valid data
            signUPPage.set_Full_Name(ReadConfig.set_full_name_text())
            self.logger.info("Entered full name")

            signUPPage.set_Email(email)
            self.logger.info("Entered email address")

            signUPPage.set_Mobile_Number(mobile_number)
            self.logger.info("Entered mobile number")

            signUPPage.set_City(ReadConfig.set_city_text())
            self.logger.info("Entered city")

            signUPPage.select_College()
            self.logger.info("Selected college")

            signUPPage.select_College_from_dropdown()
            self.logger.info("Selected college from dropdown")

            signUPPage.upload_ID_Proof()
            fil_name = signUPPage.get_Uploaded_File_Name()
            self.logger.info(f"Uploaded ID proof file: {fil_name}")

            signUPPage.set_password(ReadConfig.set_password_text())
            self.logger.info("Entered password")

            # Submit the signup form
            signUPPage.click_Join_Now()
            self.logger.info("Clicked on 'Join Now' button")

            # Verify the confirmation message after successful registration
            expectedtext = ReadConfig.set_confirm_text()
            actuletext = PS.get_text_on_confirm_register_popup()
            self.logger.info(f"Expected confirmation text: {expectedtext}")
            self.logger.info(f"Actual confirmation text: {actuletext}")

            assert expectedtext == actuletext, "Confirmation text mismatch"
            self.logger.info("Confirmation text matched successfully")

            # Click OK on confirmation popup
            PS.clicks_ok_button_on_confirm_register_popup()
            self.logger.info("Clicked 'OK' on confirmation popup")

            self.logger.info("********** TestSignupPage: Signup Page Verification Completed Successfully **********")

        except Exception as e:
            self.logger.error("********** TestSignupPage: Signup Page Verification FAILED **********")
            self.logger.error(f"Exception occurred: {e}")

            # Capture screenshot on failure
            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved to: {screenshot_path}")

            # Fail the test
            assert False, f"Test failed due to exception: {e}"

        finally:
            # Close the browser session
            self.driver.quit()
            self.logger.info("Browser session ended and driver quit")


    @pytest.mark.regression
    def test_signup_page_with_invalid_emailID(self, setup):
        """
        Test Case: test_signup_page_with_invalid_emailID
        Objective: Verify that the signup form correctly handles invalid email IDs and displays the expected error message.
        """
        test_name = "test_signup_page_with_invalid_emailID"
        self.logger.info("========== Test 006: Verifying Signup Page with Invalid Email ID ==========")

        # Assign the setup WebDriver instance
        self.driver = setup

        try:
            # Step 1: Navigate to the application base URL
            self.logger.info(f"Navigating to application URL: {self.baseURL}")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.logger.info("Browser window maximized")

            # Step 2: Initialize Page Objects and Data Generator
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            signUPPage = SignUPPage(self.driver)
            DG = DataGenerator()

            # Step 3: Generate test data with invalid email
            email = DG.generate_invalid_email()
            mobile_number = DG.generate_mobile_number()
            self.logger.info(f"Generated test data - Email: {email}, Mobile Number: {mobile_number}")

            # Step 4: Begin signup process
            self.logger.info("Clicking on 'Explore AI' button from homepage")
            homepage.click_explore_AI_button()

            self.logger.info("Navigating to signup page from login page")
            login_page.click_signup()

            # Step 5: Fill in the signup form with test data
            self.logger.info("Filling in user details on signup form")
            signUPPage.set_Full_Name(ReadConfig.set_full_name_text())
            signUPPage.set_Email(email)
            signUPPage.set_Mobile_Number(mobile_number)
            signUPPage.set_City(ReadConfig.set_city_text())
            signUPPage.set_password(ReadConfig.set_password_text())

            # Step 6: Submit the signup form
            self.logger.info("Submitting the signup form by clicking 'Join Now'")
            signUPPage.click_Join_Now()

            # Step 7: Verify error message for invalid email input
            expected_text = ReadConfig.error_message_email()
            actual_text = signUPPage.get_Error_Message_Email()

            self.logger.info(f"Expected error message: {expected_text}")
            self.logger.info(f"Actual error message received: {actual_text}")

            assert expected_text == actual_text, "Error message mismatch for invalid email"

            self.logger.info("Test Passed: Signup page correctly handled invalid email input")

        except Exception as e:
            # Log the failure and take a screenshot
            self.logger.error("Test Failed: Exception occurred during signup test with invalid email")
            self.logger.error(f"Exception details: {e}", exc_info=True)

            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Failure screenshot saved at: {screenshot_path}")

            assert False, f"Test failed due to exception: {e}"

        finally:
            self.logger.info("Closing the browser session")
            self.driver.quit()

    @pytest.mark.regression
    def test_signup_invalid_mobile_number_wrong_start(self, setup):
        """
        Test Case: test_signup_page_with_invalid_emailID
        Objective: Verify that the signup form correctly handles invalid email IDs and displays the expected error message.
        """
        test_name = "test_signup_page_with_invalid_emailID"
        self.logger.info("========== Test 007: Verifying Signup Page with Invalid Email ID ==========")

        # Assign the setup WebDriver instance
        self.driver = setup

        try:
            # Step 1: Navigate to the application base URL
            self.logger.info(f"Step 1: Navigating to application URL: {self.baseURL}")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.logger.info("Browser window maximized")

            # Step 2: Initialize Page Objects and Data Generator
            self.logger.info("Step 2: Initializing Page Objects and Data Generator")
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            signUPPage = SignUPPage(self.driver)
            DG = DataGenerator()

            # Step 3: Generate test data with invalid mobile number
            self.logger.info("Step 3: Generating test data with invalid mobile number")
            email = DG.generate_unique_email()
            mobile_number = DG.generate_invalid_mobile_number()
            self.logger.info(f"Generated test data - Email: {email}, Mobile Number: {mobile_number}")

            # Step 4: Begin signup process
            self.logger.info("Step 4: Navigating through homepage to signup page")
            self.logger.info("Clicking on 'Explore AI' button from homepage")
            homepage.click_explore_AI_button()

            self.logger.info("Navigating to signup page from login page")
            login_page.click_signup()

            # Step 5: Fill in the signup form with test data
            self.logger.info("Step 5: Filling in user details on signup form")
            signUPPage.set_Full_Name(ReadConfig.set_full_name_text())
            signUPPage.set_Email(email)
            signUPPage.set_Mobile_Number(mobile_number)
            signUPPage.set_City(ReadConfig.set_city_text())
            signUPPage.set_password(ReadConfig.set_password_text())

            # Step 6: Submit the signup form
            self.logger.info("Step 6: Submitting the signup form by clicking 'Join Now'")
            signUPPage.click_Join_Now()

            # Step 7: Verify error message for invalid mobile number input
            self.logger.info("Step 7: Verifying error message for invalid mobile number")
            expected_text = ReadConfig.error_message_mobile_number()
            actual_text = signUPPage.get_Error_Message_Mobile_Number()

            self.logger.info(f"Expected error message: {expected_text}")
            self.logger.info(f"Actual error message received: {actual_text}")

            # Assertion to validate the correctness of the error handling
            assert expected_text == actual_text, "Error message mismatch for invalid mobile number"

            self.logger.info("Test Passed: Signup page correctly handled invalid mobile number input")

        except Exception as e:
            # Log the failure and take a screenshot
            self.logger.error("Test Failed: Exception occurred during signup test with invalid mobile number")
            self.logger.error(f"Exception details: {e}", exc_info=True)

            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Failure screenshot saved at: {screenshot_path}")

            # Fail the test
            assert False, f"Test failed due to exception: {e}"

        finally:
            # Cleanup
            self.logger.info("Closing the browser session")
            self.driver.quit()

    @pytest.mark.regression
    def test_signup_with_invalid_name(self, setup):
        """
        Test Case: test_signup_page_with_invalid_name
        Objective: Verify that the signup form correctly handles invalid email IDs and displays the expected error message.
        """

        test_name = "test_signup_page_with_invalid_name"
        self.logger.info("========== Test 008: Verifying Signup Page with Invalid Name ==========")

        # Assign the setup WebDriver instance to the test
        self.driver = setup

        try:
            # Step 1: Navigate to the application base URL
            self.logger.info(f"Step 1: Navigating to application URL: {self.baseURL}")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.logger.info("Browser window maximized successfully")

            # Step 2: Initialize Page Object classes and the data generator utility
            self.logger.info("Step 2: Initializing Page Objects and Data Generator")
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            signUPPage = SignUPPage(self.driver)
            DG = DataGenerator()
            self.logger.info("Page Objects and Data Generator initialized successfully")

            # Step 3: Generate test data with an invalid full name
            self.logger.info("Step 3: Generating test data for signup form")
            email = DG.generate_unique_email()
            mobile_number = DG.generate_mobile_number()
            self.logger.info(f"Generated Email: {email}")
            self.logger.info(f"Generated Mobile Number: {mobile_number}")

            # Step 4: Navigate to signup page through the homepage
            self.logger.info("Step 4: Navigating from homepage to signup page")
            self.logger.info("Clicking on 'Explore AI' button")
            homepage.click_explore_AI_button()
            self.logger.info("Clicked on 'Explore AI' button")

            self.logger.info("Clicking on 'Signup' link on Login Page")
            login_page.click_signup()
            self.logger.info("Navigated to Signup Page")

            # Step 5: Fill the signup form with test data including an invalid full name
            self.logger.info("Step 5: Filling in signup form with test data")
            invalid_name = DG.generate_two_char_string_name()
            self.logger.info(f"Using invalid full name: {invalid_name}")
            signUPPage.set_Full_Name(invalid_name)
            signUPPage.set_Email(email)
            signUPPage.set_Mobile_Number(mobile_number)
            signUPPage.set_City(ReadConfig.set_city_text())
            signUPPage.set_password(ReadConfig.set_password_text())
            self.logger.info("Filled all fields in signup form")

            # Step 6: Submit the signup form
            self.logger.info("Step 6: Submitting the signup form by clicking 'Join Now'")
            signUPPage.click_Join_Now()
            self.logger.info("Clicked on 'Join Now'")

            # Step 7: Validate the error message shown for invalid full name input
            self.logger.info("Step 7: Verifying error message for invalid full name input")
            expected_text = ReadConfig.error_message_full_name()
            actual_text = signUPPage.get_Error_Message_Full_Name()
            self.logger.info(f"Expected Error Message: {expected_text}")
            self.logger.info(f"Actual Error Message: {actual_text}")

            # Assertion to verify error handling
            assert expected_text == actual_text, "Error message mismatch for invalid full name"
            self.logger.info("Test Passed: Signup page correctly handled invalid full name input")

        except Exception as e:
            # Log exception details and capture screenshot
            self.logger.error("Test Failed: Exception occurred during signup with invalid full name")
            self.logger.error(f"Exception Details: {e}", exc_info=True)

            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot captured and saved at: {screenshot_path}")

            # Fail the test explicitly
            assert False, f"Test failed due to exception: {e}"

        finally:
            # Close browser session
            self.logger.info("Closing the browser session")
            self.driver.quit()

    @pytest.mark.ui
    def test_signup_with_invalid_password(self, setup):
        """
        Test Case: test_signup_with_invalid_password
        Objective: Verify that the signup form correctly handles an invalid password
                   and displays the appropriate error message.
        """

        test_name = "test_signup_with_invalid_password"
        self.logger.info("========== Test 009: Verifying Signup Page with Invalid Password ==========")

        # Assign the setup WebDriver instance to the test
        self.driver = setup

        try:
            # Step 1: Navigate to the application base URL
            self.logger.info(f"Step 1: Navigating to the application URL: {self.baseURL}")
            self.driver.get(self.baseURL)
            self.driver.maximize_window()
            self.logger.info("Browser window maximized successfully")

            # Step 2: Initialize required Page Objects and Data Generator
            self.logger.info("Step 2: Initializing Page Objects and Data Generator")
            login_page = LoginPage(self.driver)
            homepage = HomePage(self.driver)
            signUPPage = SignUPPage(self.driver)
            DG = DataGenerator()
            self.logger.info("Page Objects and Data Generator initialized successfully")

            # Step 3: Generate valid test data with an invalid password
            self.logger.info("Step 3: Generating test data for the signup form")
            email = DG.generate_unique_email()
            mobile_number = DG.generate_mobile_number()
            self.logger.info(f"Generated test email: {email}")
            self.logger.info(f"Generated test mobile number: {mobile_number}")

            # Step 4: Navigate from the homepage to the signup page
            self.logger.info("Step 4: Navigating to the Signup Page")
            self.logger.info("Clicking 'Explore AI' button on homepage")
            homepage.click_explore_AI_button()
            self.logger.info("'Explore AI' button clicked")

            self.logger.info("Clicking 'Signup' link on the Login Page")
            login_page.click_signup()
            self.logger.info("Navigated to the Signup Page")

            # Step 5: Fill the signup form with an invalid password (e.g., too short)
            self.logger.info("Step 5: Filling the signup form with invalid password")
            signUPPage.set_Full_Name(ReadConfig.set_full_name_text())
            signUPPage.set_Email(email)
            signUPPage.set_Mobile_Number(mobile_number)
            signUPPage.set_City(ReadConfig.set_city_text())
            time.sleep(5)
            signUPPage.set_password(DG.generate_six_digit_password())  # Intentionally short/invalid password
            self.logger.info("All signup form fields filled")
            time.sleep(5)
            # Step 6: Submit the signup form
            self.logger.info("Step 6: Submitting the signup form")
            signUPPage.click_Join_Now()
            self.logger.info("'Join Now' button clicked")

            # Step 7: Verify the error message for the invalid password
            self.logger.info("Step 7: Validating the error message for invalid password")
            expected_text = ReadConfig.error_message_password()
            actual_text = signUPPage.get_Error_Message_Password()
            self.logger.info(f"Expected Error Message: '{expected_text}'")
            self.logger.info(f"Actual Error Message: '{actual_text}'")

            # Assertion to check if actual error matches the expected one
            assert expected_text == actual_text, "Error message mismatch for invalid password"
            self.logger.info("Test Passed: Signup page correctly displayed error for invalid password")

        except Exception as e:
            # Log the error and take a screenshot for debugging
            self.logger.error("Test Failed: Exception occurred during signup with invalid password")
            self.logger.error(f"Exception Details: {e}", exc_info=True)

            screenshot_path = f"./Screenshots/{test_name}_failure.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved at: {screenshot_path}")

            # Fail the test explicitly
            assert False, f"Test failed due to exception: {e}"

        finally:
            # Clean up and close the browser
            self.logger.info("Closing the browser session")
            self.driver.quit()
