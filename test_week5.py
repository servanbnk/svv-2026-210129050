"""Week 5: my unit tests.

Tests are written following the Arrange, Act, Assert pattern and rely on
the course fixtures math_utils, text_utils, and business_utils.
"""


# -------------------------------------------------------------------------
# Smoke tests (at least 3 tests starting with test_smoke_)
# -------------------------------------------------------------------------

def test_smoke_is_even_with_even_number(math_utils):
    """Unit test. Spec: Return True if n is an even number."""
    # Arrange
    n = 4
    # Act
    result = math_utils.is_even(n)
    # Assert
    assert result is True


def test_smoke_is_palindrome_simple_word(text_utils):
    """Unit test. Spec: Return True if text reads the same backwards."""
    # Arrange
    text = "radar"
    # Act
    result = text_utils.is_palindrome(text)
    # Assert
    assert result is True


def test_smoke_word_count_simple_sentence(text_utils):
    """Unit test. Spec: Return the number of words in text."""
    # Arrange
    text = "hello world from pytest"
    # Act
    result = text_utils.word_count(text)
    # Assert
    assert result == 4


# -------------------------------------------------------------------------
# business_utils unit tests
# -------------------------------------------------------------------------

def test_apply_discount_twenty_percent(business_utils):
    """Unit test. Spec: Return the price after a percentage discount (0-100) is applied."""
    # Arrange
    price = 100.0
    percent = 20
    # Act
    result = business_utils.apply_discount(price, percent)
    # Assert
    assert result == 80.0


def test_total_with_tax_eighteen_percent(business_utils):
    """Unit test. Spec: Return the amount including tax, e.g. 100 with 0.18 gives 118."""
    # Arrange
    amount = 100.0
    tax_rate = 0.18
    # Act
    result = business_utils.total_with_tax(amount, tax_rate)
    # Assert
    assert result == 118.0


def test_add_order_independent_calls(business_utils):
    """Unit test. Spec: Add an order to the list of orders and return the list."""
    # Arrange & Act
    first_list = business_utils.add_order("order_1")
    second_list = business_utils.add_order("order_2")
    # Assert: without passing an existing list, each call should start fresh
    assert first_list == ["order_1"]
    assert second_list == ["order_2"]


def test_is_free_shipping_boundary_exact_five_hundred(business_utils):
    """Unit test. Spec: Return True when the order total is 500 or more."""
    # Arrange
    total = 500
    # Act
    result = business_utils.is_free_shipping(total)
    # Assert
    assert result is True


# -------------------------------------------------------------------------
# math_utils unit tests
# -------------------------------------------------------------------------

def test_average_empty_list_returns_zero(math_utils):
    """Unit test. Spec: Return the average of a list of numbers, or 0 for an empty list."""
    # Arrange
    numbers = []
    # Act
    result = math_utils.average(numbers)
    # Assert
    assert result == 0


def test_clamp_above_high_boundary(math_utils):
    """Unit test. Spec: Return value limited to the range [low, high]."""
    # Arrange
    value = 25
    low = 0
    high = 10
    # Act
    result = math_utils.clamp(value, low, high)
    # Assert
    assert result == 10


def test_factorial_five(math_utils):
    """Unit test. Spec: Return n! for n >= 0."""
    # Arrange
    n = 5
    # Act
    result = math_utils.factorial(n)
    # Assert
    assert result == 120


# -------------------------------------------------------------------------
# text_utils unit tests
# -------------------------------------------------------------------------

def test_count_vowels_with_uppercase(text_utils):
    """Unit test. Spec: Return the number of vowels (a, e, i, o, u) in text, ignoring case."""
    # Arrange
    text = "Apple Orange"
    # Act
    result = text_utils.count_vowels(text)
    # Assert
    assert result == 5


def test_truncate_boundary_exact_length(text_utils):
    """Unit test. Spec: Return text cut to at most limit characters."""
    # Arrange
    text = "Testing123"
    limit = 7
    # Act
    result = text_utils.truncate(text, limit)
    # Assert
    assert result == "Testing"
