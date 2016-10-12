"""calculate check digit"""
from . import misc


def cal_check_digit(id_number):
    """Check digit
    >>> cal_check_digit('G123456')
    'A'
    >>> cal_check_digit('L555555')
    '0'
    >>> cal_check_digit('AB987654')
    '2'
    """
    reversed_number_list = []
    for item in reversed(list(id_number)):
        reversed_number_list.append(misc.char2digit(item))
    accumulate = misc.accumulate(reversed_number_list)
    remainder = divmod(accumulate, 11)[1]
    check_digit = divmod(11 - remainder, 11)[1]
    return hex(check_digit)[2].upper()

