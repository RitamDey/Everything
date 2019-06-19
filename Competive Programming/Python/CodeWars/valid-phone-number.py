import re


def validPhoneNumber(phoneNumber):
    ph = r'\([0-9]{3}\)\s[0-9]{3}-[0-9]{3}'

    if len(phoneNumber) == 14 and re.match(ph, phoneNumber):
        return True

    return False
