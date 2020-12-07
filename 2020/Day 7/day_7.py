from typing import List
import os
import json
import collections

debug = True

def parse_input(file) -> List[List]:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    bags = {}

    for line in [line.strip() for line in open(os.path.join(__location__, file)).readlines()]:

        type_of_bag = line.split('bags')[0].strip()
        contained_bags = [bag.strip().strip('.') for bag in line.split('contain')[1].strip().split(',')]

        bags[type_of_bag] = {}

        for bag in contained_bags:
            
            if bag != 'no other bags':
                quantity = int(bag.split(' ')[0])
                bag_color = ' '.join(bag.split(' ')[1:3])

                bags[type_of_bag][bag_color] = quantity

    return bags

def day6_part1(input: dict) -> int:
    '''
    BFS Graph Traversal
    '''
    total = 0
    print(input)
    
    for bag in input:
        
        if bag != 'shiny gold':

            visited = set()
            queue = collections.deque()
            found = False

            if debug: print(f'Initial bag: {bag}')

            for color in input[bag]:
                queue.append(color)
            if debug: print(f'Bags available in initial bag: {queue}')

            while queue:
                current_bag = queue.popleft()
                if debug: print(f'Current Bag: {current_bag}')
                if current_bag == 'shiny gold': found = True

                visited.add(current_bag)
                if debug: print(f'Already checked bags: {visited}')

                for neighbor in input[current_bag].keys():
                    if debug: print(f'{neighbor=}')
                    if neighbor == 'shiny gold': 
                        if debug: print(f'Found Shiny gold')
                        found = True
                    else:
                        if neighbor not in visited:
                            if debug: print(f'Adding {neighbor} to queue')
                            queue.append(neighbor)

                if debug: print('----')

            if found: total += 1
            if debug: print(f'Total so far: {total=}')
            if debug: print('=-=-=-=-=-=-=-=-=-')

    return total

def day6_part2(input: List[List]) -> int:
    '''
    BFS Graph Traversal
    '''
    total = 0
    
    queue = collections.deque()
    multipliers = {'shiny gold': 1}
    visited = set()

    queue.append('shiny gold')

    while queue:
        current_bag = queue.popleft()
        if debug: print(f'Current Bag: {current_bag}')

        visited.add(current_bag)

        if debug: print(f'Already checked bags: {visited}')

        for neighbor in input[current_bag].keys():
            if debug: print(f'{neighbor=}')
            if neighbor and neighbor not in visited:
                if debug: print(f'Adding {neighbor} to queue')
                queue.append(neighbor)
                if debug: print(f'Adding {multipliers[current_bag]} * {input[current_bag][neighbor]}')
                total += multipliers[current_bag] * input[current_bag][neighbor]
                multipliers[neighbor] = multipliers[current_bag] * input[current_bag][neighbor]

        if debug: print('-------')

        if debug: print(f'Multipliers: {multipliers}')

    if debug: print(f'Total so far: {total=}')
    if debug: print('=-=-=-=-=-=-=-=-=-')

    return total

def run_results_with_tests():
    ''' Test function based on example and run for real input, if results for tests are the expected values.'''

    test_expected_value_part_1 = 4
    test_expected_value_part_2_input1 = 32
    test_expected_value_part_2_input2 = 126

    # Tests for part 1
    # test_run_1 = day6_part1(parse_input('test_input'))
    # if test_expected_value_part_1 == test_run_1: print(f'Result Part 1 => {day6_part1(parse_input("input"))}')
    # else: print(f'Failed Test Case: Got {test_run_1} expected {test_expected_value_part_1}')

    print('=-=-==-==-=-=-=-=-=-=-=')
    
    # Tests for part 2
    # test_run_2_input1 = day6_part2(parse_input('test_input'))
    # test_run_2_input2 = day6_part2(parse_input('test_input2'))

    # if test_expected_value_part_2_input1 == test_run_2_input1 and test_expected_value_part_2_input2 == test_run_2_input2: print(f'Result Part 2 => {day6_part2(parse_input("input"))}')
    # else: print(f'Failed Test Case: Got {test_run_2_input1} and {test_run_2_input2} expected {test_expected_value_part_2_input1} and {test_expected_value_part_2_input2}')

# run_results_with_tests()
# day6_part2(parse_input('test_input'))
# day6_part2(parse_input('test_input2'))
day6_part2(parse_input("input"))