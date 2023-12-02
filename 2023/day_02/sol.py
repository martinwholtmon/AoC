import os
from functools import reduce


def read_data(file_name) -> list[str]:
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    parent_dir_path = os.path.dirname(current_dir_path)
    file_path = os.path.join(parent_dir_path, "data", file_name)

    with open(file_path, "r") as file:
        file_content = file.readlines()  # ty Simpert for that one
    return file_content


def parse_game(game) -> dict:
    # split game nr and game parts
    parts = game.split(":")

    game_nr = int(parts[0].split()[1])
    game_sets = parts[1].split(";")

    # count
    result = {"game_nr": game_nr, "games": list()}
    for game_set in game_sets:
        color_count_dict = {}
        color_counts = game_set.strip().split(",")
        for color_count in color_counts:
            count, color = color_count.split()
            color_count_dict.update({color: int(count)})
        result["games"].append(color_count_dict)
    return result


def game_possible(game_sets, limits: dict) -> bool:
    # Check the games
    for game_set in game_sets:
        for color, value in game_set.items():
            if limits.get(color) < value:
                return False
    return True


def part_one(data):
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    sum_ids = 0
    for game in data:
        game = parse_game(game)
        if game_possible(game.get("games"), limits):
            sum_ids += game.get("game_nr")
    return sum_ids


def part_two(data):
    sum = 0
    for game in data:
        game = parse_game(game)

        # get minimum colors
        minimum_colors = {}
        for game_set in game.get("games"):
            for color, value in game_set.items():
                if value > minimum_colors.get(color, 0):
                    minimum_colors[color] = value
        sum += reduce(
            lambda x, y: x * y, minimum_colors.values()
        )  # multiply numbers in list
    return sum


if __name__ == "__main__":
    data = read_data("day2.txt")
    print(part_one(data))
    print(part_two(data))
