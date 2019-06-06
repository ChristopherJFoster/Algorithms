#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         capacity = int(sys.argv[2])
#         file_location = sys.argv[1].strip()
#         file_contents = open(file_location, 'r')
#         items = []

#         for line in file_contents.readlines():
#             data = line.rstrip().split()
#             items.append(Item(int(data[0]), int(data[1]), int(data[2])))

#         file_contents.close()
#         print(knapsack_solver(items, capacity))
#     else:
#         print('Usage: knapsack.py [filename] [capacity]')


def knapsack_solver(items, capacity):
    max = []

    for i in range(len(items)):
        def add(j, combo={'Chosen': [], 'Size': 0, 'Value': 0}):
            # print(combo['Size'] + items[j].size, capacity)
            if combo['Size'] + items[j].size <= capacity:
                combo['Chosen'].append(items[j].index)
                combo['Size'] += items[j].size
                combo['Value'] += items[j].value

            if j == len(items) - 1:
                print('appended combo: ', combo)
                max.append(combo)

            else:
                print('else')
                for k in range(j + 1, len(items)):
                    print('passed combo: ', combo, k, i)
                    add(k, combo)

        add(i)

        # Compare previous max value combo with every combo of items assuming items[i] as a starting point and set new max equal to the highest value combo.

        max = [sorted(max, key=lambda item: item['Value'], reverse=True)[0]]

    # cleans up output for tests
    max = {'Chosen': max[0]['Chosen'], 'Value': max[0]['Value']}
    return max


itemlist = [Item(index=1, size=4, value=8), Item(
    index=2, size=4, value=2), Item(index=3, size=6, value=6)]

print('final answer: ', knapsack_solver(itemlist, 10))
