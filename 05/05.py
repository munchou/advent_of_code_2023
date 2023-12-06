# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("05_input.txt", "r")
content = input_file.read()
content = content.split("\n")

# print(content)

PART_CHOSEN = 1

# PART 1
"""Tranforming the input to get a usable dictionary"""
u = str(content)[1:-1]
u = u.replace("'', ", "")
u = u.replace("'", "")
u = u.replace(":", "")
u = u.replace(" map", "")
u = u.split(", ")
seeds_start = u[0]

u.remove(u[0])
seeds_start = seeds_start.split(" ")[1:]
# print(f"SEEDS: {seeds_start}")

if PART_CHOSEN == 2:
    """Unfortunately there are waaaaaay too many inputs (billions),
    and I have no idea how to optimize that, so my PC gave me a
    MemoryError, I cannot think of a way to make that faster and lighter."""
    seeds_pairs = []
    zx = 1
    for num in seeds_start:
        try:
            seeds_pairs.append((seeds_start[zx - 1], seeds_start[zx]))
            zx += 2
        except Exception:
            pass

    new_seeds = []

    for pair in seeds_pairs:
        # print(pair)
        for h in range(int(pair[1])):
            # print(int(pair[0]) + h)
            new_seeds.append(int(pair[0]) + h)
    # print(new_seeds)
    print("Pairs done")
    seeds_start = new_seeds

first_list = []
to_add = []

k = 0
while k < len(u):
    if u[k][0].isalpha():
        to_add.append(u[k])
    try:
        if u[k + 1][0].isdigit():
            to_add.append(u[k + 1].split(" "))
            k += 1
            if k + 1 == len(u):
                first_list.append(to_add)
                break
            continue
        k += 1

        first_list.append(to_add)
        to_add = []
    except IndexError:
        pass

# print(first_list)

zupa_dico = {}
for item in first_list:
    label = item[0]
    values = []
    for i in range(1, len(item)):
        destination = int(item[i][0])
        source = int(item[i][1])
        range_len = int(item[i][2])
        range_end = source + range_len
        values.append([destination, source, range_end])
    zupa_dico[label] = values

# print(zupa_dico)


def get_soil(data, dico):
    res = []
    round = 0
    for seed in data:
        seed = int(seed)
        for u in dico:
            round += 1
            if seed in range(u[1], u[2]):
                result = seed - u[1] + u[0]
                res.append(result)
                round = 0
                break
            else:
                if round == len(dico):
                    res.append(seed)
                    round = 0
                    break
                continue
    return res


soil = get_soil(seeds_start, zupa_dico["seed-to-soil"])
print("Soil done")
fertilizer = get_soil(soil, zupa_dico["soil-to-fertilizer"])
print("fertilizer done")
water = get_soil(fertilizer, zupa_dico["fertilizer-to-water"])
print("water done")
light = get_soil(water, zupa_dico["water-to-light"])
print("light done")
temperature = get_soil(light, zupa_dico["light-to-temperature"])
print("temperature done")
humidity = get_soil(temperature, zupa_dico["temperature-to-humidity"])
print("humidity done")
location = get_soil(humidity, zupa_dico["humidity-to-location"])
print("location done")


if PART_CHOSEN == 1:
    print(f"part 1: {min(location)}")
else:
    print(f"part 2: {min(location)}")


input_file.close()
