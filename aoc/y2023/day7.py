""" Day 7 Solutions """

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import permutations, product

import numpy as np

from aoc.y2023.utils import load_data


def ints(x):
    return list(map(int, x))


from collections import Counter


def sort_by_frequency_and_value(lst):
    count = Counter(lst)
    return sorted(lst, key=lambda x: (-count[x], -x))


card_vals = list(reversed("AKQJT98765432"))
card_vals_p2 = list(reversed("AKQT98765432J"))
card_map = {card: idx for idx, card in enumerate(card_vals)}
card_map_p2 = {card: idx for idx, card in enumerate(card_vals_p2)}
n_cards = len(card_map)
hand_types = {
    6: lambda x: x.count(x[0]) == 5,
    5: lambda x: x.count(x[0]) == 4,
    4: lambda x: x.count(x[0]) == 3 and x.count(x[3]) == 2,
    3: lambda x: x.count(x[0]) == 3,
    2: lambda x: x.count(x[0]) == 2 and x.count(x[3]) == 2,
    1: lambda x: x.count(x[0]) == 2,
    0: lambda x: True,
}
hand_list = list(hand_types.keys())


def rank_hand(hand):
    """rank a hand"""
    for hand_type, func in hand_types.items():
        if func(hand):
            return hand_type


def rank_hand_p2(hand):
    """rank a hand"""
    if hand == [0, 0, 0, 0, 0]:
        return 6, hand
    c = Counter(hand)
    val, ct = c.most_common()[0]
    if val == 0:
        val, ct = c.most_common()[1]
    original_hand = hand
    hand = [val if card == 0 else card for card in hand]
    hand = sort_by_frequency_and_value(hand)
    for hand_type, func in hand_types.items():
        if func(hand):
            return hand_type, original_hand


def solve(d):
    """actual solution with puzzle input"""
    result_1, result_2 = 0, 0

    print("INPUT DATA:")
    print(d)
    hands = []
    hands2 = []
    for row in d:
        hand, bid = row.split(" ")
        print(hand)
        hand2 = [card_map_p2[card] for card in hand]
        hand = [card_map[card] for card in hand]
        bid = int(bid)
        rank = rank_hand(sort_by_frequency_and_value(hand))
        rank2, hand2 = rank_hand_p2(hand2)
        hands.append((rank, *hand, bid))
        hands2.append((rank2, *hand2, bid))
    hands = sorted(hands)
    for idx, (_, *hand, bid) in enumerate(hands, start=1):
        result_1 += idx * bid

    hands2 = sorted(hands2)
    for idx, (_, *hand, bid) in enumerate(hands2, start=1):
        print("".join([card_vals_p2[card] for card in hand]), bid, idx)
        result_2 += idx * bid

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
        d = load_data("test_day7.txt")
        test_answer_1 = 6440
        test_answer_2 = 5905
        test_solution_1, test_solution_2 = solve(d)
        assert test_solution_1 == test_answer_1, f"TEST #1 FAILED: TRUTH={test_answer_1}, YOURS={test_solution_1}"
        assert test_solution_2 == test_answer_2, f"TEST #2 FAILED: TRUTH={test_answer_2}, YOURS={test_solution_2}"
        print("**** TESTS PASSED ****")
        print("Test Answer 1: ", test_answer_1)
        print("My Test Answer 1: ", test_solution_1)
        print("Test Answer 2: ", test_answer_2)
        print("My Test Answer 2: ", test_solution_2)
    print("**** REAL DATA ****")
    day = int("day7".replace("day", ""))
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
