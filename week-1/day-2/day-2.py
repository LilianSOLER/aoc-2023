from typing import List


def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def is_valid_game(game: str, condition: dict[str, int] = None) -> int:
    if condition is None:
        condition = {"red": 0, "green": 0, "blue": 0}

    game_info = game.split(":")
    game_id = int(game_info[0].split(" ")[1])

    games = game_info[1].split(";")
    for game in games:
        cubes_dict = {cube_info[1]: int(cube_info[0]) for cube in game.strip().split(",") for cube_info in
                      [cube.strip().split(" ")]}

        if not set(cubes_dict.keys()).issubset(condition.keys()):
            return 0

        if any(cubes_dict[key] > condition[key] for key in cubes_dict):
            return 0

    return game_id


def min_cond_to_win(game: str) -> int:
    condition = {"red": -1, "green": -1, "blue": -1}

    for cube_info in [cube.strip().split(" ") for game in game.split(":")[1].split(";") for cube in
                      game.strip().split(",")]:
        condition[cube_info[1]] = max(int(cube_info[0]), condition[cube_info[1]])

    return condition["red"] * condition["green"] * condition["blue"]


def part_1(content: List[str]) -> int:
    conditions = {"red": 12, "green": 13, "blue": 14}
    return sum([is_valid_game(game, conditions) if game else 0 for game in content])


def part_2(content: List[str]) -> int:
    return sum([min_cond_to_win(game) for game in content])


def main(file_path: str) -> None:
    content: List[str] = read_file(file_path)
    print(f"Part 1: {part_1(content)}")
    print(f"Part 2: {part_2(content)}")


if __name__ == "__main__":
    file_path = "data/day-2.txt"
    main(file_path)
