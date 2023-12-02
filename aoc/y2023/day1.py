""" Day 1 Solutions """

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import permutations, product

import numpy as np

from aoc.y2023.utils import load_data


def ints(x):
    return list(map(int, x))


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    print(d)
    ans = 0
    for row in d:
        print(row)
        for c in row:
            try:
                a = int(c)
                break
            except Exception:
                continue
        for c in reversed(row):
            try:
                b = int(c)
                break
            except Exception:
                continue
        ans += a*10 + b
    result_1 = ans

    num_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    ans = 0
    for row in d:
        for idx, c in enumerate(row):
            try:
                a = int(c)
                break
            except Exception:
                found = False
                for num in num_map:
                    if row[idx:].startswith(num):
                        a = num_map[num]
                        found = True
                        break
                if found:
                    break
                continue
        for idx, c in enumerate(reversed(row)):
            try:
                b = int(c)
                break
            except Exception:
                found = False
                for num in num_map:
                    if row[-idx-1:].startswith(num):
                        b = num_map[num]
                        found = True
                        break
                if found:
                    break
                continue

        ans += a*10 + b
    result_2 = ans
    return result_1, result_2


def main():
    """Main function"""
    args = ArgumentParser()
    args.add_argument("--skip", action="store_true")
    args = args.parse_args()
    # load data:
    if not args.skip:
        print("**** TEST DATA ****")
        d = load_data("test_day1.txt")
        d2 = load_data("test_day1_p2.txt")
        test_answer_1 = 142
        test_answer_2 = 281
        test_solution_1, _ = solve(d)
        _, test_solution_2 = solve(d2)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    d = load_data("day1.txt")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)


if __name__ == "__main__":
    main()
