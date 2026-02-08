import re


def normalize_phone(num):
    """
    Normalizes a phone number to a standard format (only digits and leading '+').

    Parameters:
        num (str): Phone number in any format.

    Returns:
        str: Normalized number with only digits and '+' prefix.
            Adds '+38' if the number has no country code, or '+' if it starts with 380.
    """
    digits = re.sub(r'\D', '', num)

    if digits.startswith('380'):
        return '+' + digits
    else:
        return '+38' + digits



if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)