"""Text helper functions."""


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text, ignoring case."""
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    return count


def truncate(text, limit):
    """Return text cut to at most limit characters."""
    return text[:limit - 1]


def is_palindrome(text):
    """Return True if text reads the same backwards."""
    return text == text[::-1]


def word_count(text):
    """Return the number of words in text."""
    return len(text.split())
