def is_armstrong_number(number: int) -> bool:
    """
    Determine whether a given integer is an Armstrong number.

    An Armstrong number (also known as a narcissistic number) is a number that is equal
    to the sum of its own digits, each raised to the power of the number of digits.
    """
    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == number
