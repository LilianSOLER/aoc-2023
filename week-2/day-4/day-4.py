from utils import read_file, main


def how_worth_it_is_card_aux(card):
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


def how_worth_it_is_card(content):
    return sum([how_worth_it_is_card_aux(card) for card in content])


def how_many_scratchwards_aux(card):
    card = card.strip().split(" ")

    card_id = 0
    selected_numbers = []
    winning_numbers = []
    is_winning = False
    is_searching_for_id = True

    for x in card:
        if is_searching_for_id:
            if ":" in x:
                # print(x)
                card_id = int(x[:-1])
                # print("card_id", str(card_id))
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
    for x in range(1, res + 1):
        if card_id + x in SCRATCHWARD_ARRAY:
            print("Game", card_id, "winning: " + str(res), "scratchwards so game", card_id + x,
                  "will get " + str(SCRATCHWARD_ARRAY[card_id + x] + SCRATCHWARD_ARRAY[card_id]))
            SCRATCHWARD_ARRAY[card_id + x] += SCRATCHWARD_ARRAY[card_id]
        else:
            print("Game", card_id, "winning: " + str(res), "scratchwards so game", card_id,
                  "will get " + str(SCRATCHWARD_ARRAY[card_id] + res - x + 1))
            SCRATCHWARD_ARRAY[card_id] += res - x + 1
            break


def how_many_scratchwards(content):
    c = 0
    for card in content:
        how_many_scratchwards_aux(card)
    # print(SCRATCHWARD_ARRAY)
    for x in SCRATCHWARD_ARRAY:
        print(x, SCRATCHWARD_ARRAY[x])
        c += SCRATCHWARD_ARRAY[x]
    print(c)
    return c


def test():
    file_paths = ["data/example.txt"]
    res = [30, 0]
    for file_path, result in zip(file_paths, res):
        content = read_file(file_path)
        if how_many_scratchwards(content) == result:
            print("Test failed for file: ", file_path)
            print("Expected: ", result)
            print("Got: ", sum([how_worth_it_is_card(card) for card in file_path]))


SCRATCHWARD = 0
SCRATCHWARD_ARRAY: dict[int, int] = {}
if __name__ == "__main__":
    file_path = "data/day-4.txt"
    # file_path = "data/example.txt"
    SCRATCHWARD_ARRAY = {i: 1 for i in range(1, len(read_file(file_path)) + 1)}
    main(file_path, how_worth_it_is_card, how_many_scratchwards, do_sum=False)
    # test()
