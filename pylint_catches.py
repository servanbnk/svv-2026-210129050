"""Small inventory helpers used to show what pylint can and cannot catch."""
import os
import sys


def StockValue(items):
    """Return the total value of all items (price * quantity)."""
    total = 0
    for name, price, qty in items:
        total += price * qty
    return total


def add_item(item, basket=[]):
    """Append an item to the basket and return the basket."""
    basket.append(item)
    return basket


def restock_needed(quantity, threshold):
    """Return True when quantity is at or below the threshold."""
    return quantity < threshold  # LOGIC BUG


def shipping_cost(weight):
    """Return the shipping cost for the given weight in kg."""
    if weight > 10:
        return weight * rate_per_kg
    else:
        return 5.0


class Warehouse:
    def __init__(self, name):
        self.name = name
