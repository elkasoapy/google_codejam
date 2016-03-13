#!/usr/bin/env python

################################################################################
#
# Google Code Jam to I/O for Women 2016
#
# Problem A - Cody's Jams
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os

SALE_VALUE = 0.75


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file[0].strip())

    for i in xrange(1, len(all_file), 2):
        n_elements = int(all_file[i].strip())
        elements = all_file[i + 1].strip().split(' ')
        sale_elements = [int(x) for x in elements]

        if 2 * n_elements != len(sale_elements):
            print 'Wrong formatted file!'
            sys.exit()

        problem_list.append(sale_elements)

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def solve_prices(prices):
    sale_prices = []
    not_discount = []

    for item in prices:
        if item not in not_discount:
            sale_prices.append(item)
            not_sale = int(item / SALE_VALUE)
            not_discount.append(not_sale)
        else:
            not_discount.remove(item)

    return sale_prices


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python codys_jams.py <input_file> <output_file>'
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
        solution = solve_prices(problem)
        line = 'Case #' + str(index + 1) + ': ' + ' '.join(str(x) for x in solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
