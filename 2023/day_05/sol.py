import os


def read_data(file_name) -> list[str]:
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    parent_dir_path = os.path.dirname(current_dir_path)
    file_path = os.path.join(parent_dir_path, "data", file_name)

    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content.split("\n")


def parse_data(data) -> dict:
    """This function will parse the data and return it as a map.

    Example, given
    input = [
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        ...
    ]

    return {
        "seeds": [79, 14, 55, 13],
        "seed": {
            50: [52, 48],
            98: [50, 2],
            "dest": "soil"
        },
        "soil": {
            15: [0, 37],
            52: [37, 2],
            0: [39, 15],
            "dest": "fertilizer"
        },
        ...
    }

    Args:
        data (list[str]): data

    Returns:
        dict: map
    """
    map_dict = {}
    # Handle seeds first
    seeds = data[0].split()[1:]
    map_dict.update({"seeds": seeds})

    # Handle the reset
    section = None
    section_dict = {}
    for line in data[1:]:
        # Handle sections
        if line == "":
            # Sort the section
            if section is not None:
                # Sort
                section_dict = {k: section_dict[k] for k in sorted(section_dict)}

                section_src = section[0]
                section_dest = section[2]

                # Add to map
                section_dict.update({"dest": section_dest})
                map_dict[section_src] = section_dict

            section = None
        elif section is None:
            # Grab keyword
            split_line = line.split()
            if split_line[1] == "map:":
                section = split_line[0].split("-")
                # Create dict for section
                section_dict = {}
        # Handle the map
        else:
            split_line = line.split()
            section_dict.update(
                {int(split_line[1]): [int(split_line[0]), int(split_line[2])]}
            )

    # Handle last section if not added
    if section is not None:
        # Sort
        section_dict = {k: section_dict[k] for k in sorted(section_dict)}

        section_src = section[0]
        section_dest = section[2]

        # Add to map
        section_dict.update({"dest": section_dest})
        map_dict[section_src] = section_dict
    return map_dict


def map_lookup(source_cat, number, map_dict) -> tuple[int, str]:
    """Will do a lookup in the dict and return the destination number
    as well as the destination category.

    Args:
        source_cat (str): source category
        number (int): number to lookup

    Returns:
        tuple[int, str]: dest number, dest category
    """
    mapped_number = number
    for key, value in map_dict[source_cat].items():
        # ignore dest or other non digits
        if not isinstance(key, int):
            continue

        # Break if its not in map
        if number < key:
            break

        # Check if its within the range, meaning key + range
        if number < (key + value[1]):
            mapped_number = number - key + value[0]
    return int(mapped_number), map_dict[source_cat].get("dest", None)


def inverse_map_lookup(dest_cat, number, map_dict) -> tuple[int, str]:
    """Inverse the lookup in the dict and return the original number
    as well as the source category.

    Args:
        dest_cat (str): destination category
        number (int): number to lookup

    Returns:
        tuple[int, str]: original number, source category
    """
    for cat, mappings in map_dict.items():
        if isinstance(mappings, dict) and mappings.get("dest") == dest_cat:
            for key, value in mappings.items():
                if not isinstance(key, int):
                    continue

                mapped_start, range_length = value
                mapped_end = mapped_start + range_length

                if mapped_start <= number < mapped_end:
                    original_number = key + (number - mapped_start)
                    return original_number, cat

    return None, None


def part_one(data):
    map_dict = parse_data(data)
    # print(map_lookup("seed", 79, map_dict))

    # Loop over seeds, get location value
    seed_map = {}
    for seed in map_dict["seeds"]:
        dest = "seed"
        location_nr = int(seed)
        while dest != "location":
            location_nr, dest = map_lookup(dest, location_nr, map_dict)
        seed_map.update({seed: location_nr})

    # Sort on values
    seed_map = sorted(seed_map.items(), key=lambda kv: kv[1])
    return seed_map[0][1]


def part_two(data):
    map_dict = parse_data(data)


if __name__ == "__main__":
    data = read_data("day5.txt")
    # print(part_one(data))
    # print(part_two(data))

    print(
        part_two(
            """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split(
                "\n"
            )
        )
    )
