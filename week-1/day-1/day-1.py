from typing import List


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def get_first_and_last_digit(s: str) -> int:
    digits = [int(char) for char in s if char.isdigit()]
    if not digits:
        raise ValueError("No digit found in the string")
    return int(str(digits[0]) + str(digits[-1]))


def part_1(content: List[str]) -> int:
    return sum([get_first_and_last_digit(line) for line in content])


def main(file_path: str) -> None:
    content: List[str] = read_file(file_path)
    print(f"Part 1: {part_1(content)}")


if __name__ == "__main__":
    file_path = "data/day-1.txt"
    main(file_path)
