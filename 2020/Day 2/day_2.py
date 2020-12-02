from typing import List
import os
import collections

def parse_input(file) -> List[List]:
    ''' Auxiliary function to parse the input file'''

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    output = []
    
    with open(os.path.join(__location__, file)) as input:

        for line in input:
            password = line.split(':')[1].strip()
            min_number = int(line.split(':')[0].split('-')[0])
            max_number = int(line.split(':')[0].split('-')[1].split(' ')[0])
            letter = line.split(':')[0].split(' ')[1]
            output.append([min_number, max_number, letter, password])

    return output

def day2_part1(input: List[List]) -> int:

    '''
    Approach: Using Counter
        - Counter provides us with an easy way to get the count of each letter in a string.
        - For each input, we get the Counter dict for the current password and then compare with our target letter.
        - If the letter count is in the expected range, we add one to our valid password counter.
    # Time: O(N * L) where N is the size of our input and L is the length of the passwords.
    # Space: O(L)
    '''

    valid_passwords_count = 0

    for min_number, max_number, letter, password in input:

        counter = collections.Counter(password)
        if min_number <= counter[letter] <= max_number: valid_passwords_count += 1

    return valid_passwords_count

def day2_part2(input: List[List]) -> int:
    '''
    Approach: Comparing with XOR
        - For part 2, the min and max numbers have became indexes and we can't have the target letter the same in both positions of the password string.
        - We can use the XOR operation to compare both positions. If both are True or False, it will return False. If any othe is True while the other is false, we get True as a result.
        - We need to be aware the indexes provided are not 0-based, so we need to subtract one from it.
    # Time: O(N), where N is the size of the input.
    # Space: O(1)
    '''

    valid_passwords_count = 0

    for left_index, right_index, letter, password in input:

        if (password[left_index - 1] == letter) ^ (password[right_index - 1] == letter): valid_passwords_count += 1

    return valid_passwords_count

def run_results_with_tests():

    test_data = [[1,3,'a','abcde'], [1,3,'b','cdefg'], [2,9,'c','ccccccccc']]
    test_expected_value_part_1 = 2
    test_expected_value_part_2 = 1

    # Tests for part 1
    test_run_1 = day2_part1(test_data)
    if test_expected_value_part_1 == test_run_1: print(f'Result Part 1 => {day2_part1(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_1} expected {test_expected_value_part_1}')

    print('=-=-==-==-=-=-=-=-=-=-=')
    
    # Tests for part 2
    test_run_2 = day2_part2(test_data)
    if test_expected_value_part_2 == test_run_2: print(f'Result Part 2 => {day2_part2(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_2} expected {test_expected_value_part_2}')
        
run_results_with_tests()

