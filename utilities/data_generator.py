from datetime import datetime
import random
import string


class DataGenerator:

    def generate_unique_email(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"vishaltest_{timestamp}@yopmail.com"

    def generate_mobile_number(self):
        # Starts with 7, 8, or 9, followed by 9 random digits
        first_digit = random.choice(['7', '8', '9'])
        remaining_digits = ''.join(random.choices('0123456789', k=9))
        return first_digit + remaining_digits

    def generate_unique_email_with_edu(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"vishaltest_{timestamp}@yopmail.edu"

    def generate_invalid_email(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"vishaltest_{timestamp}yopmail.com"

    def generate_invalid_mobile_number(self):
        # Choose a type of invalid number to generate
        invalid_type = random.choice(['wrong_start', 'wrong_length', 'non_digit'])

        if invalid_type == 'wrong_start':
            # Starts with 0–6 (invalid in Indian context), followed by 9 digits
            first_digit = random.choice(['0', '1'])
            remaining_digits = ''.join(random.choices('0123456789', k=9))
            return first_digit + remaining_digits

        elif invalid_type == 'wrong_length':
            # Either too short or too long
            length = random.choice([8, 9, 11, 12])
            return ''.join(random.choices('0123456789', k=length))

        elif invalid_type == 'non_digit':
            # Mix of digits and letters/special characters
            digits = ''.join(random.choices('0123456789', k=7))
            junk = ''.join(random.choices(string.ascii_letters + "!@#$%", k=3))
            return ''.join(random.sample(digits + junk, 10))

        # Optional fallback (not strictly needed since all cases are covered)
        return "INVALID000"

    def generate_two_char_string_name(self):
        return ''.join(random.choices(string.ascii_letters, k=2))

    def generate_six_digit_password(self):
        return str(random.randint(100000, 999999))