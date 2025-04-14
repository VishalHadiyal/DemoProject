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
