import math
import os


def read_data(file_name) -> list[str]:
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    parent_dir_path = os.path.dirname(current_dir_path)
    file_path = os.path.join(parent_dir_path, "data", file_name)

    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content.split("\n")


def part_one(data):
    # Parse
    time = []
    distance = []
    for line in data:
        value_type, values = line.split(":")
        values = values.split()
        if value_type == "Time":
            time.extend(values)
        elif value_type == "Distance":
            distance.extend(values)
        else:
            raise ValueError()

    # Calculate
    different_wins = 1
    for game, game_time in enumerate(time):
        wins = 0
        for holding_time in range(1, int(game_time)):
            remaining_time = int(game_time) - holding_time
            starting_speed = holding_time * 1  # speed increase
            game_distance = starting_speed * remaining_time

            if game_distance > int(distance[game]):
                wins += 1

        if wins > 0:
            different_wins *= wins
    return different_wins if different_wins > 1 else 0


def part_two(data):
    # Parse
    time = 0
    distance = 0
    for line in data:
        value_type, values = line.split(":")
        values = int(values.replace(" ", ""))
        if value_type == "Time":
            time = values
        elif value_type == "Distance":
            distance = values
        else:
            raise ValueError()

    # Calculate
    lower_bound = math.ceil(time - math.sqrt(time * time - 4 * distance)) / 2
    upper_bound = math.ceil(time + math.sqrt(time * time - 4 * distance)) / 2

    print(lower_bound, upper_bound)

    return round(upper_bound - lower_bound) + 1


if __name__ == "__main__":
    data = read_data("day6.txt")
    print(part_one(data))
    print(part_two(data))
