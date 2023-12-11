""" Day 8 Solutions """

from math import prod
import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import cycle, permutations, product

import numpy as np

from aoc.y2023.utils import load_data


def ints(x):
    return list(map(int, x))


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    print(d)
    directions = d[0]
    directions = cycle(directions)
    maps = {}
    L = 0
    R = 1
    dirs = {
        "L": L,
        "R": R,
    }
    for row in d[2:]:
        row = row.replace(" ", "")
        node, other = row.split("=")
        left, right = other.split(",")
        left = left[1:]
        right = right[:-1]
        maps[node] = (left, right)

    start = "AAA"
    goal = "ZZZ"
    node = start
    ct = 0
    if "AAA" in maps:
        while node != goal:
            ct += 1
            dir = next(directions)
            node = maps[node][dirs[dir]]
        result_1 = ct

    # part 2
    starts = [key for key in maps if key[-1].lower() == "a"]
    stops = [key for key in maps if key[-1].lower() == "z"]
    for start in starts:
        print(start)
    for stop in stops:
        print(stop)
    directions = d[0]
    directions = cycle(directions)
    cts = []
    for start in starts:
        ct = 0
        while not start.endswith("Z"):
            dir = next(directions)
            start = maps[start][dirs[dir]]
            ct += 1
        cts.append(ct)

    import math

    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    result_2 = cts[0]
    for ct in cts[1:]:
        result_2 = lcm(result_2, ct)

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
        d = load_data("test_day8.txt")
        d2 = load_data("test_day8_p2.txt")
        test_answer_1 = 2
        test_answer_2 = 6
        test_solution_1, test_solution_2 = solve(d)
        _, test_solution_2 = solve(d2)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    day = int("day8".replace("day", ""))
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
