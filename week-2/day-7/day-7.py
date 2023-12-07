from utils import main, read_file


def type_of_hands(hand):
    occurrences = {value: hand.count(value[0]) for value in hand}
    match len(occurrences):
        case 1:
            return "five-of-a-kind"
        case 2:
            if 4 in occurrences.values():
                return "four-of-a-kind"
            elif 3 in occurrences.values():
                return "full-house"
        case 3:
            if 3 in occurrences.values():
                return "three-of-a-kind"
            elif 2 in occurrences.values():
                return "two-pairs"
        case 4:
            return "one-pair"
        case _:
            return "high-card"


def sort_hands(hands):
    return sorted((hand.update({"rank": index + 1}) or hand for index, hand in enumerate(sorted(hands, key=lambda h: (
        "high-card one-pair two-pairs three-of-a-kind full-house four-of-a-kind five-of-a-kind".split(" ").index(
            h["type"]), *["23456789TJQKA".index(c[0]) for c in h["cards"]])))), key=lambda x: x["rank"])


def total_winning(content):
    return sum([hand["bid"] * hand["rank"] for hand in sort_hands([
        {"cards": line[0], "bid": int(line[1]), "type": type_of_hands(line[0]), "rank": -1}
        for line in (line.strip().split(" ") for line in content if line.strip())
    ])])


def test():
    return print(
        f"Test Passed for file: {'data/example.txt'}\nExpected: {6440}, Actual: {total_winning(read_file('data/example.txt'))}") or True


def nothing(content):
    pass


if __name__ == "__main__":
    if test():
        main("data/day-7.txt", total_winning, nothing, do_sum=False)
