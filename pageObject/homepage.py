from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:
    """
    Page Object Model (POM) class for the Home Page.
    """

    # Locators
    button_login_xpath = "//button[text()='Log In']"
    text_Latest_Opinion_CSS_SELECTOR = ".MuiTypography-root.MuiTypography-body1.css-66ma6b"
    count_of_latest_opinion_xpath = "//div[@class='MuiBox-root css-hmirpn']/div[@class='react-reveal']"
    home_page_logo_xpath = "//img[@class='MuiBox-root css-14r5sd0']"
    navbar_menu_items_xpath = "(//div[@class='MuiBox-root css-19iahwm']/div)[position() <= 6]"
    home_page_para_text_xpath = "//span[@class='MuiBox-root css-1a8bsi9']"
    instagram_icon_xpath = "(//*[@class='MuiBox-root css-ytumd6'])[1]"
    linkedin_icon_xpath  = "(//*[@class='MuiBox-root css-ytumd6'])[2]"
    whatsapp_icon_xpath  = "(//*[@class='MuiBox-root css-ytumd6'])[3]"
    footer_all_links_xpath = "/html/body/div[1]/div[2]/div[5]/div[1]/div[1]/div[3]//a"

    home_page_header_option_pricing_xpath = "//div[text()='Pricing']"

    but_explore_AI_CSS_SELECTOR = ".MuiBox-root.css-1o98lg5"

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def click_login_button(self):
        """
        Clicks the login button.
        """
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        """
        Waits for the specified element to be visible.
        :param locator: Locator tuple (By, value)
        :param timeout: Maximum time to wait for the element to be visible
        :return: WebElement if found, else raises TimeoutException
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def scroll_until_element_visible(self, timeout=10):
        """
        Scrolls the page until the 'Latest Opinion' section is displayed or timeout is reached.
        :param timeout: Maximum time to wait for the element to be visible
        :return: WebElement if found and visible, else raises Exception
        """
        locator = (By.CSS_SELECTOR, self.text_Latest_Opinion_CSS_SELECTOR)
        end_time = time.time() + timeout

        while time.time() < end_time:
            try:
                element = self.driver.find_element(*locator)
                if element.is_displayed():
                    return element
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)  # Small delay to allow rendering
            except:
                pass  # Ignore exceptions and continue scrolling

        raise Exception(f"Element {self.text_Latest_Opinion_CSS_SELECTOR} not found or not visible after scrolling.")

    def get_latest_opinion_count(self):
        """
        Returns the count of latest opinions.
        :return: Count of latest opinions as an integer
        """
        count_element = self.driver.find_elements(By.XPATH, self.count_of_latest_opinion_xpath)
        return len(count_element)

    def is_logo_visible(self):
        """
        Checks if the home page logo is visible.
        :return:
        """
        return self.driver.find_element(By.XPATH, self.home_page_logo_xpath).is_displayed()

    def get_navbar_menu_items(self):
        """
        Returns the text of the first six menu items in the navbar.
        :return: List of menu item texts
        """
        menu_items = self.driver.find_elements(By.XPATH, self.navbar_menu_items_xpath)
        return len(menu_items)

    def get_home_page_para_text(self):
        """
        Returns the text of the paragraph on the home page.
        :return: Text of the paragraph
        """
        para_text = self.driver.find_element(By.XPATH, self.home_page_para_text_xpath)
        return para_text.text

    def get_instagram_icon(self):
        """
        Returns the Instagram icon WebElement.
        """
        return self.driver.find_element(By.XPATH, self.instagram_icon_xpath)

    def get_linkedin_icon(self):
        """
        Returns whether the LinkedIn icon is visible and enabled.
        """
        return self.driver.find_element(By.XPATH, self.linkedin_icon_xpath)

    def get_whatsapp_icon(self):
        """
        Returns whether the WhatsApp icon is visible and enabled.
        """
        return self.driver.find_element(By.XPATH, self.whatsapp_icon_xpath)

    def get_footer_all_links(self):
        """
        Returns a tuple: (count of footer links, list of footer link texts)
        """
        all_links = self.driver.find_elements(By.XPATH, self.footer_all_links_xpath)
        link_texts = [link.text.strip() for link in all_links]
        return len(all_links), link_texts

    def navigate_to_pricing_page(self):
        """
        Returns the header option text from the home page.
        :return: Text of the header option
        """
        return self.driver.find_element(By.XPATH, self.home_page_header_option_pricing_xpath).click()

    def click_explore_AI_button(self):
        """
        Clicks the 'Explore AI' button.
        """
        self.driver.find_element(By.CSS_SELECTOR, self.but_explore_AI_CSS_SELECTOR).click()