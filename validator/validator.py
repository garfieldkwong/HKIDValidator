"""validator for Hong Kong ID card number"""
import re
from . import error, misc
FORMAT_REGEX = re.compile('(([A-Z]{1,2})([0-9]{6}))\(([0-9]|A)\)')


def validate(id_number):
    """Verify function
    >>> validate('C123456(9)')
    True
    >>> validate('AY987654(A)')
    False
    """
    matched = FORMAT_REGEX.search(id_number)
    if matched is None:
        raise error.FormatError()
    matched_groups = matched.groups()
    character = matched_groups[1]
    digit = matched_groups[2]
    check_digit = matched_groups[3]
    reversed_number_list = []
    for item in reversed(list(character + digit)):
        reversed_number_list.append(misc.char2digit(item))
    accumulate = misc.accumulate(reversed_number_list)
    accumulate += int(check_digit, base=16)
    remainder = divmod(accumulate, 11)[1]
    return (remainder == 0)

