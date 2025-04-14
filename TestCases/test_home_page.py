from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig
from pageObject.homepage import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestHomePage:
    """
    Test class for verifying the Home Page functionality.
    """

    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()  # Initialize logger

    def test_home_page_title(self, setup):
        """
        Test case to verify the home page title.
        """
        self.logger.info("========== TestHomePage: Home Page Title Verification Started ==========")

        self.driver = setup  # Initialize WebDriver
        self.driver.get(self.baseURL)  # Open application URL
        self.logger.info(f"Navigated to {self.baseURL}")

        # Wait for the page to load completely
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Initialize HomePage object
        homepage = HomePage(self.driver)

        # Scroll until the 'Latest Opinion' section is visible
        self.logger.info("Scrolling to 'Latest Opinion' section.")

        try:
            latest_opinion_element = homepage.scroll_until_element_visible()
            latest_opinion_text = latest_opinion_element.text
            self.logger.info(f"Fetched latest opinion text: {latest_opinion_text}")

            # Validate the text
            assert latest_opinion_text == "Latest Opinion", "Home Page Title Verification Failed"
            self.logger.info("Home Page Title Verification Passed")
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            screenshot_path = "./Screenshots/test_homepage_title.png"
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot captured: {screenshot_path}")
            assert False

        self.logger.info("========== TestHomePage: Home Page Title Verification Completed ==========")
