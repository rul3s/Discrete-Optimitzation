#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
Solution = namedtuple("Solution", ['taken', 'value', 'weight'])

def solve_it(input_data):
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    solutions = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    solutions.append(takeInOrder(items, capacity))
    solutions.append(takeHighValueFirst(items, capacity))
    solutions.append(takeLowWeightFirst(items, capacity))

    best_solution = solutions[0]
    for solution in solutions:
        if solution.value > best_solution.value:
            best_solution = solution

    # prepare the solution in the specified output format
    output_data = str(solution.value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution.taken))
    return output_data

def takeInOrder(items, capacity):
    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    return Solution(taken,value,weight)

def takeHighValueFirst(items, capacity):
    return takeInOrder(items.sort(key=lambda x: x.value),capacity)

def takeLowWeightFirst(items, capacity):
    return takeInOrder(items.sort(key=lambda x: x.weight),capacity)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')