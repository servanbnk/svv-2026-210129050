# Week 6 Test Design: Black-Box Testing (EP, BVA, Decision Table)

Student ID: 210129050

This document outlines the black-box test design for Week 6 covering Equivalence Partitioning (EP), Boundary Value Analysis (BVA), and a Decision Table for `is_leap_year`.

---

## Part A — EP and BVA for Four Functions

### 1. `business_utils.is_free_shipping(total)`
**Spec:** Return True when the order total is 500 or more.

- Boundary: `total = 500`
- Classes:
  - `E1` (Invalid / Below threshold): `total < 500` -> Expected `False`
  - `E2` (Valid / At or above threshold): `total >= 500` -> Expected `True`

| ID | Technique | Class or edge | Input | Expected |
|----|-----------|---------------|-------|----------|
| T01 | EP | E1 below threshold (< 500) | `total = 250` | False |
| T02 | EP | E2 free shipping (>= 500) | `total = 750` | True |
| T03 | BVA | edge 499/500: last below | `total = 499` | False |
| T04 | BVA | edge 499/500: first free | `total = 500` | True |
| T05 | BVA | edge 500/501: just above | `total = 501` | True |

---

### 2. `business_utils.late_fee(days_late, daily_fee)`
**Spec:** Return the late fee; no fee when days_late is 0 or negative. (When days_late > 0, fee is `days_late * daily_fee`).

- Boundary: `days_late = 0`
- Classes:
  - `E1` (No fee: negative): `days_late < 0` -> Expected `0`
  - `E2` (No fee: zero): `days_late == 0` -> Expected `0`
  - `E3` (Fee applied: positive): `days_late > 0` -> Expected `days_late * daily_fee`

| ID | Technique | Class or edge | Input | Expected |
|----|-----------|---------------|-------|----------|
| T06 | EP | E1 negative days (< 0) | `days_late = -5, daily_fee = 10` | 0 |
| T07 | EP | E3 positive days (> 0) | `days_late = 4, daily_fee = 10` | 40 |
| T08 | BVA | edge -1/0: negative boundary | `days_late = -1, daily_fee = 10` | 0 |
| T09 | BVA | edge 0/1: zero boundary | `days_late = 0, daily_fee = 10` | 0 |
| T10 | BVA | edge 0/1: first positive | `days_late = 1, daily_fee = 10` | 10 |

---

### 3. `math_utils.clamp(value, low, high)` (evaluated for `low=0, high=10`)
**Spec:** Return value limited to the range [low, high].

- Boundaries: `value = low (0)` and `value = high (10)`
- Classes:
  - `E1` (Below range): `value < low` -> Expected `low (0)`
  - `E2` (Within range): `low <= value <= high` -> Expected `value`
  - `E3` (Above range): `value > high` -> Expected `high (10)`

| ID | Technique | Class or edge | Input | Expected |
|----|-----------|---------------|-------|----------|
| T11 | EP | E1 below range (< 0) | `value = -10, low = 0, high = 10` | 0 |
| T12 | EP | E2 inside range (0..10) | `value = 5, low = 0, high = 10` | 5 |
| T13 | EP | E3 above range (> 10) | `value = 20, low = 0, high = 10` | 10 |
| T14 | BVA | lower edge -1/0: just below low | `value = -1, low = 0, high = 10` | 0 |
| T15 | BVA | lower edge -1/0: exact low | `value = 0, low = 0, high = 10` | 0 |
| T16 | BVA | upper edge 10/11: exact high | `value = 10, low = 0, high = 10` | 10 |
| T17 | BVA | upper edge 10/11: just above high | `value = 11, low = 0, high = 10` | 10 |

---

### 4. `text_utils.truncate(text, limit)` (evaluated for string length relative to limit)
**Spec:** Return text cut to at most limit characters.

- Boundary: `len(text) = limit`
- Classes:
  - `E1` (Shorter than limit): `len(text) < limit` -> Expected `text` (unchanged)
  - `E2` (Longer than limit): `len(text) > limit` -> Expected first `limit` chars

| ID | Technique | Class or edge | Input | Expected |
|----|-----------|---------------|-------|----------|
| T18 | EP | E1 shorter than limit | `text = "cat", limit = 5` | "cat" |
| T19 | EP | E2 longer than limit | `text = "elephant", limit = 4` | "elep" |
| T20 | BVA | edge (limit-1)/limit: one less | `text = "abcd", limit = 5` | "abcd" |
| T21 | BVA | edge limit: exact length | `text = "abcde", limit = 5` | "abcde" |
| T22 | BVA | edge limit/(limit+1): one more | `text = "abcdef", limit = 5` | "abcde" |

---

## Part B — Decision Table for `is_leap_year`

**Spec:** A year is a leap year if it is divisible by 4, except end-of-century years which must also be divisible by 400 (divisible by 100 alone is not leap).

### Condition Matrix (2^3 = 8 combinations)
- C1: Divisible by 4?
- C2: Divisible by 100?
- C3: Divisible by 400?

| Combination | C1: Div by 4? | C2: Div by 100? | C3: Div by 400? | Feasibility | Rule | Action (Leap Year?) | Example Year |
|-------------|---------------|-----------------|-----------------|-------------|------|---------------------|--------------|
| 1 | False | False | False | Possible | R1 | Not Leap (False) | 2023 |
| 2 | False | False | True | Impossible* | - | - | - |
| 3 | False | True | False | Impossible* | - | - | - |
| 4 | False | True | True | Impossible* | - | - | - |
| 5 | True | False | False | Possible | R2 | Leap (True) | 2024 |
| 6 | True | False | True | Impossible* | - | - | - |
| 7 | True | True | False | Possible | R3 | Not Leap (False) | 1900 |
| 8 | True | True | True | Possible | R4 | Leap (True) | 2000 |

*\*Note: A year divisible by 400 is mathematically always divisible by 100 and by 4. Similarly, a year divisible by 100 is always divisible by 4. Hence combinations 2, 3, 4, and 6 are mathematically impossible.*

### Simplified Decision Table Rules
| Rule | C1: Div by 4? | C2: Div by 100? | C3: Div by 400? | Action (is_leap_year) | Example Year |
|------|---------------|-----------------|-----------------|-----------------------|--------------|
| R1 | False | False | False | False | 2023 |
| R2 | True | False | False | True | 2024 |
| R3 | True | True | False | False | 1900 |
| R4 | True | True | True | True | 2000 |

---

## Comparison with Week 5 Findings
In Week 5, tests focused on single arbitrary representative inputs and general smoke tests. The Week 6 systematic BVA (such as testing exact threshold `total = 500` for `is_free_shipping` and `len(text) == limit` for `truncate`) clearly exposes boundary-shift off-by-one errors (e.g. `total > 500` rejecting 500, or slicing `text[:limit-1]` losing a character), and the decision table ensures corner cases like century leap years (1900 vs 2000) are rigorously verified.
