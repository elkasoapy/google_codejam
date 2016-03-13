#!/usr/bin/env python

################################################################################
#
# Google Code Jam to I/O for Women 2016
#
# Problem D - Password Security
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os
import random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NO_SECURE_ALPHABET = 'IMPOSSIBLE'
MAX_TRIES = 100000


def read_problems_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file[0].strip())

    for i in xrange(1, len(all_file), 2):
        n_passwords = int(all_file[i].strip())
        passwords = all_file[i + 1].strip().split(' ')

        if n_passwords != len(passwords):
            print 'Wrong formatted file!'
            sys.exit()

        problem_list.append(passwords)

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def solve_password_security(passwords):
    secure_alphabet = ALPHABET
    insecure = True
    n_tries = 0

    while insecure and n_tries < MAX_TRIES:
        insecure = False

        for password in passwords:
            if len(password) == 1:
                return NO_SECURE_ALPHABET
            else:
                if password in secure_alphabet:
                    secure_alphabet = ''.join(random.sample(secure_alphabet, len(secure_alphabet)))
                    insecure = True
                    n_tries += 1
                    break

    if n_tries < MAX_TRIES:
        return secure_alphabet
    else:
        return NO_SECURE_ALPHABET


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python password_security.py <input_file> <output_file>'
        sys.exit()

    problems_file = sys.argv[1]
    if not os.path.isfile(problems_file):
        print 'Incorrect first parameter given to this script: ' + sys.argv[1]
        print 'The given file does not exist'
        sys.exit()

    # Read the input data
    problems_values = read_problems_file(problems_file)

    # Process the problems
    output = []
    for index, problem in enumerate(problems_values):
        solution = solve_password_security(problem)
        line = 'Case #' + str(index + 1) + ': ' + solution
        output.append(line)

    # Output to file
    outputFile = open(sys.argv[2], 'w')
    outputFile.write('\n'.join(output))
    outputFile.close()
