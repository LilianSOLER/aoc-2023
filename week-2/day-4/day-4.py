from utils import read_file, main


def how_worth_it_is_card(card):
    card = card.strip().split(" ")
    print(card)

    id = 0
    selected_numbers = []
    winning_numbers = []
    is_winning = False
    is_searching_for_id = True

    for x in card:
        if is_searching_for_id:
            if ":" in x:
                id = int(x[:-1])
                is_searching_for_id = False
                is_winning = True
        elif is_winning:
            if x == "|":
                is_winning = False
            elif x.isnumeric():
                winning_numbers.append(int(x))
        else:
            if x.isnumeric():
                selected_numbers.append(int(x))

    res = 0
    for x in selected_numbers:
        if x in winning_numbers:
            res += 1

    if res == 0:
        return 0
    else:
        return 2 ** (res - 1)


def test():
    file_paths = ["data/example.txt", "data/day-4.txt"]
    res = [13, 0]
    for file_path, result in zip(file_paths, res):
        content = read_file(file_path)
        if sum([how_worth_it_is_card(card) for card in content]) == result:
            print("Test failed for file: ", file_path)
            print("Expected: ", result)
            print("Got: ", sum([how_worth_it_is_card(card) for card in file_path]))


if __name__ == "__main__":
    file_path = "data/day-4.txt"
    # file_path = "data/example.txt"
    main(file_path, how_worth_it_is_card, how_worth_it_is_card)
    # test()
