import configparser

# Create a configuration parser object
config = configparser.ConfigParser()

# Read the configuration file
config.read(".\Configuration\config.ini")


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