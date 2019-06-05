#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# This solution actually works for larger ns, but I wrote not to accept a cache as an argument (which I think is better than requiring a cache). However, the tests in test_eating_cookies.py _do_ pass in a cache, which breaks my code. I added two lines to reject the incoming cache.

def eating_cookies(n, cache=None):
    # The following two lines reject any cache passed in as an argument:
    if cache == None or cache[0] == 0:
        cache = {0: 1, 1: 1, 2: 2}
    if n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(n - 1, cache) + \
            eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


print(eating_cookies(50))
