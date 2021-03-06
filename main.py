#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program randomizes 10 numbers and figures which is the largest

import random


def main():
    # this function randomizes 10 numbers and figures out which is the largest

    my_numbers = []
    largest_num = 0

    # input
    for loop_counter in range(0, 10):
        randomized_number = random.randint(1, 100)  # a number between 1-100
        my_numbers.append(randomized_number)

    print("Your numbers are: ", end="")

    for loop_counter in range(0, 10):
        print("{0} ".format(my_numbers[loop_counter]), end="")
        indicator = my_numbers[loop_counter] - largest_num

        if indicator > 0:
            largest_num = my_numbers[loop_counter]

        else:
            print("", end="")

    print("\n\nThe largest random number is {0}.".format(largest_num))


if __name__ == "__main__":
    main()
