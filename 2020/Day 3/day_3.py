from typing import List
import os

def parse_input(file) -> List[List]:
    ''' Auxiliary function to parse the input file'''

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    return [line.strip() for line in open(os.path.join(__location__, file)).readlines()]


def day3(input: List[List], slope_right: int, slope_down: int) -> int:
    ''' Adapted function from Part 1 to general case in part 2'''

    '''
        - Iteratively, we check each value as we go down the slope, taking care to not go out of bounds when the column goes over the size of the line.
        - When that is the case, we go back to the beginning by subtracting len(line) from the total.
    # Time: O(N) where N is the number of lines in the input
    # Space: O(1)
    '''

    tree_count = 0

    row = slope_down
    column = slope_right

    line_len = len(input[0])

    while row < len(input):
        # print(f'Row: {row} | Column: {column} | Found: {input[row][column]}')
        if input[row][column] == '#': tree_count += 1

        if column + slope_right < line_len: column += slope_right
        else: column = column + slope_right - line_len
        row += slope_down

    return tree_count

def run_results_with_tests():
    ''' Test function based on example and run for real input, if results for test are expected.'''

    test_data = [
                '..##.......',
                '#...#...#..',
                '.#....#..#.',
                '..#.#...#.#',
                '.#...##..#.',
                '..#.##.....',
                '.#.#.#....#',
                '.#........#',
                '#.##...#...',
                '#...##....#',
                '.#..#...#.#']

    test_expected_value_part_1 = 7
    test_expected_value_part_2 = 336

    input = parse_input("input")

    # Tests for part 1
    test_run_1 = day3(test_data, 3, 1)
    if test_expected_value_part_1 == test_run_1: print(f'Result Part 1 => {day3(input, 3, 1)}')
    else: print(f'Failed Test Case: Got {test_run_1} expected {test_expected_value_part_1}')

    print('=-=-==-==-=-=-=-=-=-=-=')
    
    # Tests for part 2
    test_run_2 = day3(test_data, 1, 1) * test_run_1 * day3(test_data, 5, 1) * day3(test_data, 7, 1) * day3(test_data, 1, 2)
    if test_expected_value_part_2 == test_run_2: print(f'Result Part 2 => {day3(input, 1, 1) * day3(input, 3, 1) * day3(input, 5, 1) * day3(input, 7, 1) * day3(input, 1, 2)}')
    else: print(f'Failed Test Case: Got {test_run_2} expected {test_expected_value_part_2}')

run_results_with_tests()