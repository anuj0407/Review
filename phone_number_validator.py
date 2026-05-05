'''
Task 1: Validate Phone Numbers
a) Write a regex pattern to validate Indian mobile numbers:
9876543210
+91-9876543210
b) Implement:
def is_valid_mobile(number: str) -> bool
c) Write 2 pytest unit tests:
One valid case
One invalid case
d) Extend regex to allow spaces:
+91 98765 43210
 Update tests accordingly
e) Explain one edge case not handled:
Example: leading zeros, landline numbers
'''
import re

def is_valid_mobile(phone_number):
    phone_pattern = r"^(\+91-?)?\s?\d{5}\s?\d{5}$"

    if re.match(phone_pattern,phone_number):
        return True
    elif re.match(r"^\+314\d{7}",phone_number):
        raise ValueError("Landline Number")
    elif re.match(r"^0+",phone_number):
        raise ValueError("Leading Zeros problem")
    else:
        return False