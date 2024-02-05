import re


def is_valid_msisdn(phone_number: str) -> bool:
    """
    Checks if the given phone number is a valid MSISDN.

    Args:
        phone_number (str): The phone number to check.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    pattern = re.compile(r"^[1-9]\d{9,14}$")
    return bool(pattern.match(phone_number)) if phone_number else False


def get_cellphone_operator(phone_number: str) -> str:
    """
    Returns the operator of the given phone number.

    Args:
        phone_number (str): The phone number to check.

    Returns:
        str: The operator of the phone number.
    """
    if phone_number.startswith('0'):
        return 'Orange'
    elif phone_number.startswith('7'):
        return 'SFR'
    elif phone_number.startswith('6'):
        return 'Free Mobile'
    else:
        return 'Unknown'


def get_cellphone_region(phone_number: str) -> str:
    """
    Returns the region of the given phone number.

    Args:
        phone_number (str): The phone number to check.

    Returns:
        str: The region of the phone number.
    """
    if phone_number.startswith('0'):
        return 'Paris'
    elif phone_number.startswith('7'):
        return 'Lyon'
    elif phone_number.startswith('6'):
        return 'Marseille'
    else:
        return 'Unknown'
