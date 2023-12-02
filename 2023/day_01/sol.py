from helper import read_input


def letters_to_numbers(line, reverse):
    letter_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    if reverse:
        line = line[::-1]
        letter_dict = {word[::-1]: number for word, number in letter_dict.items()}

    ret_line = ""
    for c in line:
        ret_line += c
        # Check after digit
        for word, number in letter_dict.items():
            ret_line = ret_line.replace(word, number)
    return ret_line


def get_numbers(line):
    return [str(char) for char in line if char.isdigit()]


def get_numbers_converted(line, reverse=False):
    # convert letters to numbers
    return get_numbers(letters_to_numbers(line, reverse))


def part_one(text):
    # Split the input text into lines
    lines = text.lower().split("\n")

    total_sum = 0
    for line in lines:
        number = get_numbers(line)
        first = number[0]
        second = number[-1]
        total_sum += int(first + second)
    return total_sum


def part_two(text):
    # Split the input text into lines
    lines = text.lower().split("\n")

    total_sum = 0
    for line in lines:
        first = get_numbers_converted(line, False)[0]
        second = get_numbers_converted(line, True)[0]
        total_sum += int(first + second)
    return total_sum


if __name__ == "__main__":
    input = read_input("day1.txt")
    print(part_one(input))
    print(part_two(input))
