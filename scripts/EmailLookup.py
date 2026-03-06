# Imports
from email_validator import validate_email, EmailNotValidError
import requests
import hashlib

class EmailLookup:
    def __init__(self, email) -> None:
        self.email = email
        self.lookup()
    
    def lookup(self):
        try:
            validate_email(self.email, check_deliverability=True)
            haveIBeenPwned = input("You entered a valid email, would you like to check if your email has been pwned? [y/n]: ")
            if haveIBeenPwned.lower() == "y":
                self.haveIBeenPwned()
        except EmailNotValidError as e:
            print(f"Invalid email address: {e}")
        except Exception as e:
            print(f"Error: {e}. An unexpected error occurred during email lookup. \n")
    
    def haveIBeenPwned(self):
        try:
            # Hash email
            hashed_email = hashlib.sha1(self.email.encode('utf-8')).hexdigest().upper()
            response = requests.get(f"https://api.pwnedpasswords.com/range/{hashed_email[:5]}").text

            if hashed_email[5:] in response:
                print(f"Your email has been pwned!")
                print(f"It has been pwned {response.split(hashed_email[5:])[1].split(':')[1].strip()[0]} times! \n")
            else:
                print("Your email has not been pwned! \n")

        except Exception as e:
            print(f"Error: {e}. Unable to make a request to Have I Been Pwned. \n")


