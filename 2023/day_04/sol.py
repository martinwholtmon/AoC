import os
import numpy as np
from collections import deque


def read_data(file_name) -> list[str]:
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    parent_dir_path = os.path.dirname(current_dir_path)
    file_path = os.path.join(parent_dir_path, "data", file_name)

    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content.split("\n")


def part_one(data):
    points = 0
    for line in data:
        game = line.split("|")
        winning_numbers = game[0].split(":")[1].split()
        number = game[1].split()

        # Count duplicate (2^(n-1))
        duplicates = len(np.intersect1d(winning_numbers, number))
        if duplicates > 0:
            points += 2 ** (duplicates - 1)
    return points


def part_two(data):
    scratchcards = 0
    factor_dict = {}
    for line in data:
        game = line.split("|")
        card_nr = int(game[0].split(":")[0].split()[1])
        winning_numbers = game[0].split(":")[1].split()
        number = game[1].split()
        wins = len(np.intersect1d(winning_numbers, number))

        # Process
        for n in range(factor_dict.get(card_nr, 1)):
            # Add to dict
            for n in range(card_nr + 1, card_nr + wins + 1):
                factor_dict[n] = factor_dict.get(n, 1) + 1
            scratchcards += 1
    return scratchcards


if __name__ == "__main__":
    data = read_data("day4.txt")
    print(part_one(data))
    print(part_two(data))
