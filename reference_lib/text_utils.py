"""Text helper functions."""


def count_vowels(text):
    """Spec: Return the number of vowels (a, e, i, o, u) in text, ignoring case."""
    count = 0
    vowels = "aeiouAEIOU"
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def truncate(text, limit):
    """Spec: Return text cut to at most limit characters."""
    return text[:limit]


def is_palindrome(text):
    """Spec: Return True if text reads the same backwards."""
    return text == text[::-1]


def word_count(text):
    """Spec: Return the number of words in text."""
    return len(text.split())
