#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2008 - Qualification round
#
# Problem B - Train Timetable
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
        # Processing the existing train schedules
        turnaround = int(all_file[n_line].strip())
        n_line += 1

        n_trains = [int(x) for x in all_file[n_line].strip().split(' ')]

        trains_a = []
        trains_b = []

        for i in xrange(n_line + 1, n_line + n_trains[0] + 1):
            trains_a.append(all_file[i].strip().split(' '))

        n_line += n_trains[0]

        for i in xrange(n_line + 1, n_line + n_trains[1] + 1):
            trains_b.append(all_file[i].strip().split(' '))

        n_line += (n_trains[1] + 1)

        problem_list.append([turnaround, trains_a, trains_b])

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def time_to_minutes(text_time):
    minute_conversion = [60,1]

    return sum([a*b for a,b in zip(minute_conversion, map(int,text_time.split(':')))])


def solve_trains(trains_configuration):
    turnaround = trains_configuration[0]
    trains_a  = trains_configuration[1]
    trains_b  = trains_configuration[2]

    # Add the trains that start from a
    all_trains = [[time_to_minutes(train[0]), time_to_minutes(train[1]), 1] for train in trains_a]
    for train in trains_b:
        all_trains.append([time_to_minutes(train[0]), time_to_minutes(train[1]), -1])
    all_trains.sort()

    n_trains_a = 0
    n_trains_b = 0
    available_a = []
    available_b = []

    for train in all_trains:
        available = False

        if train[2] == 1:
            # This train starts from a
            for train_available in available_a:
                if train[0] >= train_available:
                    available_a.remove(train_available)
                    available = True
                    break

            if not available:
                n_trains_a += 1

            available_b.append(train[1] + turnaround)
        else:
            # This train starts from b
            for train_available in available_b:
                if train[0] >= train_available:
                    available_b.remove(train_available)
                    available = True
                    break

            if not available:
                n_trains_b += 1

            available_a.append(train[1] + turnaround)

    return n_trains_a, n_trains_b


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python train_timetable.py <input_file> <output_file>'
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
        solution = solve_trains(problem)
        line = 'Case #' + str(index + 1) + ': ' + str(solution[0]) + ' ' + str(solution[1])
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
