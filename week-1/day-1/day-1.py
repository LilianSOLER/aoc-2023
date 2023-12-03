from typing import List, Tuple

from utils import find_all, main


def get_first_and_last_digit(s: str) -> int:
    digits = [int(char) for char in s if char.isdigit()]
    if not digits:
        raise ValueError("No digit found in the string")
    return int(str(digits[0]) + str(digits[-1]))


def get_first_and_last_digit_v2(s: str) -> int:
    number_mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    all_indexes: List[Tuple[int, int]] = []

    for index, word in enumerate(number_mapping):
        indexes = find_all(s, word)
        if indexes:
            all_indexes.extend([(i, index + 1) for i in indexes])

    if all_indexes:
        s_array = list(s)
        all_indexes.sort(key=lambda x: x[0])
        s_array[all_indexes[0][0]] = str(all_indexes[0][1])
        s_array[all_indexes[-1][0]] = str(all_indexes[-1][1])
        s = "".join(s_array)

    return get_first_and_last_digit(s)


if __name__ == "__main__":
    file_path = "data/day-1.txt"
    main(file_path, get_first_and_last_digit, get_first_and_last_digit_v2)
