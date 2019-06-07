#!/usr/bin/python

import sys


def making_change(amount, denominations):
    cache = {i: 1 if i == 0 else 0 for i in range(0, amount + 1)}
    for i in denominations:
        for j in range(1, amount + 1):
            if j - i >= 0:
                cache[j] = cache[j] + cache[j - i]
    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
