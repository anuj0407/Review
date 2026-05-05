'''
c) Write 2 pytest unit tests:
One valid case
One invalid case
d) Extend regex to allow spaces:
+91 98765 43210
 Update tests accordingly
e) Explain one edge case not handled:
Example: leading zeros, landline numbers
'''
import pytest
from phone_number_validator import is_valid_mobile

# Valid case
def test_valid_phone():
    assert is_valid_mobile("+91-92871 90393")

# Invalid case
def test_invalid_phone():
    assert is_valid_mobile("839291") == False

# For edge cases
def test_edge_case_landline():
    with pytest.raises(ValueError,match = "Landline Number"):
        is_valid_mobile("+3149898238")
def test_edge_case():
    with pytest.raises(ValueError,match = "Leading Zeros problem"):
        is_valid_mobile("000092822389")

