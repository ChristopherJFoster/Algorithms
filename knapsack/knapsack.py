#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity):
    maxes = {}

    for i in range(len(items)):
        maxes[i] = {}
        for j in range(1, capacity + 1):
            if i == 0:
                if items[i].size <= j:
                    maxes[i][j] = {'Chosen': [items[i].index],
                                   'Value': items[i].value}
                else:
                    maxes[i][j] = {'Chosen': [], 'Value': 0}
            elif j - items[i].size == 0:
                if maxes[i - 1][j]['Value'] > items[i].value:
                    maxes[i][j] = {'Chosen': maxes[i - 1][j]['Chosen'],
                                   'Value': maxes[i - 1][j]['Value']}
                else:
                    maxes[i][j] = {'Chosen': [items[i].index],
                                   'Value': items[i].value}
            elif j - items[i].size > 0:
                if maxes[i - 1][j]['Value'] > items[i].value + maxes[i - 1][j - items[i].size]['Value']:
                    maxes[i][j] = {'Chosen': maxes[i - 1][j]['Chosen'],
                                   'Value': maxes[i - 1][j]['Value']}
                else:
                    new_max = {'Chosen': maxes[i - 1][j - items[i].size]['Chosen'],
                               'Value': maxes[i - 1][j - items[i].size]['Value']}
                    print('new_max: ', new_max)
                    new_max['Chosen'].append(items[i].index)
                    new_max['Value'] += items[i].value
                    print('new_max: ', new_max)
                    maxes[i][j] = new_max
                    print('maxes[i][j]: ', maxes[i][j])
            else:
                maxes[i][j] = {'Chosen': [], 'Value': 0}
    # for i in maxes:
    #     for j in maxes[i]:
    #         print(i, j, maxes[i][j])
    return maxes[len(items) - 1][capacity]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
