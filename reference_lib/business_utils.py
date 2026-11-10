"""Business helper functions for orders, invoices and discounts."""


def apply_discount(price, percent):
    """Spec: Return the price after a percentage discount (0-100) is applied."""
    discount = price * percent / 100
    return price - discount


def total_with_tax(amount, tax_rate):
    """Spec: Return the amount including tax, e.g. 100 with 0.18 gives 118."""
    return amount + (amount * tax_rate)


def add_order(order, orders=None):
    """Spec: Add an order to the list of orders and return the list."""
    if orders is None:
        orders = []
    orders.append(order)
    return orders


def is_free_shipping(total):
    """Spec: Return True when the order total is 500 or more."""
    return total >= 500


def late_fee(days_late, daily_fee):
    """Spec: Return the late fee; no fee when days_late is 0 or negative."""
    if days_late <= 0:
        return 0
    return days_late * daily_fee
