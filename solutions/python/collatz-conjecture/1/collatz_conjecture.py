def steps(number):
    """
    Return the number of steps to reach 1 using the Collatz Conjecture.

    Args:
        number (int): A strictly positive integer.

    Returns:
        int: Steps needed to reach 1.

    Raises:
        ValueError: If number is zero or negative.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number % 2 == 0:   # even
            number //= 2
        else:                 # odd
            number = 3 * number + 1
        count += 1

    return count
