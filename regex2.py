import re

def validate_password(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    return bool(pattern.match(password))

def validate_date(date_str):
    pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$')
    return bool(pattern.match(date_str))

def extract_emails(text):
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}')
    return pattern.findall(text)

def extract_phone_numbers(text):
    pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
    return pattern.findall(text)

def replace_titles(text):
    return re.sub(r'Mr\.', 'Ms.', text)

def main():
    while True:
        print("\n--- Regex Toolkit ---")
        print("1. Validate Password")
        print("2. Validate Date (DD/MM/YYYY)")
        print("3. Extract Emails")
        print("4. Extract Phone Numbers (XXX-XXX-XXXX)")
        print("5. Replace 'Mr.' with 'Ms.'")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            pwd = input("Enter password: ")
            print("Valid password?" , validate_password(pwd))

        elif choice == "2":
            date = input("Enter date (DD/MM/YYYY): ")
            print("Valid date?" , validate_date(date))

        elif choice == "3":
            text = input("Enter text: ")
            print("Emails found:", extract_emails(text))

        elif choice == "4":
            text = input("Enter text: ")
            print("Phone numbers found:", extract_phone_numbers(text))

        elif choice == "5":
            text = input("Enter text: ")
            print("Updated text:", replace_titles(text))

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
