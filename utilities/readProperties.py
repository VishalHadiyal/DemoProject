import configparser

# Create a configuration parser object
config = configparser.ConfigParser()

# Read the configuration file
config.read("./Configuration/config.ini")


class ReadConfig:
    """
    This class is used to read values from the config.ini file.
    It contains static methods to retrieve application-related configurations.
    """

    @staticmethod
    def get_application_url():
        """
        Retrieves the application base URL from the configuration file.

        Returns:
            str: The base URL of the application.
        """
        return config.get('COMMON', 'baseURL', fallback=None)

    @staticmethod
    def get_user_email():
        """
        Retrieves the username from the configuration file.

        Returns:
            str: The username from the config file.
        """
        return config.get('COMMON', 'username', fallback=None)

    @staticmethod
    def get_user_password():
        """
        Retrieves the user password from the configuration file.

        Returns:
            str: The password from the config file.
        """
        return config.get('COMMON', 'password', fallback=None)

    @staticmethod
    def get_pricing_page_url():
        """
        Retrieves the Pricing Page URL from the configuration file.

        Returns:
            str: The Pricing Page URL.
        """
        return config.get('PRICING', 'pricing_page_url', fallback=None)

    @staticmethod
    def get_free_trial_content_text():
        """
        Retrieves the Free Trial text from the configuration file.

        Returns:
            str: The Free Trial text.
        """
        return config.get('STATIC_DATA', 'content', fallback=None)

    @staticmethod
    def get_general_plan_text():
        """
        Retrieves the PG text from the configuration file.

        Returns:
            str: The PG text.
        """
        return config.get('STATIC_DATA', 'general_plan_text', fallback=None)

    @staticmethod
    def get_student_plan_text():
        """
        Retrieves the Student Plan text from the configuration file.

        Returns:
            str: The Student Plan text.
        """
        return config.get('STATIC_DATA', 'student_plan_text', fallback=None)

    @staticmethod
    def get_top_up_plan_text():
        """
        Retrieves the Top Up Plan text from the configuration file.

        Returns:
            str: The Top Up Plan text.
        """
        return config.get('STATIC_DATA', 'top_up_plan_text', fallback=None)

    @staticmethod
    def get_gift_voucher_text():
        """
        Retrieves the Gift Voucher text from the configuration file.

        Returns:
            str: The Gift Voucher text.
        """
        return config.get('STATIC_DATA', 'gift_voucher_plan_text', fallback=None)

    @staticmethod
    def get_note_expected_text():
        """
        Retrieves the Note text from the configuration file.

        Returns:
            str: The Note text.
        """
        return config.get('STATIC_DATA', 'note_text', fallback=None)

    @staticmethod
    def get_section_29_text_values():
        """
        Retrieves the Section 29 text from the configuration file.

        Returns:
            str: The Section 29 text.
        """
        return config.get('STATIC_DATA', 'section29', fallback=None)

    @staticmethod
    def set_full_name_text():
        """
        Retrieves the Full Name text from the configuration file.

        Returns:
            str: The Full Name text.
        """
        return config.get('SIGNUP_DATA', 'FULL_NAME', fallback=None)


    @staticmethod
    def set_password_text():
        """
        Retrieves the Password text from the configuration file.

        Returns:
            str: The Password text.
        """
        return config.get('SIGNUP_DATA', 'PASSWORD', fallback=None)

    @staticmethod
    def set_city_text():
        """
        Retrieves the City text from the configuration file.

        Returns:
            str: The City text.
        """
        return config.get('SIGNUP_DATA', 'CITY', fallback=None)

    @staticmethod
    def set_confirm_text():

        """
        Retrieves the Confirm text from the configuration file.

        Returns:
            str: The Confirm text.
        """
        return config.get('SIGNUP_DATA', 'REGISTER_CONFIRM_TEXT', fallback=None)

    @staticmethod
    def error_message_full_name():
        """
        Retrieves the error message for Full Name from the configuration file.

        Returns:
            str: The error message for Full Name.
        """
        return config.get('SIGNUP_DATA', 'FULLNAME_ERROR_TEXT', fallback=None)

    @staticmethod
    def error_message_email():
        """
        Retrieves the error message for Email from the configuration file.

        Returns:
            str: The error message for Email.
        """
        return config.get('SIGNUP_DATA', 'EMAIL_ERROR_TEXT', fallback=None)

    @staticmethod
    def error_message_mobile_number():
        """
        Retrieves the error message for Mobile Number from the configuration file.

        Returns:
            str: The error message for Mobile Number.
        """
        return config.get('SIGNUP_DATA', 'MOBILE_ERROR_TEXT', fallback=None)

    @staticmethod
    def error_message_password():
        """
        Retrieves the error message for Password from the configuration file.

        Returns:
            str: The error message for Password.
        """
        return config.get('SIGNUP_DATA', 'PASSWORD_ERROR_TEXT', fallback=None)

    @staticmethod
    def get_student_drop_down_text():
        """
        Retrieves the Student Dropdown text from the configuration file.

        Returns:
            str: The Student Dropdown text.
        """
        return config.get('SIGNUP_DATA', 'STUDENT_SELECT_LABEL', fallback=None)

    @staticmethod
    def get_signup_page_text():
        """
        Retrieves the Signup Page text from the configuration file.

        Returns:
            str: The Signup Page text.
        """
        return config.get('SIGNUP_DATA', 'SIGNUP_PAGE_TEXT', fallback=None)

    @staticmethod
    def get_university_name_text():
        """
        Retrieves the University text from the configuration file.

        Returns:
            str: The University text.
        """
        return config.get('SIGNUP_DATA', 'COLLAGE_NAME', fallback=None)

    @staticmethod
    def enter_para_search_text():
        """
        Retrieves the Para Search text from the configuration file.

        Returns:
            str: The Para Search text.
        """
        return config.get('PARA_SEARCH', 'QUESTION_ONE', fallback=None)

    @staticmethod
    def get_new_chat_create_text():
        """
        Retrieves the New Chat Create text from the configuration file.

        Returns:
            str: The New Chat Create text.
        """
        return config.get('PARA_SEARCH', 'NEW_CHAT_CREATE_TEXT', fallback=None)

