import re

from main_api.models import OpenData


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


def get_cellphone_operator_and_region(phone_number: str) -> tuple[str, str]:
    """
    Returns the operator and region of the given phone number.

    Args:
        phone_number (str): The phone number to check.

    Returns:
        tuple[str, str]: A tuple containing the operator and region.
    """
    code = phone_number[1:4]
    number = phone_number[4:]
    result: OpenData = OpenData.objects.filter(
        code=code,
        from_limit__lte=number,
        to_limit__gte=number,
    ).first()
    if not result:
        raise ValueError(f"Phone number: {phone_number} does not exist!")
    operator = result.operator
    region = result.region
    return operator, region
