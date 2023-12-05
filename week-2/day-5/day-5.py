from utils import read_file, main


def array_to_maps(array):
    res = {}
    for x in array:
        min_range_translate, min_range_value, numbers_map = array.split(" ")
        min_range_translate = int(min_range_translate)
        min_range_value = int(min_range_value)
        numbers_map = int(numbers_map)
        for i in range(numbers_map):
            res[min_range_value + i] = min_range_translate + i
    return res


def array_to_maps_v2(array):
    res = []

    min_range_translate, min_range_value, numbers_map = array.split(" ")
    min_range_translate = int(min_range_translate)
    min_range_value = int(min_range_value)
    numbers_map = int(numbers_map)
    res.append([min_range_value, min_range_value + numbers_map, min_range_value - min_range_translate])
    return res


def read_content(content):
    print("Reading content")
    seeds = content[0].strip().split(" ")[1:]
    seeds = [int(x) for x in seeds]
    maps_array = []
    is_writting_map = False
    print("Extracting maps")
    for x in content[1:]:
        x = x.strip()
        if "map" in x:
            is_writting_map = True
            maps_array.append([])
            continue
        if is_writting_map:
            if x == "":
                is_writting_map = False
                continue
            else:
                maps_array[-1].append(x)

    print("Converting maps")
    maps = []
    for map_array in maps_array:
        maps.append([])
        for x in map_array:
            maps[-1].append(array_to_maps_v2(x))

    print("seeds", seeds)
    print("maps", maps)

    print("Reading content done")
    return seeds, maps


def seed_to_location(seed, maps):
    print("seed_to_location", seed, maps)
    old_name = "seeds"
    for i in range(len(maps)):
        old_seed = seed
        new_map = maps[i][1]
        map_name = maps[i][0]
        print("seed", seed, "will be map from", old_name, "to", map_name)
        old_name = map_name
        for sub_map in new_map:
            if seed in sub_map:
                print("seed", seed, "mapped to", sub_map[seed], "in sub_map", sub_map)
                seed = sub_map[seed]
                break
        if old_seed == seed:
            print("seed", seed, "did not change")

    print("seed_to_location", seed)
    return seed


def seed_to_location_v2(seed, maps):
    print("seed_to_location", seed, maps)
    old_name = "seeds"
    for i in range(len(maps)):
        old_seed = seed
        new_map = maps[i][1]
        map_name = maps[i][0]
        print("seed", seed, "will be map from", old_name, "to", map_name)
        old_name = map_name
        for sub_map in new_map:
            print("sub_map", sub_map)
            sub_map = sub_map[0]
            if sub_map[1] >= seed >= sub_map[0]:
                print("seed", seed, "mapped to", seed - sub_map[2], "in sub_map", sub_map)
                seed -= sub_map[2]
                break
        if old_seed == seed:
            print("seed", seed, "did not change")

    print("seed_to_location", seed)
    return seed


def min_location(content):
    print("min_location")
    seeds, maps = read_content(content)
    locations = []
    maps_names = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature",
                  "temperature-to-humidity", "humidity-to-location"]
    # add names to maps
    maps = list(zip(maps_names, maps))
    print(maps)
    for seed in seeds:
        location = seed_to_location_v2(seed, maps)
        locations.append(location)
    print(locations)
    print("min_location", min(locations))
    return min(locations)


def test():
    file_paths = ["data/example.txt"]
    res = [35]
    for file_path, result in zip(file_paths, res):
        content = read_file(file_path)
        if min_location(content) != result:
            print("Test failed for file: " + file_path)
            print("Expected: " + str(result)
                  + " Actual: " + str(min_location(content)))
            return


if __name__ == "__main__":
    file_path = "data/day-5.txt"
    # file_path = "data/example.txt"
    main(file_path, min_location, min_location, do_sum=False)
    # test()
