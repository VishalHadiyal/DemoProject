import os
import time
import json

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from pageObject.parasearch import ParaSearch
from pageObject.homepage import HomePage
from pageObject.loginPage import LoginPage
from pageObject.profilepage import ProfilePage
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class TestParaSearchPage:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_para_search_functionality(self, setup):
        self.logger.info("========== [TEST STARTED] test_para_search_functionality ==========")

        # Set up driver and open base URL
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 60)

        # Initialize page objects
        homepage = HomePage(self.driver)
        loginpage = LoginPage(self.driver)
        parasearch = ParaSearch(self.driver)
        profilepage = ProfilePage(self.driver)

        # Perform login steps
        homepage.click_login_button()
        loginpage.set_username(ReadConfig.get_user_email())
        loginpage.set_password(ReadConfig.get_user_password())
        loginpage.click_login()

        # Wait for successful login confirmation
        try:
            wait.until(lambda d: parasearch.get_success_alert_text() == "Login Successful !")
        except TimeoutException:
            self.logger.error("[LOGIN FAILED] Could not detect success message after login.")
            self.driver.save_screenshot("./Screenshots/login_failed_alert_not_found.png")
            assert False

        # Get list of questions from config
        para_questions = ReadConfig.get_para_search_text_list()
        responses = []  # To store question-response pairs

        # Iterate over each question and perform the test
        for idx, question in enumerate(para_questions, start=1):
            self.logger.info(f"[START] Processing Question {idx}: {question}")

            try:
                # Attempt to open sidebar if present
                try:
                    parasearch.clicks_side_bar_button()
                    time.sleep(1)
                except TimeoutException:
                    self.logger.warning("[WARNING] Sidebar not available. Continuing without clicking.")

                # Create new chat
                try:
                    parasearch.clicks_add_new_chat_button()
                    expected_text = ReadConfig.get_new_chat_create_text()
                    wait.until(lambda d: parasearch.get_text_on_success_popup_message() == expected_text)
                    self.logger.info(f"[INFO] New chat created for Question {idx}.")
                except Exception as e:
                    self.logger.error(f"[ERROR] Failed to create new chat for Question {idx}: {e}")
                    self.driver.save_screenshot(f"./Screenshots/question_{idx}_chat_creation_failed.png")
                    assert False

                # Enter question in search bar
                try:
                    search_bar = parasearch.wait_for_search_bar_ready(self.driver, parasearch)
                    search_bar.clear()
                    search_bar.send_keys(question)
                except Exception as e:
                    self.logger.error(f"[ERROR] Search bar interaction failed for Question {idx}: {e}")
                    self.driver.save_screenshot(f"./Screenshots/question_{idx}_search_bar_issue.png")
                    assert False

                # Click search button
                parasearch.clicks_search_button()

                # Wait for and capture the response
                try:
                    time.sleep(2)
                    wait.until(lambda d: parasearch.get_response_text() != "")
                    response = parasearch.get_response_text()
                    self.logger.info(f"[SUCCESS] Response received for Question {idx}.")
                    responses.append({
                        "question": question,
                        "response": response
                    })
                except TimeoutException:
                    self.logger.error(f"[ERROR] No response received for Question {idx}.")
                    self.driver.save_screenshot(f"./Screenshots/question_{idx}_no_response_received.png")
                    assert False

            except Exception as e:
                self.logger.error(f"[FATAL ERROR] Unexpected error for Question {idx}: {e}")
                self.driver.save_screenshot(f"./Screenshots/question_{idx}_unexpected_error.png")
                assert False

        # Save all question-response data to a JSON file
        responses_file = "./Responses/para_search_responses.json"
        os.makedirs(os.path.dirname(responses_file), exist_ok=True)
        with open(responses_file, "w", encoding="utf-8") as f:
            json.dump(responses, f, indent=4, ensure_ascii=False)
        self.logger.info("[INFO] All responses saved to para_search_responses.json.")

        # Perform logout operation
        try:
            parasearch.clicks_user_profile_logo()
            profilepage.click_profile_icon_on_profile_page()
            profilepage.click_logout_button_on_profile_page()
            assert self.driver.title == "Para"
            self.logger.info("[INFO] Logout successful.")
        except Exception as e:
            self.logger.error(f"[ERROR] Logout failed: {e}")
            self.driver.save_screenshot("./Screenshots/logout_failed.png")
            assert False

        # Close browser session
        self.driver.quit()
        self.logger.info("========== [TEST PASSED] test_para_search_functionality ==========")
