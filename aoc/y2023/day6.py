""" Day 6 Solutions """

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import permutations, product
from unittest import result

import numpy as np

from aoc.y2023.utils import load_data


def ints(x):
    return list(map(int, x))


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    print(d)
    # regex for all integers in a text row:
    import re

    def extract_integers(text):
        integers = re.findall(r"\d+", text)
        return list(map(int, integers))

    times = extract_integers(d[0])
    dists = extract_integers(d[1])
    print(times, dists)
    result_1 = 1
    for t, d in zip(times, dists):
        ct = 0
        for w in range(t):
            dist = w * (t - w)
            if dist > d:
                ct += 1
        result_1 *= ct

    times = int("".join(map(str, times)))
    dists = int("".join(map(str, dists)))
    ct = 0
    from tqdm.auto import tqdm

    for w in tqdm(range(times)):
        dist = w * (times - w)
        if dist > dists:
            ct += 1
    result_2 = ct

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
        d = load_data("test_day6.txt")
        test_answer_1 = 288
        test_answer_2 = 71503
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    day = int("day6".replace("day", ""))
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
