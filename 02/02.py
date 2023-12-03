# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("02_input.txt", "r")
content = input_file.read()
content = content.split("\n")

games_dict = {}

# PART 1
red_limit = 12
green_limit = 13
blue_limit = 14

# Remove "Game" and useless space, create a dictionary
for i in content:
    i = i.replace("Game", "").strip()
    i = i.split(":")
    games_dict[i[0]] = i[1][1:]


bad_items = []

for item in games_dict:
    cubes_draw = games_dict[item]
    cubes_draw = cubes_draw.split(";")
    for draw in cubes_draw:
        draw = draw.split(",")
        for u in draw:
            if "red" in u:
                number = ""
                for char in u:
                    if char.isdigit():
                        number += char
                if int(number) > red_limit:
                    # print(item, number)
                    if item not in bad_items:
                        bad_items.append(item)
                    break
            if "blue" in u:
                number = ""
                for char in u:
                    if char.isdigit():
                        number += char
                if int(number) > blue_limit:
                    # print(item, number)
                    if item not in bad_items:
                        bad_items.append(item)
                    break
            if "green" in u:
                number = ""
                for char in u:
                    if char.isdigit():
                        number += char
                if int(number) > green_limit:
                    # print(item, number)
                    if item not in bad_items:
                        bad_items.append(item)
                    break

ok_games = 0
for num in range(1, 101):
    if str(num) not in bad_items:
        ok_games += num

print(f"part 1: {ok_games}")

# PART 2 (reusing the previously generated dictionary)
final_powaaa = []
for item in games_dict:
    cubes_draw = games_dict[item]
    cubes_draw = cubes_draw.replace(";", ",")
    cubes_draw = cubes_draw.split(",")
    min_green = 0
    min_red = 0
    min_blue = 0
    for i in cubes_draw:
        if "blue" in i:
            number = ""
            for char in i:
                if char.isdigit():
                    number += char
            if int(number) > min_blue:
                min_blue = int(number)
        if "green" in i:
            number = ""
            for char in i:
                if char.isdigit():
                    number += char
            if int(number) > min_green:
                min_green = int(number)
        if "red" in i:
            number = ""
            for char in i:
                if char.isdigit():
                    number += char
            if int(number) > min_red:
                min_red = int(number)

    powaaa = min_green * min_red * min_blue
    # print(f"g:{min_green}, r:{min_red}, b:{min_blue}, {powaaa}")
    final_powaaa.append(powaaa)

# print(final_powaaa)
# print(sum(final_powaaa))

print(f"part 2: {sum(final_powaaa)}")

input_file.close()
