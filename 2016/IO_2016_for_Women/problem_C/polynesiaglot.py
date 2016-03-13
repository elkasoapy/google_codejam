#!/usr/bin/env python

################################################################################
#
# Google Code Jam to I/O for Women 2016
#
# Problem C - Polynesiaglot
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os

LANGUAGE_ELEMENTS = 3
MAX_LIMIT = 1000000007
precomputed_results = {}


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file[0].strip())

    for i in xrange(1, len(all_file)):
        current_problem = all_file[i].strip().split(' ')

        if LANGUAGE_ELEMENTS != len(current_problem):
            print 'Wrong formatted file!'
            sys.exit()

        problem_list.append([int(x) for x in current_problem])

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def solve_polynesiaglot(consonants, vowels, length):
    # Check if we have precomputed results
    if vowels in precomputed_results:
        vowels_precomputed_results = precomputed_results[vowels]
    else:
        vowels_precomputed_results = {}

    if consonants in vowels_precomputed_results:
        consonants_precomputed_results = vowels_precomputed_results[consonants]
    else:
        consonants_precomputed_results = {}

    if length in consonants_precomputed_results:
        return consonants_precomputed_results[length]
    else:
        # Any consonant in a word must be immediately followed by a vowel.
        if length == 1:
            n_words = vowels
        elif length == 2:
            n_words = vowels * (consonants + vowels)
        else:
            n_words = vowels * solve_polynesiaglot(consonants, vowels, length - 1) + \
                      (consonants * vowels) * solve_polynesiaglot(consonants, vowels, length - 2)

        # Store the precomputed results
        consonants_precomputed_results[length] = n_words
        vowels_precomputed_results[consonants] = consonants_precomputed_results
        precomputed_results[vowels] = vowels_precomputed_results

    return n_words % MAX_LIMIT


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python polynesiaglot.py <input_file> <output_file>'
        sys.exit()

    problems_file = sys.argv[1]
    if not os.path.isfile(problems_file):
        print 'Incorrect first parameter given to this script: ' + sys.argv[1]
        print 'The given file does not exist'
        sys.exit()

    # Read the input data
    problem_values = read_problem_file(problems_file)

    # Process the problems
    output = []
    for index, problem in enumerate(problem_values):
        solution = solve_polynesiaglot(problem[0], problem[1], problem[2])
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
