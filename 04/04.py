# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("04_input.txt", "r")
content = input_file.read()
content = content.split("\n")

# print(content)

# PART 1
"""Transform the input into a dictionary:
'Card x': [winning numbers], [owned numbers]"""
test = []
cards_dict = {}

for item in content:
    item = item.split(":")
    u = item[1].strip().split("|")
    v = []
    for i in u:
        i = i.split()
        v.append(i)

    cards_dict[item[0]] = v


def get_points_from_winning_cards(card):
    winning_cards = cards_dict[card][0]
    owned_cards = cards_dict[card][1]
    winning_numbers = 0
    for i in owned_cards:
        if i in winning_cards:
            winning_numbers += 1
    # print(f"{card} -> {winning_numbers} winning numbers")
    if winning_numbers == 1:
        return 1
    elif winning_numbers > 1:
        return 2 ** (winning_numbers - 1)
    else:
        return 0


score = 0
for i in range(len(content)):
    i += 1
    space = ""
    if i < 10:
        space = "  "
    if 9 < i < 100:
        space = " "
    card = f"Card {space}{i}"
    points = get_points_from_winning_cards(card)
    score += points

print(f"part 1: {score}")


# PART 2
"""Build a dictionary to save the instances of each card."""
cards_instances_dict = {}
for i in range(1, len(content) + 1):
    cards_instances_dict[f"Card {i}"] = 1
# print(cards_instances_dict)


def get_matching_numbers(card):
    winning_cards = cards_dict[card][0]
    owned_cards = cards_dict[card][1]
    winning_numbers = 0
    for i in owned_cards:
        if i in winning_cards:
            winning_numbers += 1
    return winning_numbers


"""Get the numbers of instances"""
for i in range(len(content)):
    i += 1
    space = ""
    if i < 10:
        space = "  "
    if 9 < i < 100:
        space = " "
    card = f"Card {space}{i}"
    points = get_matching_numbers(card)
    # update dict to add +1 to the next card(s)
    # which means card i+u for u in range(1, points+1)
    copies = cards_instances_dict[f"Card {i}"]
    for c in range(1, copies + 1):
        for u in range(1, points + 1):
            try:
                cards_instances_dict[f"Card {i+u}"] += 1
            except KeyError:
                pass

summy = 0
for card in cards_instances_dict:
    summy += cards_instances_dict[card]

print(f"part 2: {summy}")

input_file.close()
