#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2008 - Qualification round
#
# Problem A - Saving the Universe
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file[0].strip())

    n_line = 1
    while n_line < len(all_file):
        # Processing the existing search engines
        n_engines = int(all_file[n_line].strip())
        engines = []

        for i in xrange(n_line + 1, n_line + n_engines + 1):
            engines.append(all_file[i].strip())

        n_line += (n_engines + 1)

        # Processing the queries
        n_queries = int(all_file[n_line].strip())
        queries = []

        for i in xrange(n_line + 1, n_line + n_queries + 1):
            queries.append(all_file[i].strip())

        n_line += (n_queries + 1)

        problem_list.append((engines, queries))

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def solve_universe(engines_queries):
    engines = engines_queries[0]
    queries = engines_queries[1]

    n_changes = 0

    unseen_engines = list(engines)

    for query in queries:
        if query in unseen_engines:
            unseen_engines.remove(query)

            if len(unseen_engines) == 0:
                n_changes += 1
                unseen_engines = list(engines)
                unseen_engines.remove(query)

    return n_changes


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python saving_universe.py <input_file> <output_file>'
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
        solution = solve_universe(problem)
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
