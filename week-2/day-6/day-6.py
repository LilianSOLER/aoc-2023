from functools import reduce

from utils import main, read_file


def number_of_way_to_win(content):
    return reduce(lambda x, y: x * y, (len([x for x in range(row[0]) if x * (row[0] - x) > row[1]]) for row in
                                       list(zip([int(x) for x in
                                                 [x for x in content[0].strip().split(" ")[1:] if x != ""]],
                                                [int(x) for x in
                                                 [x for x in content[1].strip().split(" ")[1:] if x != ""]]))))


def test():
    file_paths = ["data/example.txt"]
    res = [288]
    for file_path, result in zip(file_paths, res):
        content = read_file(file_path)
        if number_of_way_to_win(content) != result:
            print("Test failed for file: " + file_path)
            print("Expected: " + str(result)
                  + " Actual: " + str(number_of_way_to_win(content)))
            return


if __name__ == "__main__":
    file_path = "data/day-6-p2.txt"
    # file_path = "data/example.txt"
    test()
    main(file_path, number_of_way_to_win, number_of_way_to_win, do_sum=False)
