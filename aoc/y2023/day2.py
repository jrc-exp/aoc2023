""" Day 2 Solutions """

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
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    result_1 = 0
    result_2 = 0
    for row in d:
        print(row)
        too_many = False
        game, rest = row.split(":")
        id = int(game.split(" ")[1])
        games = rest.split(";")
        print(id)
        most = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        for game in games:
            rounds = game.split(",")
            for round in rounds:
                num, color = round.strip(" ").split(" ")
                num = int(num)
                if num > most[color]:
                    most[color] = num
                if num > max_cubes[color]:
                    too_many = True
        from math import prod

        result_2 += prod(most.values())

        if not too_many:
            result_1 += id

    return result_1, result_2


def main():
    """Main function"""
    args = ArgumentParser()
    args.add_argument("--skip", action="store_true")
    args = args.parse_args()
    # load data:
    if not args.skip:
        print("**** TEST DATA ****")
        d = load_data("test_day2.txt")
        test_answer_1 = 8
        test_answer_2 = 2286
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    d = load_data("day2.txt")
    answer_1, answer_2 = solve(d)
    print("Answer 1:", answer_1)
    print("Answer 2:", answer_2)


if __name__ == "__main__":
    main()
