"""Misc"""
from . import error
REVERSED_WEIGHT = [2, 3, 4, 5, 6, 7, 8, 9]


def char2digit(character):
    """Convert character to digit
    >>> char2digit('A')
    1
    >>> char2digit('Z')
    26
    >>> char2digit('1')
    1
    >>> try:
    ...     char2digit('a')
    ... except Exception as exc:
    ...     print(type(exc))
    <class 'validator.error.ValueError'>
    >>> try:
    ...     char2digit('AA')
    ... except Exception as exc:
    ...     print(type(exc))
    <class 'validator.error.ValueError'>
    >>> try:
    ...     char2digit('')
    ... except Exception as exc:
    ...     print(type(exc))
    <class 'validator.error.ValueError'>
    """
    if len(character) != 1:
        raise error.ValueError()
    if character.isupper():
        return ord(character) - ord('A') + 1
    elif character.isdigit():
        return int(character)
    else:
        raise error.ValueError()


def accumulate(reversed_number_list):
    """Accumulate
    >>> accumulate([6, 5, 4, 3, 2, 1, 7])
    133
    >>> accumulate([5, 5, 5, 5, 5, 5, 12])
    231
    """
    accumulate = 0
    for idx in range(0, len(reversed_number_list)):
        accumulate += reversed_number_list[idx] * REVERSED_WEIGHT[idx]
    return accumulate