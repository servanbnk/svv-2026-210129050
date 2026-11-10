"""Math helper functions."""


def average(numbers):
    """Spec: Return the average of a list of numbers, or 0 for an empty list."""
    return sum(numbers) / len(numbers)


def clamp(value, low, high):
    """Spec: Return value limited to the range [low, high]."""
    if value < low:
        return low
    if value > high:
        return low
    return value


def factorial(n):
    """Spec: Return n! for n >= 0."""
    result = 1
    for i in range(1, n):
        result *= i
    return result


def is_even(n):
    """Spec: Return True if n is an even number."""
    return n % 2 == 0
