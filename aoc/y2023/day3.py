""" Day 0 Solutions """

from math import prod
import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import permutations, product
from string import digits
import re

import numpy as np

from aoc.y2023.utils import load_data, NEIGHBOR8


def ints(x):
    return list(map(int, x))


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    print(d)
    matches = []
    gears = defaultdict(list)
    for idy, row in enumerate(d):
        for match in re.finditer(r"\d+", row):
            start, end = match.span()
            number = match.group()
            done = False
            for idx in range(start, end):
                if done:
                    break
                for x, y in NEIGHBOR8:
                    if idx + x < 0 or idx + x >= len(row):
                        continue
                    if idy + y < 0 or idy + y >= len(d):
                        continue
                    if d[idy + y][idx + x] not in digits + ".":
                        matches.append(int(number))
                        print(number)
                        done = True
                        break
            added = set()
            for idx in range(start, end):
                for x, y in NEIGHBOR8:
                    if idx + x < 0 or idx + x >= len(row):
                        continue
                    if idy + y < 0 or idy + y >= len(d):
                        continue
                    if d[idy + y][idx + x] == "*":
                        if (idy + y, idx + x) in added:
                            continue
                        gears[(idy + y, idx + x)].append(int(number))
                        added.add((idy + y, idx + x))

    print(gears)

    result_1 = sum(matches)
    result_2 = sum(prod(v) for k, v in gears.items() if len(v) == 2)

    return result_1, result_2


def main():
    """Main function"""
    args = ArgumentParser()
    args.add_argument("--skip", action="store_true")
    args = args.parse_args()
    # load data:
    if not args.skip:
        print("**** TEST DATA ****")
        d = load_data("test_day3.txt")
        test_answer_1 = 4361
        test_answer_2 = 467835
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    d = load_data("day3.txt")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)


if __name__ == "__main__":
    main()
