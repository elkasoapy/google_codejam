#!/usr/bin/env python

################################################################################
#
# Google Code Jam to I/O for Women 2016
#
# Problem B - Dance Around The Clock
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os

DANCE_ELEMENTS = 3


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file[0].strip())

    for i in xrange(1, len(all_file)):
        current_problem = all_file[i].strip().split(' ')

        if DANCE_ELEMENTS != len(current_problem):
            print 'Wrong formatted file!'
            sys.exit()

        problem_list.append([int(x) for x in current_problem])

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def solve_dance(dancers, k_dancer, n_rounds):
    solution_dance = []

    # Each time dancers rounds have gone round, everything is still the same
    n_rounds = n_rounds % dancers

    if (k_dancer % 2) == 1:
        # k_dancer is odd
        position_k_dancer_round_n = (k_dancer + n_rounds) % dancers

        k_left = (position_k_dancer_round_n + n_rounds + 1) % dancers
        k_right = (position_k_dancer_round_n + n_rounds - 1) % dancers
    else:
        # k_dancer is even
        position_k_dancer_round_n = (k_dancer + dancers - n_rounds) % dancers
        k_left = (position_k_dancer_round_n - n_rounds + dancers + 1) % dancers
        k_right = (position_k_dancer_round_n - n_rounds + dancers - 1) % dancers

    # As the clock starts with 1, move 0 to be dancers instead
    if k_left == 0:
        k_left = dancers
    if k_right == 0:
        k_right = dancers

    solution_dance.append(k_left)
    solution_dance.append(k_right)

    return solution_dance


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python dance_clock.py <input_file> <output_file>'
        sys.exit()

    problems_file = sys.argv[1]
    if not os.path.isfile(problems_file):
        print 'Incorrect first parameter given to this script: ' + sys.argv[1]
        print 'The given file does not exist'
        sys.exit()

    # Read the input data
    problems_values = read_problem_file(problems_file)

    # Process the problems
    output = []
    for index, problem in enumerate(problems_values):
        solution = solve_dance(problem[0], problem[1], problem[2])
        line = 'Case #' + str(index + 1) + ': ' + ' '.join(str(x) for x in solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
