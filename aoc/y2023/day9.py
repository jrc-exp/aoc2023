""" Day 0 Solutions """

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
    result_1 = 0
    for row in d:
        nums = ints(row.split(" "))
        rows = [nums]
        while True:
            diffs = np.diff(rows[-1])
            rows.append(list(diffs))
            if np.all(diffs == 0):
                break
        rows[-1].append(0)
        for idx, row in enumerate(reversed(rows[:-1]), start=1):
            goal = rows[-idx][-1]
            row.append(row[-1] + goal)

        # part 2 the short way!
        val = 0
        for idx, row in enumerate(reversed(rows[:-1]), start=1):
            val = row[0] - val

        result_1 += rows[0][-1]
        result_2 += val

    return result_1, result_2


def main():
    """Main function"""
    args = ArgumentParser()
    args.add_argument("--skip", action="store_true")
    args.add_argument("--submit", action="store_true")
    args = args.parse_args()
    # load data:
    if not args.skip:
        print("**** TEST DATA ****")
        d = load_data("test_day9.txt")
        test_answer_1 = 114
        test_answer_2 = 2
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)

    print("**** REAL DATA ****")
    day = 9
    # d = load_data(f"day{day}.txt")
    import os
    from aocd import submit, get_data

    d = get_data(day=day, year=2023).split("\n")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)

    if args.submit or not os.path.exists(f"/tmp/lock_day{day}_a"):
        with open(f"/tmp/lock_day{day}_a", "w") as f:
            f.write("locked")
        submit(answer_1, part="a", day=day, year=2023)
    if test_answer_2 != 0 and answer_2:
        if args.submit or not os.path.exists(f"/tmp/lock_day{day}_b"):
            with open(f"/tmp/lock_day{day}_b", "w") as f:
                f.write("locked")
            submit(answer_2, part="b", day=day, year=2023)


if __name__ == "__main__":
    main()
