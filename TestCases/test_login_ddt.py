import time
from selenium.common.exceptions import NoSuchElementException

from utilities.readProperties import ReadConfig
from pageObject.loginPage import LoginPage
from pageObject.parasearch import ParaSearch
from pageObject.homepage import HomePage
from pageObject.profilepage import ProfilePage
from utilities.customlogger import LogGen
from utilities.ExcelUtils import ExcelUtils


class Test002_DDT_Login:
    # Reading the base URL from the configuration file
    baseURL = ReadConfig.get_application_url()

    # Path to the Excel file containing test data
    path = "./TestData/datadriven.xlsx"

    # Logger instance for logging test execution details
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        """
        Data-Driven Test for Login functionality.
        Iterates through multiple login credentials stored in an Excel file,
        attempts login, records results in the Excel sheet, and proceeds to the next record.
        """
        self.logger.info("**************************Test_002_login_ddt test**********************")

        # Initialize the WebDriver
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Create object instances for interacting with various pages
        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ps = ParaSearch(self.driver)
        self.pp = ProfilePage(self.driver)

        # Get the total number of rows in the Excel sheet
        self.rows = ExcelUtils.get_row_count(self.path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        for r in range(2, self.rows + 1):
            try:
                # Attempt to click the login button on the homepage
                try:
                    self.hp.click_login_button()
                except NoSuchElementException:
                    self.logger.error("Login button not found on homepage, skipping this test case.")
                    ExcelUtils.write_data(self.path, 'Sheet1', r, 4, "Fail")
                    continue

                # Read login credentials and expected result from Excel
                self.user = ExcelUtils.read_data(self.path, 'Sheet1', r, 1)
                self.password = ExcelUtils.read_data(self.path, 'Sheet1', r, 2)
                self.exp = ExcelUtils.read_data(self.path, 'Sheet1', r, 3)

                # Perform login
                self.lp.set_username(self.user)
                self.lp.set_password(self.password)
                self.lp.click_login()

                # Wait for login process to complete
                time.sleep(5)

                # Capture the actual page title after login attempt
                act_title = self.driver.title
                exp_title = "Para"  # Expected title upon successful login

                # Validate login attempt based on expected outcome
                if act_title == exp_title:
                    if self.exp == 'Pass':
                        self.logger.info("*** Test Passed ***")
                        ExcelUtils.write_data(self.path, 'Sheet1', r, 4, "Pass")
                    else:
                        self.logger.info("*** Test Failed ***")
                        ExcelUtils.write_data(self.path, 'Sheet1', r, 4, "Fail")
                else:
                    if self.exp == "Pass":
                        self.logger.info("*** Test Failed ***")
                        ExcelUtils.write_data(self.path, 'Sheet1', r, 4, "Fail")
                    else:
                        self.logger.info("*** Test Passed ***")
                        ExcelUtils.write_data(self.path, 'Sheet1', r, 4, "Pass")
            except Exception as e:
                # Log any exceptions and mark the test as failed
                self.logger.error(f"Exception occurred during test execution: {str(e)}")
                ExcelUtils.write_data(self.path, 'Sheet1', r, 4, "Fail")

            finally:
                try:
                    # Attempt to log out before the next test iteration
                    self.ps.clicks_user_profile_logo()
                    self.pp.click_profile_icon_on_profile_page()
                    self.pp.click_logout_button_on_profile_page()
                except NoSuchElementException:
                    self.logger.warning("Logout elements not found, possibly due to an invalid login attempt.")

        # End of test execution logging
        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed TC_LoginDDT_002 *************")

        # Close the browser session
        self.driver.close()
        assert True

