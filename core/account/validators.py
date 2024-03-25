from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def is_valid_mobile(value):
    mobile_regex = "^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$"
    if(re.search(mobile_regex, value)):
        return value
    raise ValidationError(_("invalid phone number"))


def is_valid_national_code(value: str):
    if len(value) != 10:
        raise ValidationError("invalid iranian national code")

    check = int(value[9])
    sum = 0
    for i in range(9):
        sum += int(value[i]) * (10 - i)

    remainder = sum % 11

    if remainder < 2 and check == remainder:
        return value
    elif remainder >= 2 and check == 11 - remainder:
        return value
    else:
        raise ValidationError("invalid iranian national code")

