import time

import pytest
from pageObject.homepage import HomePage
from pageObject.pricingpage import PricingPage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class TestPricingPage:
    base_url = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_pricing_page_title(self, setup):
        """
        Test case to verify the page URL of the Pricing Page after navigation.

        :param setup: WebDriver instance provided by the pytest fixture.
        """
        self.logger.info("********** Test_001_PricingPage **********")
        driver = setup  # Get the WebDriver instance from the setup fixture

        try:
            # Navigate to the base URL and maximize the browser window
            driver.get(self.base_url)
            driver.maximize_window()

            # Initialize the HomePage object
            homepage = HomePage(driver)

            # Navigate to the Pricing Page by simulating a user click on the appropriate element
            homepage.navigate_to_pricing_page()

            # Fetch the expected URL of the Pricing Page from configuration
            expected_url = ReadConfig.get_pricing_page_url()

            # Capture the current URL from the browser after navigation
            actual_url = driver.current_url

            # Log both expected and actual URLs for debugging
            self.logger.info(f"Expected URL: {expected_url}")
            self.logger.info(f"Actual URL: {actual_url}")

            # Assertion to ensure the actual URL matches the expected URL
            assert actual_url == expected_url, \
                f"URL mismatch: expected {expected_url}, got {actual_url}"

        except AssertionError as e:
            # On assertion failure, take a screenshot and log the error for debugging
            screenshot_path = "./Screenshots/test_pricing_page_title_failure.png"
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise  # Re-raise the exception to mark the test as failed

        finally:
            # Ensure the browser is closed after test completion
            driver.quit()
            self.logger.info("********** Test_001_PricingPage Completed **********")

    @pytest.mark.skip
    def test_pricing_page_content(self, setup):
        """
        Test case to verify the 'Free Trial' section content on the Pricing Page.

        :param setup: WebDriver instance provided by the pytest fixture.
        """
        self.logger.info("********** Test_002_PricingPage **********")
        driver = setup

        try:
            # Open the target URL and maximize the browser window
            driver.get(self.base_url)
            driver.maximize_window()

            # Initialize page object models
            homepage = HomePage(driver)
            pricingpage = PricingPage(driver)

            # Navigate to the Pricing Page via homepage actions
            homepage.navigate_to_pricing_page()

            # Get the expected 'Free Trial' text from the config file
            expectedContent = ReadConfig.get_free_trial_content_text()

            # Retrieve the actual text shown on the Pricing Page
            actuleContent = pricingpage.get_free_trial_text()

            # Log both expected and actual content for reference
            self.logger.info(f"Expected Content: {expectedContent}")
            self.logger.info(f"Actual Content: {actuleContent}")

            # Assertion to compare expected and actual values
            assert actuleContent == expectedContent, \
                f"Content mismatch: expected {expectedContent}, got {actuleContent}"

        except AssertionError as e:
            # Take a screenshot on assertion failure and log the details
            screenshot_path = "./Screenshots/test_pricing_page_content_failure.png"
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise  # Re-raise the exception to mark the test as failed

        finally:
            # Close the browser after the test
            driver.quit()
            self.logger.info("********** Test_002_PricingPage Completed **********")

    @pytest.mark.skip
    def test_general_plan_text(self, setup):
        """
        Test case to verify the content of the General Plan section on the Pricing Page.

        :param setup: WebDriver instance provided by the pytest fixture.
        """
        self.logger.info("********** Test_003_PricingPage **********")
        driver = setup

        try:
            # Navigate to the base URL and maximize the browser window
            driver.get(self.base_url)
            driver.maximize_window()

            # Initialize page objects for HomePage and PricingPage
            homepage = HomePage(driver)
            pricingpage = PricingPage(driver)

            # Navigate from the homepage to the pricing page
            homepage.navigate_to_pricing_page()  # Clicks on the 'Pricing' option in the header

            # Retrieve the expected text for the general plan from configuration
            expectedContent = ReadConfig.get_general_plan_text()

            # Get the actual text displayed on the Pricing page for the general plan
            actuleContent = pricingpage.get_all_the_plan_text_values_common_method()

            # Log both expected and actual content for debugging purposes
            self.logger.info(f"Expected Content: {expectedContent}")
            self.logger.info(f"Actual Content: {actuleContent}")

            # Perform assertion to verify if the actual content matches the expected content
            assert actuleContent == expectedContent, \
                f"Content mismatch: expected {expectedContent}, got {actuleContent}"

        except AssertionError as e:
            # In case of assertion failure, take a screenshot and log the error
            screenshot_path = "./Screenshots/test_pricing_page_content_failure.png"
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise  # Re-raise the exception to mark the test as failed

        finally:
            # Ensure the browser is closed after the test completes
            driver.quit()
            self.logger.info("********** Test_003_PricingPage Completed **********")

