import pytest
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig
from pageObject.servicespage import Services


class TestServicesPage:
    """
    Test class to verify the Services Page functionality.
    """

    base_url = ReadConfig.get_application_url()
    expected_title = "Para"
    logger = LogGen.loggen()

    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_title_of_the_page(self, setup):
        """
        Verify that the Services page title matches the expected value.
        """
        self.logger.info("========== Test: Verifying Services Page Title ==========")
        driver = setup

        try:
            driver.get(self.base_url)
            driver.maximize_window()
            self.logger.info("Opened application URL and maximized window.")

            # Wait for body to ensure page has loaded
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Navigate to Services page
            services_page = Services(driver)
            services_page.click_services_options_on_header()

            actual_title = services_page.get_page_title()
            assert actual_title == self.expected_title, (
                f"Expected title: '{self.expected_title}', but got: '{actual_title}'"
            )

            self.logger.info("Services page title verified successfully.")

        except AssertionError as ae:
            self.logger.error(f"Assertion failed: {ae}")
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise
        finally:
            driver.quit()
            self.logger.info("Closed browser after test execution.")

    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_url_of_the_page(self, setup):
        """
        Verify that the Services page URL matches the expected value.
        """
        self.logger.info("========== Test: Verifying Services Page URL ==========")
        driver = setup

        try:
            driver.get(self.base_url)
            driver.maximize_window()
            self.logger.info("Opened application URL and maximized window.")

            # Wait for body to ensure page has loaded
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # Navigate to Services page
            services_page = Services(driver)
            services_page.click_services_options_on_header()

            actual_url = services_page.get_current_url()
            expected_url = "https://para.unada.in/services"
            assert actual_url == expected_url

            self.logger.info("Services page URL verified successfully.")

        except AssertionError as ae:
            self.logger.error(f"Assertion failed: {ae}")
            raise
        except Exception as e:
            self.logger.error(f"An unexpected error occurred: {e}")
            raise
        finally:
            driver.quit()
            self.logger.info("Closed browser after test execution.")

    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_services_page_name(self, setup):
        """
        Verify that the Services page name matches the expected value.
        """
        self.logger.info("========== Test: Verifying Services Page Name ==========")
        driver = setup

        driver.get(self.base_url)
        driver.maximize_window()
        self.logger.info("Opened application URL and maximized window.")

        # Wait for body to ensure page has loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Navigate to Services page
        services_page = Services(driver)
        services_page.click_services_options_on_header()

        # Wait for body to ensure page has loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        actual_page_name = services_page.get_services_page_name()
        expected_page_name = "Our Services"
        assert actual_page_name == expected_page_name

        self.logger.info("Services page name verified successfully.")
        driver.quit()
        self.logger.info("Closed browser after test execution.")

    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_services_page_text_quote(self, setup):
        """
        Verify that the Services page text quote matches the expected value.
        """
        self.logger.info("========== Test: Verifying Services Page Text Quote ==========")
        driver = setup

        driver.get(self.base_url)
        driver.maximize_window()
        self.logger.info("Opened application URL and maximized window.")

        # Wait for body to ensure page has loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Navigate to Services page
        services_page = Services(driver)
        services_page.click_services_options_on_header()

        # Wait for body to ensure page has loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        actual_text_quote = services_page.get_services_page_text_quote()
        expected_text_quote = "Transforming legal hurdles into smooth pathways"
        assert actual_text_quote == expected_text_quote

        self.logger.info("Services page text quote verified successfully.")
        driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_services_parasors_logo_and_content(self, setup):
        driver = setup
        logger = self.logger  # Assuming you're using a logger attached to self
        base_url = self.base_url  # Set this via fixture or class attribute

        logger.info("========== Test: Verifying Parasors Logo on Services Page ==========")

        try:
            driver.get(base_url)
            driver.maximize_window()
            logger.info("Opened application URL and maximized window.")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            services_page = Services(driver)
            services_page.click_services_options_on_header()

            # Check logo
            try:
                assert services_page.get_services_parasors_logo, "Parasors logo is not displayed."
            except AssertionError as e:
                logger.error(f"Assertion failed: {e}")

            # Check content
            expected_text = "ParaSors leverages AI to provide e-journal updates and generate original headnotes for Indian court judgments."
            try:
                actual_text = services_page.get_services_content_of_parasors()
                assert expected_text in actual_text, f"Expected content not found. Got: {actual_text}"
            except AssertionError as e:
                logger.error(f"Assertion failed: {e}")

        finally:
            driver.quit()
            logger.info("Closed the browser.")


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_services_paradraft_logo_and_content(self, setup):
        """
        Verify that the Parasors logo and content on the Services page are displayed correctly.
        """
        self.logger.info("========== Test: Verifying Parasors Logo on Services Page ==========")
        driver = setup

        driver.get(self.base_url)
        driver.maximize_window()
        self.logger.info("Opened application URL and maximized window.")

        # Wait for body to ensure page has loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Navigate to Services page
        services_page = Services(driver)
        services_page.click_services_options_on_header()

        # Verify Parasors logo is displayed
        is_logo_displayed = services_page.get_services_paradraft_logo()
        assert is_logo_displayed, "Parasors logo is not displayed."

        # Verify Parasors content
        expected_content = "Paradraft focuses on enhancing legal drafting processes, offering tools and templates tailored for Indian legal practices."
        actual_content = services_page.get_services_content_of_paradraft()
        assert expected_content in actual_content, f"Expected content not found. Got: {actual_content}"

        self.logger.info("Parasors logo and content on Services page verified successfully.")
        driver.quit()


    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_services_parasearch_logo_and_content(self, setup):
        """
        Verify that the Parasearch logo and content on the Services page are displayed correctly.
        """
        self.logger.info("========== Test: Verifying Parasearch Logo on Services Page ==========")
        driver = setup

        driver.get(self.base_url)
        driver.maximize_window()
        self.logger.info("Opened application URL and maximized window.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Navigate to the Services page
        services_page = Services(driver)
        services_page.click_services_options_on_header()

        # Wait for and scroll to Parasearch logo
        logo_locator = (By.XPATH, services_page.services_parasearch_logo_xpath)
        parasearch_logo_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(logo_locator)
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                              parasearch_logo_element)
        self.logger.info("Scrolled to Parasearch logo.")

        is_logo_displayed = services_page.get_services_parasearch_logo()
        assert is_logo_displayed, "Parasearch logo is not displayed."
        self.logger.info("Parasearch logo is displayed correctly.")

        # Wait for and scroll to Parasearch content
        content_locator = (By.CSS_SELECTOR, services_page.services_content_of_parasearch_css_selector)
        parasearch_content_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(content_locator)
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                              parasearch_content_element)
        self.logger.info("Scrolled to Parasearch content.")

        expected_content = (
            "ParaSearch's flagship product is a cutting-edge legal research assistant built upon an advanced Language Learning Model (LLM)."
        )

        # Ensure this method returns the content text
        actual_content = services_page.get_services_content_of_parasearch()
        assert isinstance(actual_content, str), "Expected actual content to be string, got something else."

        assert expected_content in actual_content, f"Expected content not found. Got: {actual_content}"
        self.logger.info("Parasearch content is displayed correctly.")

        self.logger.info("Parasearch logo and content on Services page verified successfully.")
        driver.quit()


    @pytest.mark.skip(reason="Skipping these tests temporarily")
    def test_services_paradoc_logo_and_content(self, setup):
        """
        Verify that the Paradoc logo and content on the Services page are displayed correctly.
        """
        self.logger.info("========== Test: Verifying Paradoc Logo on Services Page ==========")
        driver = setup

        driver.get(self.base_url)
        driver.maximize_window()
        self.logger.info("Opened application URL and maximized window.")

        # Wait for body element to ensure the page has loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Navigate to the Services page
        services_page = Services(driver)
        services_page.click_services_options_on_header()

        # Wait for and scroll to Paradoc logo
        logo_locator = (By.XPATH, services_page.services_paradoc_logo_xpath)
        paradoc_logo_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(logo_locator)
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                              paradoc_logo_element)
        self.logger.info("Scrolled to Paradoc logo.")

        is_logo_displayed = services_page.get_services_paradoc_logo()
        assert is_logo_displayed, "Paradoc logo is not displayed."
        self.logger.info("Paradoc logo is displayed correctly.")

        # Wait for and scroll to Paradoc content
        content_locator = (By.CSS_SELECTOR, services_page.services_content_of_parasearch_css_selector)
        paradoc_content_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(content_locator)
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                              paradoc_content_element)
        self.logger.info("Scrolled to Paradoc content.")

        expected_content = (
            "Paradoc specializes in the analysis and management of legal documents within the ParaSearch ecosystem."
        )

        actual_content = services_page.get_services_content_of_paradoc()
        assert isinstance(actual_content, str), "Expected actual content to be string, got something else."
        assert expected_content in actual_content, f"Expected content not found. Got: {actual_content}"
        self.logger.info("Paradoc content is displayed correctly.")

        self.logger.info("Paradoc logo and content on Services page verified successfully.")
        driver.quit()

    # ======================================= Parameterized Tests (Optimize Way) =========================================

    @pytest.mark.parametrize("logo_name, logo_method_name, logo_xpath_attr", [
        ("Parasors", "get_services_parasors_logo", "services_parasors_logo_xpath"),
        ("Paradraft", "get_services_paradraft_logo", "services_paradraft_logo_xpath"),
        ("Parasearch", "get_services_parasearch_logo", "services_parasearch_logo_xpath"),
        ("Paradoc", "get_services_paradoc_logo", "services_paradoc_logo_xpath"),
    ])
    @pytest.mark.skip(reason="Skipping this test temporarily")
    def test_services_logo_displayed(self, setup, logo_name, logo_method_name, logo_xpath_attr):
        """
        Verify that specific logos on the Services page are displayed with proper wait.
        """
        self.logger.info(f"========== Test: Verifying {logo_name} Logo on Services Page ==========")
        driver = setup
        driver.get(self.base_url)
        driver.maximize_window()
        self.logger.info("Opened application URL and maximized window.")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        services_page = Services(driver)
        services_page.click_services_options_on_header()

        # Get the logo XPath from the Services class (page object)
        logo_xpath = getattr(services_page, logo_xpath_attr)

        # Wait for the logo to be visible
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, logo_xpath))
            )
            is_logo_displayed = getattr(services_page, logo_method_name)()
        except Exception as e:
            self.logger.error(f"{logo_name} logo not found or not visible: {e}")
            is_logo_displayed = False

        assert is_logo_displayed, f"{logo_name} logo is not displayed on the Services page"
        self.logger.info(f"{logo_name} logo on Services page verified successfully.")
        driver.quit()

    # -------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize("device_name, width, height", [
        ("Television", 1920, 1080),
        ("Tablet", 768, 1024),
        ("Mobile", 375, 667),
    ])
    def test_services_responsive_views(self, setup, device_name, width, height):
        """
        Responsive test for Services Page on different device viewports.
        Includes connection failure handling.
        """
        self.logger.info(f"========== Test: {device_name} view ==========")

        driver = None
        try:
            driver = setup
            driver.set_window_size(width, height)
            self.logger.info(f"Set window size: {width}x{height} for {device_name}")

            driver.get(self.base_url)
            self.logger.info("Navigated to base URL.")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            services_page = Services(driver)
            services_page.click_services_options_on_header()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, services_page.services_parasors_logo_xpath))
            )

            assert services_page.get_services_parasors_logo(), f"{device_name} view: Logo not visible."
            self.logger.info(f"{device_name} view: Verified logo presence.")

            actual_quote = services_page.get_services_page_text_quote()
            assert actual_quote == "Transforming legal hurdles into smooth pathways", f"{device_name} view: Incorrect quote."
            self.logger.info(f"{device_name} view: Quote verified.")

        except WebDriverException as we:
            self.logger.error(f" WebDriver Exception in {device_name} view: {we}")
            self.logger.error("Check if your browser and WebDriver versions are compatible.")
            self.logger.error("Make sure no firewall or antivirus is blocking the connection.")
            raise

        except Exception as e:
            self.logger.error(f" Error in {device_name} view: {e}")
            raise

        finally:
            if driver:
                driver.quit()
                self.logger.info(f"{device_name} view: Driver session closed.")
