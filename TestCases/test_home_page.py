import pytest

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


    @pytest.mark.skip(reason="Skipping this test temporarily")
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


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_latest_opinion_count(self, setup):
        """
        Test case to verify the count of latest opinions.
        """
        self.logger.info("========== TestHomePage: Latest Opinion Count Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
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
        # Get the count of latest opinions
        latest_opinion_count = homepage.get_latest_opinion_count()
        self.logger.info(f"Latest Opinion Count: {latest_opinion_count}")
        # Validate the count
        assert latest_opinion_count == 6, "Latest Opinion Count Verification Failed"
        self.logger.info("Latest Opinion Count Verification Passed")
        self.logger.info("========== TestHomePage: Latest Opinion Count Verification Completed ==========")
        self.driver.quit()
        # Ensure browser closure after test execution
        self.logger.info("Browser closed after test execution.")
        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_home_page_logo(self, setup):
        """
        Test case to verify the home page logo.
        """
        self.logger.info("========== TestHomePage: Home Page Logo Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")
        # Wait for the page to load completely
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        # Initialize HomePage object
        homepage = HomePage(self.driver)

        homepage.is_logo_visible()
        self.logger.info("Home Page Logo Verification Passed")
        self.logger.info("========== TestHomePage: Home Page Logo Verification Completed ==========")
        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_home_page_menu_items(self, setup):
        """
        Test case to verify the home page menu items.
        """
        self.logger.info("========== TestHomePage: Home Page Menu Items Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")
        # Wait for the page to load completely
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        # Initialize HomePage object
        homepage = HomePage(self.driver)

        # Get the count of menu items
        menu_items_count = homepage.get_navbar_menu_items()
        self.logger.info(f"Menu Items Count: {menu_items_count}")
        # Validate the count
        assert menu_items_count == 6, "Home Page Menu Items Count Verification Failed"
        self.logger.info("Home Page Menu Items Count Verification Passed")
        self.logger.info("========== TestHomePage: Home Page Menu Items Verification Completed ==========")


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_home_page_para_text(self, setup):
        """
        Test case to verify the PARA text on the home page.
        """
        self.logger.info("========== TestHomePage: Home Page PARA Text Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Initialize HomePage object
        homepage = HomePage(self.driver)

        # Get the PARA text
        para_text = homepage.get_home_page_para_text()
        self.logger.info(f"PARA Text: {para_text}")

        # Validate the PARA text
        assert para_text.upper() == "PARA", "Home Page PARA Text Verification Failed"

        self.logger.info("Home Page Para Text Verification Passed")
        self.logger.info("========== TestHomePage: Home Page PARA Text Verification Completed ==========")

        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_instagram_icon(self, setup):
        """
        Test case to verify the Instagram icon on the home page.
        """
        self.logger.info("========== TestHomePage: Instagram Icon Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Initialize HomePage object
        homepage = HomePage(self.driver)

        # Get the Instagram icon element
        instagram_icon = homepage.get_instagram_icon()

        # Validate the Instagram icon visibility and enabled state
        assert instagram_icon.is_displayed() and instagram_icon.is_enabled(), "Instagram Icon Verification Failed"

        self.logger.info("Instagram Icon Verification Passed")
        self.logger.info("========== TestHomePage: Instagram Icon Verification Completed ==========")

        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_linkedin_icon(self, setup):
        """
        Test case to verify the LinkedIn icon on the home page.
        """
        self.logger.info("========== TestHomePage: LinkedIn Icon Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Initialize HomePage object
        homepage = HomePage(self.driver)

        # Get the LinkedIn icon element
        linkedin_icon = homepage.get_linkedin_icon()

        # Validate the LinkedIn icon visibility and enabled state
        assert linkedin_icon.is_displayed() and linkedin_icon.is_enabled(), "LinkedIn Icon Verification Failed"

        self.logger.info("LinkedIn Icon Verification Passed")
        self.logger.info("========== TestHomePage: LinkedIn Icon Verification Completed ==========")

        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_whatapp_icon(self, setup):
        """
        Test case to verify the WhatsApp icon on the home page.
        """
        self.logger.info("========== TestHomePage: WhatsApp Icon Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Initialize HomePage object
        homepage = HomePage(self.driver)

        # Get the WhatsApp icon element
        whatsapp_icon = homepage.get_whatsapp_icon()

        # Validate the WhatsApp icon visibility and enabled state
        assert whatsapp_icon.is_displayed() and whatsapp_icon.is_enabled(), "WhatsApp Icon Verification Failed"

        self.logger.info("WhatsApp Icon Verification Passed")
        self.logger.info("========== TestHomePage: WhatsApp Icon Verification Completed ==========")

        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_footer_links(self, setup):
        """
        Test case to verify the footer links on the home page.
        """
        self.logger.info("========== TestHomePage: Footer Links Verification Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        homepage = HomePage(self.driver)

        # Wait until footer links are present (optional but helpful)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, homepage.footer_all_links_xpath))
        )

        # Get the footer links (count and texts)
        count, texts = homepage.get_footer_all_links()

        self.logger.info(f"Found {count} footer links")
        self.logger.info(f"Footer Links Texts: {texts}")

        # Assertion
        expected_count = 7
        assert count == expected_count, f"Expected {expected_count} footer links, but found {count}"

        self.logger.info("Footer Links Verification Passed")
        self.logger.info("========== TestHomePage: Footer Links Verification Completed ==========")

        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    @pytest.mark.responsive
    def test_responsive_small_screen(self, setup):
        """
        Test case to verify the responsiveness of the home page on small screens.
        """
        self.logger.info("========== TestHomePage: Responsive Test for Small Screen Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Resize browser to small screen dimensions (e.g., 375x667 for mobile)
        self.driver.set_window_size(375, 667)
        self.logger.info("Browser resized to 375x667 (small screen).")

        homepage = HomePage(self.driver)

        # Verify visibility of key elements
        assert homepage.is_logo_visible(), "Logo is not visible on small screen."
        self.logger.info("Logo is visible on small screen.")

        navbar_items_count = homepage.get_navbar_menu_items()
        assert navbar_items_count > 0, "Navbar items are not visible on small screen."
        self.logger.info(f"Navbar items are visible on small screen: {navbar_items_count} items.")

        self.logger.info("========== TestHomePage: Responsive Test for Small Screen Completed ==========")
        self.driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    @pytest.mark.responsive
    def test_responsive_medium_screen(self, setup):
        """
        Test case to verify the responsiveness of the home page on medium screens.
        """
        self.logger.info("========== TestHomePage: Responsive Test for Medium Screen Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Resize browser to medium screen dimensions (e.g., 768x1024 for tablets)
        self.driver.set_window_size(768, 1024)
        self.logger.info("Browser resized to 768x1024 (medium screen).")

        homepage = HomePage(self.driver)

        # Verify visibility of key elements
        assert homepage.is_logo_visible(), "Logo is not visible on medium screen."
        self.logger.info("Logo is visible on medium screen.")

        navbar_items_count = homepage.get_navbar_menu_items()
        assert navbar_items_count > 0, "Navbar items are not visible on medium screen."
        self.logger.info(f"Navbar items are visible on medium screen: {navbar_items_count} items.")

        self.logger.info("========== TestHomePage: Responsive Test for Medium Screen Completed ==========")
        self.driver.quit()


    @pytest.mark.responsive
    def test_responsive_large_screen(self, setup):
        """
        Test case to verify the responsiveness of the home page on large screens.
        """
        self.logger.info("========== TestHomePage: Responsive Test for Large Screen Started ==========")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info(f"Navigated to {self.baseURL}")

        # Resize browser to large screen dimensions (e.g., 1920x1080 for desktops)
        self.driver.set_window_size(1920, 1080)
        self.logger.info("Browser resized to 1920x1080 (large screen).")

        homepage = HomePage(self.driver)

        # Verify visibility of key elements
        assert homepage.is_logo_visible(), "Logo is not visible on large screen."
        self.logger.info("Logo is visible on large screen.")

        navbar_items_count = homepage.get_navbar_menu_items()
        assert navbar_items_count > 0, "Navbar items are not visible on large screen."
        self.logger.info(f"Navbar items are visible on large screen: {navbar_items_count} items.")

        self.logger.info("========== TestHomePage: Responsive Test for Large Screen Completed ==========")
        self.driver.quit()
