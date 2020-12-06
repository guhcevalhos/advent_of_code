from typing import List
import os
import json
import collections

def parse_input(file) -> List[List]:
    ''' Auxiliary function to parse the input file'''

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    current_entry = []
    input = []

    with open(os.path.join(__location__, file)) as reader:
        
        for line in reader.readlines():
            # Get lines that belong to same document
            if line.strip(): current_entry.append(f'{"".join(line.strip())} ')
            else:
            # When finished with a sequence of data, get dict representation for document
                input.append(''.join(current_entry))
                current_entry = []

    # By the end of the file, there's still one remaining entry.
    input.append(''.join(current_entry))

    return input


def day6_part1(input: List[List]) -> int:
    '''
    Transforms list input into a set of individual questions that show up in the answers, from them, we just need to count how many questions showed up.
    # Time: O(N)
    # Space: O(L), where L is the number of questions where we have yes in the input.
    '''

    s = 0

    for entry in input:
        # Transforming entry in set and removing extra space entry, as it is required by part 2, but not in here.
        individual_questions_yes = set(entry) - {' '}
        s += len(individual_questions_yes)

    return s


def day6_part2(input: List[List]) -> int:
    '''
    On part 2 we need to check how many questions had yes, but only if all people answered yes.
    For that, we check the amount of people in answering, if 1, we just get all questions from this person.
    If more than one person responded, we need to check for how many questions have the same number of yes as the number of people, using a Counter.
    # Time: O(N * L), where L is the number of questions where we have yes in the input.where L is the number of questions where we have yes in the input.
    # Space: O(P + L), where P is the number of people answering the question. 
    '''
    s = 0

    for entry in input:            

        input_per_person = entry.split()
        amount_of_people = len(input_per_person)
        number_of_yes_per_question = collections.Counter(''.join(input_per_person))

        if amount_of_people == 1: s += len(number_of_yes_per_question)
        else:
            for count in number_of_yes_per_question.values():
                if count == amount_of_people: s += 1

    return s

def run_results_with_tests():
    ''' Test function based on example and run for real input, if results for tests are the expected values.'''

    test_expected_value_part_1 = 11
    test_expected_value_part_2 = 6

    # Tests for part 1
    test_run_1 = day6_part1(parse_input('test_input'))
    if test_expected_value_part_1 == test_run_1: print(f'Result Part 1 => {day6_part1(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_1} expected {test_expected_value_part_1}')

    print('=-=-==-==-=-=-=-=-=-=-=')
    
    # Tests for part 2
    test_run_2 = day6_part2(parse_input('test_input'))

    if test_expected_value_part_2 == test_run_2: print(f'Result Part 2 => {day6_part2(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_2} expected {test_expected_value_part_2}')

run_results_with_tests()