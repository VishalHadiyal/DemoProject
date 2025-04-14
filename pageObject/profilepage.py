from selenium.webdriver.common.by import By


class ProfilePage:
    """
    Page Object Model (POM) class for the Profile Page.
    This class contains locators and methods to interact with the profile page elements.
    """

    # CSS Selector locator for the profile icon on the profile page
    ICON_PROFILE_PAGE_CSS_SELECTOR = "div[class='MuiBox-root css-z08w8j'] div[class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-12og7yj']"
    LOGOUT_BUTTON_XPATH = "//body/div[3]/div[3]/div[1]/div[3]/div[1]"

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.

        :param driver: WebDriver instance used to interact with the web browser.
        """
        self.driver = driver  # Assign the provided driver instance to the class for reuse.

    def click_profile_icon_on_profile_page(self):
        """
        Click on the profile icon available on the profile page.

        This method uses the WebDriver instance to locate the profile icon using the defined CSS selector
        and performs a click action on it.
        """
        self.driver.find_element(By.CSS_SELECTOR,
                                 self.ICON_PROFILE_PAGE_CSS_SELECTOR).click()  # Perform the click action on the profile icon.

    def click_logout_button_on_profile_page(self):
        """
        Click on the logout button available on the profile page.

        This method uses the WebDriver instance to locate the logout button using the defined CSS selector
        and performs a click action on it.
        """
        self.driver.find_element(By.XPATH,self.LOGOUT_BUTTON_XPATH).click()