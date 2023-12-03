from typing import List, Tuple


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def get_first_and_last_digit(s: str) -> int:
    digits = [int(char) for char in s if char.isdigit()]
    if not digits:
        raise ValueError("No digit found in the string")
    return int(str(digits[0]) + str(digits[-1]))


def find_all(s, word):
    indexes = []
    index = s.find(word)
    while index != -1:
        indexes.append(index)
        index = s.find(word, index + 1)

    return indexes


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


def part_1(content: List[str]) -> int:
    return sum([get_first_and_last_digit(line) for line in content])


def part_2(content: List[str]) -> int:
    return sum([get_first_and_last_digit_v2(line) for line in content])


def main(file_path: str) -> None:
    content: List[str] = read_file(file_path)
    print(f"Part 1: {part_1(content)}")
    print(f"Part 2: {part_2(content)}")


if __name__ == "__main__":
    file_path = "data/day-1.txt"
    main(file_path)
