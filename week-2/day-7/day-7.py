from utils import main, read_file


def type_of_hands_common(occurrences):
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


def count_occurrences(hand):
    return {value: hand.count(value[0]) for value in hand}


def type_of_hands(hand):
    return type_of_hands_common(count_occurrences(hand))


def type_of_hands_v2(hand):
    occurrences = count_occurrences(hand)
    if "J" in occurrences:
        j_count = occurrences.pop("J")
        if j_count:
            if j_count == 5:
                return "five-of-a-kind"
            occurrences[next(
                key for key, value in occurrences.items() if value == max(occurrences.values(), default=0))] += j_count
            return type_of_hands_common(occurrences)

    return type_of_hands_common(occurrences)


def sort_hands_common(hands, card_key="23456789TJQKA"):
    type_of_cards = card_key
    type_of_types = "high-card one-pair two-pairs three-of-a-kind full-house four-of-a-kind five-of-a-kind".split(" ")

    return sorted((hand.update({"rank": index + 1}) or hand for index, hand in enumerate(sorted(hands, key=lambda h: (
        type_of_types.index(h["type"]), *[type_of_cards.index(c[0]) for c in h["cards"]])))), key=lambda x: x["rank"])


def total_winning(content):
    return sum(hand["bid"] * hand["rank"] for hand in sort_hands_common([
        {"cards": line[0], "bid": int(line[1]), "type": type_of_hands(line[0]), "rank": -1}
        for line in (line.strip().split(" ") for line in content if line.strip())
    ]))


def total_winning_v2(content):
    return sum(hand["bid"] * hand["rank"] for hand in sort_hands_common([
        {"cards": line[0], "bid": int(line[1]), "type": type_of_hands_v2(line[0]), "rank": -1}
        for line in (line.strip().split(" ") for line in content if line.strip())
    ], card_key="J23456789TQKA"))


def test():
    expected_result = 5905
    actual_result = total_winning_v2(read_file('data/example.txt'))
    print(f"Test Passed for file: {'data/example.txt'}\nExpected: {expected_result}, Actual: {actual_result}")
    return True


if __name__ == "__main__":
    if test():
        main("data/day-7.txt", total_winning, total_winning_v2, do_sum=False)
