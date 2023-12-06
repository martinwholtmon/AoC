import os


def read_data(file_name) -> list[str]:
    current_dir_path = os.path.dirname(os.path.abspath(__file__))
    parent_dir_path = os.path.dirname(current_dir_path)
    file_path = os.path.join(parent_dir_path, "data", file_name)

    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content.split("\n")


def adjecent_symbols(data, row_idx, start_idx, stop_idx):
    """This function will take the row, start and end index
    and check if there are any adjecent symbols (meaning non digits).


    Args:
        data (list[str]): input data
        row_idx (int): row index we are at
        start_idx (int): the start index of a number
        stop_idx (int): end index of a number
    """
    # Define the ranges (witin bounds)
    row_range = range(max(0, row_idx - 1), min(row_idx + 2, len(data)))
    col_range = range(max(0, start_idx - 1), min(stop_idx + 2, len(data[row_idx])))

    # Check each char within the range
    # if not digit and not dot (.), then its a symbol
    for row_idx in row_range:
        for col_idx in col_range:
            char = data[row_idx][col_idx]
            if not char.isdigit() and char != ".":
                return True
    return False


def part_one(data):
    """sum numbers that are not adjacent to a symbol.
    To do this, we need to keep track of current, past and next line.

    If we find a number, get the start and end index (range of the number),
    add 1 to stand and end of the range. Check if there are any
    symbols within that range on current, past and next line.

    The symbols are defined as everything that is not a number or a dot (.),
    e.g. "$", "@", "/"...

    Args:
        data (list[str]): input
    """
    total_sum = 0
    for row_idx, row in enumerate(data):
        # Iterate over the characters, if number check if adjacent
        start_idx = None
        for col_idx, char in enumerate(row):
            if char.isdigit():
                if start_idx is None:
                    start_idx = col_idx  # set start index
            elif start_idx is not None:  # Reached end of number
                if adjecent_symbols(data, row_idx, start_idx, col_idx - 1):
                    total_sum += int(row[start_idx:col_idx])
                start_idx = None  # Reset
        # Handle if number is at end of row
        if start_idx is not None and adjecent_symbols(
            data, row_idx, start_idx, len(row) - 1
        ):
            total_sum += int(row[start_idx:])
    return total_sum


def find_whole_number(data, row_idx, col_idx) -> tuple[int, int]:
    """Given a position of a number, traverse both ways to find the complete number.

    Args:
        data (list[str]): input
        row_idx (int): row where the number is
        col_idx (int): col where the registerd digit is located

    Returns:
        tuple[int, int]: The complete number, end index of the number
    """
    # Traverse left
    left_idx = col_idx - 1
    while left_idx >= 0 and data[row_idx][left_idx].isdigit():
        left_idx -= 1

    # Traverse right
    right_idx = col_idx + 1
    while right_idx < len(data[row_idx]) and data[row_idx][right_idx].isdigit():
        right_idx += 1

    # Return the number and the end index
    return int(data[row_idx][left_idx + 1 : right_idx]), right_idx - 1


def adjecent_numbers(data, p_row_idx, p_col_idx) -> int:
    """Check if the symbol has two adjecent part numbers

    Args:
        data (list[str]): input data
        row_idx (int): current row
        pos_idx (int): position of symbol

    Returns:
        int: if two numbers, multiply of those or 0.
    """
    # Define the ranges (witin bounds)
    row_range = range(max(0, p_row_idx - 1), min(p_row_idx + 2, len(data)))
    col_range = range(max(0, p_col_idx - 1), min(p_col_idx + 2, len(data[p_row_idx])))

    # Check for adjecent part numbers
    part_numbers = []
    for row_idx in row_range:
        col_idx = col_range.start
        while col_idx in col_range:
            if col_idx != p_col_idx and data[row_idx][col_idx].isdigit():
                number, end_idx = find_whole_number(data, row_idx, col_idx)
                part_numbers.append(number)

                # Contine where number stopped
                col_idx = max(col_idx, end_idx)
            col_idx += 1  # Increment
    # Retrun
    if len(part_numbers) == 2:
        return part_numbers[0] * part_numbers[1]
    return 0


def part_two(data):
    """Identify the symbol *, check if it has two adjecent numbers.
    If it does, multiply those numbers and add it to the total sum

    Args:
        data (list[str]): input data

    Returns:
        int: sum of all gear ratios
    """
    total_sum = 0
    for row_idx, row in enumerate(data):
        for col_idx, char in enumerate(row):
            if char == "*":
                total_sum += adjecent_numbers(data, row_idx, col_idx)
    return total_sum


if __name__ == "__main__":
    data = read_data("day3.txt")
    print(part_one(data))
    print(part_two(data))

    print(
        part_two(
            """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split(
                "\n"
            )
        )
    )
