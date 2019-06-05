#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # sets up results list with lists equal to the total number of permutations
    result = [[] for _ in range(3**n)]

    def rps(s):
        # base case
        if s == 0:
            return
        # count ensures that on each pass through rps(s), one play is added to each permutation
        count = 0
        while count < 3**n:
            # Each for loop adds a play to the appropriate list in result, then bumps the count up
            for _ in range(3**s//3):
                result[count].append('rock')
                count += 1
            for _ in range(3**s//3):
                result[count].append('paper')
                count += 1
            for _ in range(3**s//3):
                result[count].append('scissors')
                count += 1
        # once a pass is done, the next smallest pass is called, down to rps(0)
        rps(s - 1)
    rps(n)

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
