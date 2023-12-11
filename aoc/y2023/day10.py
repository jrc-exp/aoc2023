""" Day 10 Solutions """

from operator import ne
import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import permutations, product

import numpy as np

from aoc.y2023.utils import load_data, NEIGHBOR4, NEIGHBOR8

N4 = NEIGHBOR4
N, S, E, W = ((-1, 0), (1, 0), (0, 1), (0, -1))


def ints(x):
    return list(map(int, x))


pipe_map = {
    "|": (N, S),
    "-": (E, W),
    "L": (N, E),
    "J": (N, W),
    "7": (S, W),
    "F": (S, E),
    "S": NEIGHBOR8,
}


def move(loc, dir):
    return loc[0] + dir[0], loc[1] + dir[1]


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0
    print("INPUT DATA:")
    print(d)

    grid = dict()
    neighbors = dict()
    for idy, row in enumerate(d):
        for idx, c in enumerate(row):
            loc = (idy, idx)
            grid[loc] = float("inf")
            if c in pipe_map:
                neighbors[loc] = [move(loc, conn) for conn in pipe_map[c]]
            if c == "S":
                start = loc
                grid[start] = 0

    connections = defaultdict(set)
    for loc in neighbors:
        for neighbor in neighbors[loc]:
            if neighbor in neighbors and loc in neighbors[neighbor]:
                connections[loc].add(neighbor)
                connections[neighbor].add(loc)

    loc = start

    def print_grid(grid):
        for idy in range(len(d)):
            row = ""
            for idx in range(len(d[0])):
                row += str(grid[(idy, idx)] if grid[(idy, idx)] != float("inf") else ".")

    locs = [start]
    while locs:
        next_locs = set()
        for loc in locs:
            for c in connections[loc]:
                if grid[c] > grid[loc] + 1:
                    grid[c] = grid[loc] + 1
                    if grid[loc] + 1 > result_1:
                        result_1 = grid[loc] + 1
                    next_locs.add(c)
        locs = next_locs

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
        d = load_data("test_day10.txt")
        test_answer_1 = 8
        test_answer_2 = 0
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    day = int("day10".replace("day", ""))
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