# ====================== Parameterized Test Cases ======================
# ====================== Test Cases for Pricing Page =====================
# ====================== Test all the Plan Text =====================
    @pytest.mark.skip
    @pytest.mark.parametrize(
        "plan_type, get_expected_content_method, click_plan_method",
        [
            # Plan type, method to fetch expected content, method name to click corresponding UI tab
            ("Student", ReadConfig.get_student_plan_text, "click_student_plan"),
            ("General", ReadConfig.get_general_plan_text, "click_general_plan"),
            ("TopUp", ReadConfig.get_top_up_plan_text, "click_top_up_plan"),
            ("GiftVoucher", ReadConfig.get_gift_voucher_text, "click_gift_voucher"),
        ]
    )
    def test_pricing_plan_text(self, setup, plan_type, get_expected_content_method, click_plan_method):
        """
        Parameterized test to verify pricing plan sections (e.g., Student, General, TopUp, GiftVoucher) on the Pricing Page.

        :param setup: WebDriver instance from pytest fixture.
        :param plan_type: The type of pricing plan (e.g., "Student", "General", etc.).
        :param get_expected_content_method: Reference to the method that returns expected plan content from config.
        :param click_plan_method: Name of the method to click the plan tab on the UI.
        """
        self.logger.info(f"********** Test_004_PricingPage - {plan_type} Plan **********")
        driver = setup

        try:
            # Navigate to the application URL and maximize the browser window
            driver.get(self.base_url)
            driver.maximize_window()

            # Initialize Page Object Models
            homepage = HomePage(driver)
            pricingpage = PricingPage(driver)

            # Navigate to the Pricing Page
            homepage.navigate_to_pricing_page()

            # Click on the appropriate plan tab using dynamic method call
            getattr(pricingpage, click_plan_method)()

            # Get the expected and actual text content
            expected_content = get_expected_content_method()
            actual_content = pricingpage.get_all_the_plan_text_values_common_method()

            # Log the expected and actual content for debugging
            self.logger.info(f"Expected {plan_type} Plan Content: {expected_content}")
            self.logger.info(f"Actual {plan_type} Plan Content: {actual_content}")

            # Assert that the content matches
            assert actual_content == expected_content, \
                f"{plan_type} Plan content mismatch: expected {expected_content}, got {actual_content}"

        except AssertionError as e:
            # Capture a screenshot on assertion failure
            screenshot_path = f"./Screenshots/test_pricing_page_{plan_type.lower()}_failure.png"
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed for {plan_type} Plan: {e}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            # Always quit the driver
            driver.quit()
            self.logger.info(f"********** Test_004_PricingPage - {plan_type} Plan Completed **********")

    @pytest.mark.skip
    def test_note_text(self, setup):
        """
        Test case to verify the note text on the Pricing Page and
        check the content under Section 29 of Terms and Conditions.

        :param setup: WebDriver instance provided by the pytest fixture.
        """
        self.logger.info("********** Test_005_PricingPage **********")
        driver = setup

        try:
            # Open the application URL and maximize the browser window
            driver.get(self.base_url)
            driver.maximize_window()

            # Initialize Page Object Models for HomePage and PricingPage
            homepage = HomePage(driver)
            pricingpage = PricingPage(driver)

            # Navigate to the Pricing Page from the Home Page
            homepage.navigate_to_pricing_page()

            # Get the expected note text from the configuration
            note_expected_text = ReadConfig.get_note_expected_text()

            # Get the actual note text displayed on the Pricing Page
            note_actual_text = pricingpage.get_note_text()

            # Log the expected and actual note texts
            self.logger.info(f"Expected Note Content: {note_expected_text}")
            self.logger.info(f"Actual Note Content: {note_actual_text}")

            # Assert that the note content matches the expected value
            assert note_actual_text == note_expected_text, \
                f"Note content mismatch: expected '{note_expected_text}', got '{note_actual_text}'"

            # Click on the 'Terms and Conditions' section
            pricingpage.click_terms_and_conditions()

            # Get expected and actual text for Section 29 of Terms and Conditions
            section_29_expected_text = ReadConfig.get_section_29_text_values()
            section_29_actual_text = pricingpage.get_section_29_text()

            # Log the expected and actual Section 29 content
            self.logger.info(f"Expected Section 29 Content: {section_29_expected_text}")
            self.logger.info(f"Actual Section 29 Content: {section_29_actual_text}")

            # Assert that the Section 29 content matches the expected value
            assert section_29_actual_text == section_29_expected_text, \
                f"Section 29 content mismatch: expected '{section_29_expected_text}', got '{section_29_actual_text}'"

        except AssertionError as e:
            # Handle assertion failure by logging the error and taking a screenshot
            screenshot_path = "./Screenshots/test_pricing_page_note_failure.png"
            driver.save_screenshot(screenshot_path)
            self.logger.error(f"Assertion failed: {e}")
            self.logger.error(f"Screenshot saved at: {screenshot_path}")
            raise

        finally:
            # Cleanup: Close the browser window
            driver.quit()
            self.logger.info("********** Test_005_PricingPage Completed **********")