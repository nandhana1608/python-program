import re

# Email validation
email = input("Enter email address: ")

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")

# Phone number validation
phone = input("Enter phone number: ")

if re.fullmatch(r"(?:\+91[- ]?)?[6-9][0-9]{9}", phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

# Transaction ID extraction
log = input("Enter transaction log: ")

ids = re.findall(r"TXN[0-9]+", log)

print("Transaction IDs:", ids)