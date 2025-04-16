from selenium.webdriver.common.by import By


class Services:

    services_header_option_visible_text = "//*[text()='Services']"
    services_page_name_css_selector = ".MuiTypography-root.MuiTypography-body1.css-z1nhid"
    services_page_text_quote_xpath = "//*[text()='Transforming legal hurdles into smooth pathways']"

    services_parasors_logo_xpath = "//img[@src = '/static/media/parasorc.dd828ea49bea46d40b67.png']"
    services_content_of_parasors_xpath = "//p[contains(text(),'ParaSors leverages AI to provide e-journal updates')]"

    services_paradraft_logo_xpath = "//img[@src = '/static/media/paradraft.1adba6d882050c331613.png']"
    services_content_of_paradraft_xpath = "//p[contains(text(),'Paradraft focuses on enhancing legal drafting proc')]"

    services_parasearch_logo_xpath = "//img[@src = '/static/media/parasearch.5750e9634f9ca7286254.png']"
    services_content_of_parasearch_css_selector = "div[class='MuiBox-root css-16d3pem'] p[class='MuiTypography-root MuiTypography-body1 css-l159bm']"

    services_paradoc_logo_xpath = "//img[@src = '/static/media/paradoc.4d444550ef95f88f6aca.png']"
    services_content_of_paradoc_xpath = "//p[contains(text(),'Paradoc specializes in the analysis and management')]"

    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver


    def click_services_options_on_header(self):
        """
        Clicks the services header option.
        """
        self.driver.find_element(By.XPATH, self.services_header_option_visible_text).click()

    def get_page_title(self):
        """
        Returns the title of the current page.
        :return: Title of the page as a string
        """
        return self.driver.title

    def get_current_url(self):
        """
        Returns the current URL of the page.
        :return: Current URL as a string
        """
        return self.driver.current_url

    def get_services_page_name(self):
        """
        Returns the name of the services page.
        :return: Name of the services page as a string
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.services_page_name_css_selector).text

    def get_services_page_text_quote(self):
        """
        Returns the text quote from the services page.
        :return: Text quote from the services page as a string
        """
        return self.driver.find_element(By.XPATH, self.services_page_text_quote_xpath).text

    def get_services_parasors_logo(self):
        """
        Returns the Parasors logo element from the services page.
        :return: WebElement representing the Parasors logo
        """
        return self.driver.find_element(By.XPATH, self.services_parasors_logo_xpath).is_displayed()

    def get_services_content_of_parasors(self):
        """
        Returns the content of the Parasors section from the services page.
        :return: Content of the Parasors section as a string
        """
        return self.driver.find_element(By.XPATH, self.services_content_of_parasors_xpath).text

    def get_services_paradraft_logo(self):
        """
        Returns the Paradraft logo element from the services page.
        :return: WebElement representing the Paradraft logo
        """
        return self.driver.find_element(By.XPATH, self.services_paradraft_logo_xpath).is_displayed()

    def get_services_content_of_paradraft(self):
        """
        Returns the content of the Paradraft section from the services page.
        :return: Content of the Paradraft section as a string
        """
        return self.driver.find_element(By.XPATH, self.services_content_of_paradraft_xpath).text

    def get_services_parasearch_logo(self):
        """
        Returns the Parasearch logo element from the services page.
        :return: WebElement representing the Parasearch logo
        """
        return self.driver.find_element(By.XPATH, self.services_parasearch_logo_xpath).is_displayed()

    def get_services_content_of_parasearch(self):
        """
        Returns the content of the Parasearch section from the services page.
        :return: Content of the Parasearch section as a string
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.services_content_of_parasearch_css_selector).text

    def get_services_paradoc_logo(self):
        """
        Returns the Paradoc logo element from the services page.
        :return: WebElement representing the Paradoc logo
        """
        return self.driver.find_element(By.XPATH, self.services_paradoc_logo_xpath).is_displayed()

    def get_services_content_of_paradoc(self):
        """
        Returns the content of the Paradoc section from the services page.
        :return: Content of the Paradoc section as a string
        """
        return self.driver.find_element(By.XPATH, self.services_content_of_paradoc_xpath).text