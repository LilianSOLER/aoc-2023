from typing import List


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def main(file_path: str, func1, func2, do_sum=True) -> None:
    content: List[str] = read_file(file_path)

    def process_lines(c, f):
        return sum([f(line) for line in c])

    print(f"Part 1: {process_lines(content, func1) if do_sum else func1(content)}")
    print(f"Part 2: {process_lines(content, func2) if do_sum else func2(content)}")


def find_all(s, word):
    indexes = []
    index = s.find(word)
    while index != -1:
        indexes.append(index)
        index = s.find(word, index + 1)

    return indexes
