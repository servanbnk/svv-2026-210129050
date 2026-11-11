"""Week 6: black-box tests designed from week6_design.md.

Tests Equivalence Partitioning (EP), Boundary Value Analysis (BVA),
and Decision Table testing against business_utils, math_utils, and text_utils.
"""
import pytest


# ---------------------------------------------------------------------------
# Function 1: business_utils.is_free_shipping
# Spec: Return True when the order total is 500 or more.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("total, expected", [
    (250, False),  # T01 EP E1 below threshold (< 500)
    (750, True),   # T02 EP E2 free shipping (>= 500)
])
def test_is_free_shipping_ep(business_utils, total, expected):
    """EP T01-T02. Unit test. Spec: Return True when the order total is 500 or more."""
    assert business_utils.is_free_shipping(total) is expected


@pytest.mark.parametrize("total, expected", [
    (499, False),  # T03 BVA edge 499/500: last below
    (500, True),   # T04 BVA edge 499/500: first free
    (501, True),   # T05 BVA edge 500/501: just above
])
def test_is_free_shipping_bva(business_utils, total, expected):
    """BVA T03-T05. Unit test. Spec: Return True when the order total is 500 or more."""
    assert business_utils.is_free_shipping(total) is expected


# ---------------------------------------------------------------------------
# Function 2: business_utils.late_fee
# Spec: Return the late fee; no fee when days_late is 0 or negative.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("days_late, daily_fee, expected", [
    (-5, 10, 0),   # T06 EP E1 negative days (< 0)
    (4, 10, 40),   # T07 EP E3 positive days (> 0)
])
def test_late_fee_ep(business_utils, days_late, daily_fee, expected):
    """EP T06-T07. Unit test. Spec: Return the late fee; no fee when days_late is 0 or negative."""
    assert business_utils.late_fee(days_late, daily_fee) == expected


@pytest.mark.parametrize("days_late, daily_fee, expected", [
    (-1, 10, 0),   # T08 BVA edge -1/0: negative boundary
    (0, 10, 0),    # T09 BVA edge 0/1: zero boundary
    (1, 10, 10),   # T10 BVA edge 0/1: first positive
])
def test_late_fee_bva(business_utils, days_late, daily_fee, expected):
    """BVA T08-T10. Unit test. Spec: Return the late fee; no fee when days_late is 0 or negative."""
    assert business_utils.late_fee(days_late, daily_fee) == expected


# ---------------------------------------------------------------------------
# Function 3: math_utils.clamp
# Spec: Return value limited to the range [low, high].
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("value, low, high, expected", [
    (-10, 0, 10, 0),  # T11 EP E1 below range (< 0)
    (5, 0, 10, 5),    # T12 EP E2 inside range (0..10)
    (20, 0, 10, 10),  # T13 EP E3 above range (> 10)
])
def test_clamp_ep(math_utils, value, low, high, expected):
    """EP T11-T13. Unit test. Spec: Return value limited to the range [low, high]."""
    assert math_utils.clamp(value, low, high) == expected


@pytest.mark.parametrize("value, low, high, expected", [
    (-1, 0, 10, 0),   # T14 BVA lower edge -1/0: just below low
    (0, 0, 10, 0),    # T15 BVA lower edge -1/0: exact low
    (10, 0, 10, 10),  # T16 BVA upper edge 10/11: exact high
    (11, 0, 10, 10),  # T17 BVA upper edge 10/11: just above high
])
def test_clamp_bva(math_utils, value, low, high, expected):
    """BVA T14-T17. Unit test. Spec: Return value limited to the range [low, high]."""
    assert math_utils.clamp(value, low, high) == expected


# ---------------------------------------------------------------------------
# Function 4: text_utils.truncate
# Spec: Return text cut to at most limit characters.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("text, limit, expected", [
    ("cat", 5, "cat"),        # T18 EP E1 shorter than limit
    ("elephant", 4, "elep"),  # T19 EP E2 longer than limit
])
def test_truncate_ep(text_utils, text, limit, expected):
    """EP T18-T19. Unit test. Spec: Return text cut to at most limit characters."""
    assert text_utils.truncate(text, limit) == expected


@pytest.mark.parametrize("text, limit, expected", [
    ("abcd", 5, "abcd"),    # T20 BVA edge (limit-1)/limit: one less
    ("abcde", 5, "abcde"),  # T21 BVA edge limit: exact length
    ("abcdef", 5, "abcde"), # T22 BVA edge limit/(limit+1): one more
])
def test_truncate_bva(text_utils, text, limit, expected):
    """BVA T20-T22. Unit test. Spec: Return text cut to at most limit characters."""
    assert text_utils.truncate(text, limit) == expected


# ---------------------------------------------------------------------------
# Decision Table: is_leap_year helper function
# Spec: A year is a leap year if divisible by 4, except end-of-century years
# which must also be divisible by 400.
# ---------------------------------------------------------------------------

def is_leap_year(year: int) -> bool:
    """Spec: A year is a leap year if divisible by 4, except end-of-century years which must also be divisible by 400."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


@pytest.mark.parametrize("year, expected", [
    (2023, False),  # DT R1 C1=F, C2=F, C3=F: not leap
    (2024, True),   # DT R2 C1=T, C2=F, C3=F: leap
    (1900, False),  # DT R3 C1=T, C2=T, C3=F: not leap (century non-400)
    (2000, True),   # DT R4 C1=T, C2=T, C3=T: leap (century 400)
])
def test_leap_year_decision_table(year, expected):
    """DT R1-R4. Unit test. Spec: A year is a leap year if divisible by 4, except end-of-century years which must also be divisible by 400."""
    assert is_leap_year(year) is expected
