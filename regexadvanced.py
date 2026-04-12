"""
Advanced regex validation functions for passwords, dates, emails, and phone numbers.
"""
import re

def validate_password(password):
    """
    Validate a password with minimum length of 8 characters,
    uppercase letters and lowercase.
    """
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    return bool(pattern.match(password))

# Example text
print(validate_password("Password123"))  # True
print(validate_password("word234"))      # False



def validate_date(date_str):
    """
    Validate a date string in DD/MM/YYYY format.
    Returns True if the date is valid, False otherwise.
    """
    pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$')
    return bool(pattern.match(date_str))

# Example
print(validate_date("12/04/2026"))  # True
print(validate_date("31/13/2026"))  # False

def extract_emails(text):
    """
    this is a function that extracts email addresses from a given text
    """
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}')
    return pattern.findall(text)

# Example test
EXAMPLE_TEXT = "Kindly share your review at customercare@example.com or marketing@company.org"
print(extract_emails(EXAMPLE_TEXT))  # ['customercare@example.com', 'marketing@company.org']


def extract_phone_numbers(text):
    """
    Extract phone numbers in the format XXX-XXX-XXXX from the given text.
    """
    pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
    return pattern.findall(text)

# Example test
NUMBER = "Kindly call 184-456-7890 or 987-654-3210  for more information"
print(extract_phone_numbers(NUMBER))  # ['184-456-7890', '987-654-3210']

def replace_titles(text):
    """
    Replace all occurrences of 'Ms.' with 'Miss.' in the given text.
    """
    return re.sub(r'Ms\.', 'Miss.', text)

# Example test
TEXT = "Ms. Waithera and Ms. Mwende will both be late for today's meeting"
print(replace_titles(TEXT))  # "Miss. Waithera and Miss. Mwende will both be late for today's meeting"