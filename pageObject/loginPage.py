from selenium.webdriver.common.by import By

class LoginPage:
    """
    Page Object Model (POM) class for the Login Page.
    This class contains locators and methods to interact with the login page elements.
    """

    # Locators
    textbox_username_xpath = "//input[@name = 'email']"
    textbox_password_xpath = "//input[@name = 'password']"
    button_login_xpath = "//button[@type='submit']"
    button_SignUP_CSSSelector = ".MuiTypography-root.MuiTypography-body1.css-1p90lx9"

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def set_username(self, username):
        """
        Enter the username in the username text box.
        :param username: User's email/username
        """
        username_element = self.driver.find_element(By.XPATH, self.textbox_username_xpath)
        username_element.clear()
        username_element.send_keys(username)

    def set_password(self, password):
        """
        Enter the password in the password text box.
        :param password: User's password
        """
        password_element = self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        password_element.clear()
        password_element.send_keys(password)

    def click_login(self):
        """
        Click the login button.
        """
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_signup(self):
        """
        Click the Sign Up button.
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, self.button_SignUP_CSSSelector).click()
