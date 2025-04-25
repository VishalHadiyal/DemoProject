from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PricingPage:

    # Locators
    txtPageContent = "//p[@class='MuiTypography-root MuiTypography-body1 css-ppua96']"
    txtFreeTrial_CSS_Selector = ".MuiTypography-root.MuiTypography-body1.css-1osmri2"

    btnGeneralPlan = "//div[text()='General Plan']"

    btnStudentPlan = "//p[text()='Student Plan']"

    btnTopUpPlan = "//p[text()='Top Up Plan']"

    btnGiftVoucher = "//p[text()='Gift Voucher']"

    text_of_the_all_plan_CSS_Selector = ".MuiTypography-root.MuiTypography-body1.css-1tayq9h"

    txtNoteXpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-1ht5877']"
    lnkTermsAndConditions = "//a[text()='Terms & Conditions']"

    txtSection29XPATH = "//h2[@id='specific-section']"

    # ======================================= XPATH for plans and pricing =======================================
    # Like monthly, yearly, etc.
    txtPlanNameXpath  = "//div[@class = 'MuiBox-root css-1mnl8w7']"

    # Like 1 month RS. 650
    txtPricingXpath = "//p[@class = 'MuiTypography-root MuiTypography-body1 css-drmost']"

    # Like 1 month 90 : Credits
    txtCreditXpath = "//div[@class = 'MuiBox-root css-wyqhe1'][1]"

    # Like valid fof 1 month
    txtValidityXpath = "//div[@class = 'MuiBox-root css-wyqhe1'][2]"


    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.
        :param driver: WebDriver instance
        """
        self.driver = driver

    def get_page_content(self):
        """
        Get the page content text.
        :return: Page content text
        """
        return self.driver.find_element(By.XPATH, self.txtPageContent).text

    def get_free_trial_text(self):
        """
        Get the free trial text.
        :return: Free trial text
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.txtFreeTrial_CSS_Selector).text

    def click_general_plan(self):
        """
        Click the General Plan button.
        """
        self.driver.find_element(By.XPATH, self.btnGeneralPlan).click()

    def click_student_plan(self):
        """
        Click the Student Plan button.
        """
        self.driver.find_element(By.XPATH, self.btnStudentPlan).click()

    def click_top_up_plan(self):
        """
        Click the Top Up Plan button.
        """
        self.driver.find_element(By.XPATH, self.btnTopUpPlan).click()

    def click_gift_voucher(self):
        """
        Click the Gift Voucher button.
        """
        self.driver.find_element(By.XPATH, self.btnGiftVoucher).click()

    def get_all_the_plan_text_values_common_method(self):
        """
        Get the Student Plan text.
        :return: Student Plan text
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.text_of_the_all_plan_CSS_Selector).text

    def get_note_text(self):
        """
        Get the note text.
        :return: Note text
        """
        return self.driver.find_element(By.XPATH, self.txtNoteXpath).text

    def click_terms_and_conditions(self):
        """
        Click the Terms & Conditions link.
        """
        self.driver.find_element(By.XPATH, self.lnkTermsAndConditions).click()

    def get_section_29_text(self):
        try:
            # Define the XPath locator for the section. Replace 'self.txtSection29XPATH' with your actual XPath.
            section_locator = (By.XPATH, self.txtSection29XPATH)

            # Wait for the section to become visible on the page (up to 10 seconds).
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(section_locator)
            )

            # Find the element on the page using the defined locator.
            element = self.driver.find_element(*section_locator)

            # Scroll the element into view to ensure it is visible, in case it is not currently in the viewport.
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Return the stripped text of the section (remove any leading or trailing whitespace).
            return element.text.strip()

        except Exception as e:
            # If there is any error (e.g., element not found or issue with the scroll), print the error message.
            print("Error locating Section 29:", e)

            # Return an empty string in case of an error.
            return ""

# ======================================= XPATH for plans and pricing =======================================

    # def get_plan_name(self):
    #     """
    #     Get the plan names.
    #     :return: List of plan names
    #     """
    #     return [elem.text for elem in self.driver.find_elements(By.XPATH, self.txtPlanNameXpath)]
    #
    # def get_pricing(self):
    #     """
    #     Get the pricing information.
    #     :return: List of pricing information
    #     """
    #     return [elem.text for elem in self.driver.find_elements(By.XPATH, self.txtPricingXpath)]
    #
    # def get_credit(self):
    #     """
    #     Get the credit information.
    #     :return: List of credit information
    #     """
    #     return [elem.text for elem in self.driver.find_elements(By.XPATH, self.txtCreditXpath)]
    #
    # def get_validity(self):
    #     """
    #     Get the validity information.
    #     :return: List of validity information
    #     """
    #     return [elem.text for elem in self.driver.find_elements(By.XPATH, self.txtValidityXpath)]
