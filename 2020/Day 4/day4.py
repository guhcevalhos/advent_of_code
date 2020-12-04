from typing import List
import os
import json

# Set debug output throughout script
debug = False


def get_json_from_string(current_entry: str) -> json:

    current_json = []

    # Transform in key-value pair and put in JSON format.
    for entry in ''.join(current_entry).split():
        key = entry.split(':')[0]
        value = entry.split(':')[1]
        current_json.append((f'"{key}":"{value}"'))

    # Create a JSON formatted string and return  
    json_formatted_string = f'{{{",".join(current_json)}}}'
    return json.loads(''.join(json_formatted_string))


def parse_input(file) -> List[List]:
    ''' Auxiliary function to parse the input file'''

    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    current_entry = []
    input = []

    with open(os.path.join(__location__, file)) as reader:
        
        for line in reader.readlines():
            # Get lines that belong to same document
            if line.strip(): current_entry.append(f' {line.strip()} ')
            else:
            # When finished with a sequence of data, get dict representation for document
                input.append(get_json_from_string(''.join(current_entry)))
                current_entry = []

    # By the end of the file, there's still one remaining entry.
    input.append(get_json_from_string(''.join(current_entry)))
                                 
    return input


def day4_part1(input: List[str]) -> int:

    '''
    By getting a list of the required fields, we can build a set and compare with the set given by entry.keys().
    If the required_fields set is bigger, then the passport is invalid, as it lacks required fields.
    # Time: O(N * R) where N is the size of the input and R is the number of required fields ~ O(N)
    # Space: O(1)
    '''

    '''
    The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

    Count the number of valid passports - those that have all required fields. Treat cid as optional.
    '''
    passport_count = 0
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    for entry in input: 
        if entry.keys() >= required_keys: passport_count += 1

    return passport_count


def day4_part2(input: List[str]) -> int:

    '''
    For part 2, we need to check each entry in the passport data to confirm validity.
    # Time: O(N * F) where N is the number of documents in the input and F is the number of fields in each document. ~ O(N)
    # Space: O(1)
    '''

    '''
    Field Requirements:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''

    passport_count = 0
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    for entry in input:
        if debug: print(entry)
        if entry.keys() >= required_keys: 

            if len(entry['byr']) == 4 and 1920 <= int(entry['byr']) <= 2002 and \
                len(entry['iyr']) == 4 and 2010 <= int(entry['iyr']) <= 2020 and \
                len(entry['eyr']) == 4 and 2020 <= int(entry['eyr']) <= 2030 and \
                entry['hcl'][0] == '#' and all(c in 'abcdef0123456789' for c in entry['hcl'][1:]) and \
                entry['ecl'] in {'amb','blu','brn', 'gry', 'grn' ,'hzl', 'oth'} and \
                len(entry['pid']) == 9 and \
                150 <= int(entry['hgt'][:-2]) <= 193 if entry['hgt'][-2:] == 'cm' else 59 <= int(entry['hgt'][:-2]) <= 76 if entry['hgt'][-2:] == 'in' else False:
                    passport_count += 1
            else:
                if debug: print('Invalid! Incorrect Fields')
        else:
            if debug: print('Invalid! Missing fields')

    return passport_count
        
        
def run_results_with_tests():
    ''' Test function based on example and run for real input, if results for tests are the expected values.'''

    test_expected_value_part_1 = 2
    
    # Part 2 is validated on a different set of examples: valid_passports and invalid_passports
    test_expected_value_part_2_valid = 4
    test_expected_value_part_2_invalid = 0

    # Tests for part 1
    test_run_1 = day4_part1(parse_input('test_input'))
    if test_expected_value_part_1 == test_run_1: print(f'Result Part 1 => {day4_part1(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_1} expected {test_expected_value_part_1}')

    print('=-=-==-==-=-=-=-=-=-=-=')
    
    # # Tests for part 2
    test_run_2_valid = day4_part2(parse_input('valid_passports'))
    test_run_2_invalid = day4_part2(parse_input('invalid_passports'))

    if test_expected_value_part_2_valid == test_run_2_valid and test_expected_value_part_2_invalid == test_run_2_invalid: print(f'Result Part 2 => {day4_part2(parse_input("input"))}')
    else: print(f'Failed Test Case: Got {test_run_2_valid} and {test_run_2_invalid} expected {test_expected_value_part_2_valid} and {test_expected_value_part_2_invalid}')

run_results_with_tests()