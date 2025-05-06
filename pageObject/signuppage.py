import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig


class SignUPPage:
    # Locators
    designableCSSSelector = ".MuiTypography-root.MuiTypography-body1.css-1q4jom8"
    btnProfessionalTextCssSelector = ".css-pvl5tv"
    txtFullNameXpath = "//input[@name = 'fullName']"
    txtEmailXpath = "//input[@name = 'email']"
    txtMobileNumberXpath = "//input[@name = 'mobile']"
    txtCityXpath = "//input[@name = 'city']"
    txtPasswordXpath = "//input[@name = 'password']"
    btnJoinNowXpath = "//button[@type = 'submit']"
    btnPasswordShowXpath = "//button[@type='button']"
    btnStudentTextCSSSelector = ".css-1jbw1ol"
    uploadIDProofCSSSelector = ".MuiBox-root.css-1xo6uy9"
    dropCollageXpath = "//div[@id='mui-component-select-ipaddress']"
    txtuplodedfileCssSelector = ".MuiTypography-root.MuiTypography-body2.css-68o8xu"

    dropoptionselectCollage = "//li[normalize-space()='GUJARAT UNIVERSITY']"
    txtpasswordID = "//input[@id='standard-basic' and @type='password']"

    errorMessageFillNameXpath = "//p[normalize-space()='String must contain at least 3 character(s)']"
    errorMessageEmailXpath = "//p[normalize-space()='Invalid email']"
    errorMessageMobileXpath = "//p[normalize-space()='String must contain at most 10 character(s)']"
    errorMessagePasswordXpath = "//p[normalize-space()='String must contain at least 8 character(s)']"

    labelText_selectCollage_Xpath = "//p[normalize-space()='Select Collage']"

    def __init__(self, driver):
        """
        Initializes the SignUPPage with a WebDriver instance.

        Args:
            driver (WebDriver): The Selenium WebDriver object.
        """
        self.driver = driver

    def get_Text_of_the_page(self):
        """
        Retrieves the visible text from a specified element on the page.

        Returns:
            str: The text content of the targeted element.
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.designableCSSSelector).text

    def click_Professional_Plan(self):
        """
        Attempts to interact with the Professional Plan button.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.btnProfessionalTextCssSelector)
        element.click()

    def click_Student_Plan(self):
        """
        Clicks on the Student Plan button.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, self.btnStudentTextCSSSelector)
        element.click()

    def set_Full_Name(self, full_name):
        """
        Enters the full name into the Full Name input field.

        Args:
            full_name (str): The user's full name.
        """
        self.driver.find_element(By.XPATH, self.txtFullNameXpath).send_keys(full_name)

    def set_Email(self, email):
        """
        Enters the email address into the Email input field.

        Args:
            email (str): The user's email address.
        """
        self.driver.find_element(By.XPATH, self.txtEmailXpath).send_keys(email)

    def set_Mobile_Number(self, mobile_number):
        """
        Enters the mobile number into the Mobile Number input field.

        Args:
            mobile_number (str): The user's mobile phone number.
        """
        self.driver.find_element(By.XPATH, self.txtMobileNumberXpath).send_keys(mobile_number)

    def set_City(self, city):
        """
        Enters the city name into the City input field.

        Args:
            city (str): The city where the user resides.
        """
        self.driver.find_element(By.XPATH, self.txtCityXpath).send_keys(city)

    def set_password(self, password: str):
        """
        Enters the given password into the password input field.

        Args:
            password (str): The password to enter.

        Returns:
            str: The actual value present in the password input field after entry.
        """
        element = self.driver.find_element(By.XPATH, self.txtPasswordXpath)
        element.clear()  # Optional: Clear the field before entering new text
        element.send_keys(password)
        return element.get_attribute("value")

    def click_Join_Now(self):
        """
        Clicks the 'Join Now' button to submit the signup form.
        """
        self.driver.find_element(By.XPATH, self.btnJoinNowXpath).click()

    def click_Password_Show(self):
        """
        Clicks the 'Show Password' button to toggle password visibility.
        """
        self.driver.find_element(By.XPATH, self.btnPasswordShowXpath).click()

    def upload_ID_Proof(self):
        """
        Uploads an ID proof file via hidden input.
        """
        file_upload = self.driver.find_element(By.CSS_SELECTOR, self.uploadIDProofCSSSelector)

        file_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        file_path = "C:/Users/DELL/PycharmProjects/DemoProject/TestData/sample.jpeg"
        file_input.send_keys(file_path)

    def get_Uploaded_File_Name(self):
        """
        Retrieves the name of the uploaded file.

        Returns:
            str: The name of the uploaded file.
        """
        return self.driver.find_element(By.CSS_SELECTOR, self.txtuplodedfileCssSelector).text

    def select_College(self):
        """
        Opens the dropdown to select a college from the list.
        """
        self.driver.find_element(By.XPATH, self.dropCollageXpath).click()

    def select_College_from_dropdown(self):
        """
        Scrolls to and selects a college from the dropdown list of colleges.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.dropoptionselectCollage))
        )
        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()

    def get_Error_Message_Full_Name(self):
        """
        Retrieves the error message for the Full Name field.

        Returns:
            str: The error message text.
        """
        return self.driver.find_element(By.XPATH, self.errorMessageFillNameXpath).text

    def get_Error_Message_Email(self):
        """
        Retrieves the error message for the Email field.

        Returns:
            str: The error message text.
        """
        return self.driver.find_element(By.XPATH, self.errorMessageEmailXpath).text

    def get_Error_Message_Mobile_Number(self):
        """
        Retrieves the error message for the Mobile Number field.

        Returns:
            str: The error message text.
        """
        # Explicit wait to ensure the error message element is visible
        error_message_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.errorMessageMobileXpath))
        )
        return error_message_element.text

    def get_Error_Message_Password(self):
        """
        Retrieves the error message for the Password field.

        Returns:
            str: The error message text.
        """
        return self.driver.find_element(By.XPATH, self.errorMessagePasswordXpath).text

    def get_Label_Text_Select_College(self):
        """
        Retrieves the label text for the Select College field.

        Returns:
            str: The label text.
        """
        return self.driver.find_element(By.XPATH, self.labelText_selectCollage_Xpath).text