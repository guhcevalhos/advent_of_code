from typing import List
from math import ceil, floor
import os

debug = False

def parse_input(file) -> List[List]:
    ''' Auxiliary function to parse the input file'''

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    return [line.strip() for line in open(os.path.join(__location__, file)).readlines()]

def day5_part1(input: List[List]) -> int:
    ''' Return highest seat ID on a boarding pass'''

    ''' Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
    In this example, the seat has ID 44 * 8 + 5 = 357. 
    
    128 rows on the plane, (numbered 0 through 127)
    '''
    
    '''
    We apply binary search according to the instruction provided to figure out the row and column for the set, based on the input provided.
    # Time: O(N * L), where L is the size of each boarding pass = 10 ~ O(N)
    # Space: O(1)
    '''

    max_seat_id = float('-inf')

    for boarding_pass in input:

        lower = 0
        upper = 127
        row = 0
        column = 0

        if debug: print(f'Boarding Pass: {boarding_pass}')

        for letter in boarding_pass[:7]:

            if debug: print(f'Current Letter: {letter}')
            mid = lower + (upper - lower) / 2
            if letter == 'F': upper = floor(mid)
            else: lower = ceil(mid)
            if debug: print(f'Lower: {lower} | Mid: {mid} | Upper: {upper}')

        row = lower
        if debug: print(f'Row found: {row}')
        left = 0
        right = 7
        if debug: print(f'--')

        for letter in boarding_pass[7:]:
            
            if debug: print(f'Current Letter: {letter}')
            mid = left + (right - left) / 2
            if letter == 'L': right = floor(mid)
            else: left = ceil(mid)
            if debug: print(f'Left: {left} | Mid: {mid} | Upper: {right}')

        column = left
        if debug: print(f'Column found: {column}')
        
        if debug: print(f'Current Seat Id: {row * 8 + column} | Max Seen: {max_seat_id}')
        max_seat_id = max(max_seat_id, row * 8 + column)
        if debug: print('----')

    return max_seat_id


def get_seat_id(boarding_pass: List[List]) -> int:
    ''' Auxiliary function to return seat ID from a boarding pass, similar to first one'''

    ''' Every seat also has a unique seat ID: multiply the row by 8, then add the column. 
    In this example, the seat has ID 44 * 8 + 5 = 357. 
    
    128 rows on the plane, (numbered 0 through 127)
    '''

    lower = 0
    upper = 127
    row = 0
    column = 0

    if debug: print(f'Boarding Pass: {boarding_pass}')

    for letter in boarding_pass[:7]:

        if debug: print(f'Current Letter: {letter}')
        mid = lower + (upper - lower) / 2
        if letter == 'F': upper = floor(mid)
        else: lower = ceil(mid)
        if debug: print(f'Lower: {lower} | Mid: {mid} | Upper: {upper}')

    row = lower
    if debug: print(f'Row found: {row}')
    left = 0
    right = 7
    if debug: print(f'--')

    for letter in boarding_pass[7:]:
        
        if debug: print(f'Current Letter: {letter}')
        mid = left + (right - left) / 2
        if letter == 'L': right = floor(mid)
        else: left = ceil(mid)
        if debug: print(f'Left: {left} | Mid: {mid} | Upper: {right}')

    column = left
    if debug: print(f'Column found: {column}')
    
    if debug: print(f'Current Seat Id: {row * 8 + column} | Max Seen: {max_seat_id}')
    return row * 8 + column

def day5_part2(input: List[List]) -> int:

    '''
    We use the aux function get_set_id() to get all Ids from the input.
    After that, we sort them and do a linear search to figure out which id is missing.
    # Time: O(N**2 Lg N)
    # Space: O(N)
    '''

    seats = []

    for boarding_pass in input:
        seats.append(get_seat_id(boarding_pass))

    seats.sort()
    print(seats)

    for index, id in enumerate(seats):
        if id + 1 != seats[index + 1]: return id + 1

    
def run_results_with_tests():
    ''' Test function based on example and run for real input, if results for test are expected.'''

    test_data = [
        'FBFBBFFRLR',
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'BBFFBBFRLL'
    ]

    test_expected_value_part_1 = 820

    # Tests for part 1
    test_run_1 = day5_part1(test_data)
    if test_expected_value_part_1 == test_run_1: print(f'Result Part 1 => {day5_part1(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_1} expected {test_expected_value_part_1}')

    print('=-=-==-==-=-=-=-=-=-=-=')
    
    # Part 2, as no test data as provided
    print(day5_part2(parse_input("input")))

run_results_with_tests()