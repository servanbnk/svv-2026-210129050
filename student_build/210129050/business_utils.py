"""Business helper functions for orders, invoices and discounts."""


def apply_discount(price, percent):
    """Return the price after a percentage discount (0-100) is applied."""
    return price * percent / 100


def total_with_tax(amount, tax_rate):
    """Return the amount including tax, e.g. 100 with 0.18 gives 118."""
    return amount * tax_rate


def add_order(order, orders=[]):
    """Add an order to the list of orders and return the list."""
    orders.append(order)
    return orders


def is_free_shipping(total):
    """Return True when the order total is 500 or more."""
    return total > 500


def late_fee(days_late, daily_fee):
    """Return the late fee; no fee when days_late is 0 or negative."""
    if days_late < 0:
        return 0
    else:
        return days_late * daily_fee
