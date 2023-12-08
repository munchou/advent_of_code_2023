# That messy code was brought to you by munchou. At least it works. Yay!
from operator import itemgetter

input_file = open("07_input.txt", "r")
content = input_file.read()
content = content.split()

# print(content)

CHOSEN_PART = 2

# PART 1

# The following dictionaries are used to give each card (King, Queen, etc.)
# a value by using a letter, so that the hand of cards can be converted
# into a corresponding string, which then will be used to sort lists in the
# (reversed) alphabetical order.
if CHOSEN_PART == 1:
    cards_strength_dico = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "D",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M",
    }
else:
    cards_strength_dico = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "Z",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M",
    }


# Cards strentgh from 7 (Five of a kind) to 0 (all different)


def transform_hand_into_values(card):
    new_hand = ""
    for char in card:
        char_value = cards_strength_dico[char]
        new_hand += char_value
    # print(card, new_hand)
    return new_hand


def cards_strength(card):
    # for cards in cards_list:
    card = cards[0]
    cards_count = []
    if CHOSEN_PART == 2:
        if "J" in card:
            number_of_j = card.count("J")
            temp_card = card.replace("J", "")
            new_cards_count = []
            for char in temp_card:
                if [char, card.count(char)] not in new_cards_count:
                    new_cards_count.append([char, card.count(char)])
            if len(new_cards_count) != 0:
                new_cards_count = sorted(new_cards_count, key=itemgetter(1))
                new_cards_count[-1][1] += number_of_j
                new_card = card.replace("J", new_cards_count[-1][0])
                card_with_j = [card, new_card]
                card, old_card = card_with_j[1], card_with_j[0]
            else:
                old_card = card
        else:
            old_card = card

    for char in card:
        if [char, card.count(char)] not in cards_count:
            cards_count.append([char, card.count(char)])
    cards_count.sort(key=lambda cards_count: cards_count[1])

    if len(cards_count) == 5:
        if CHOSEN_PART == 2:
            card = old_card
        return [transform_hand_into_values(card), 0, int(cards[1])]
    if len(cards_count) == 4:
        if CHOSEN_PART == 2:
            card = old_card
        return [transform_hand_into_values(card), 1, int(cards[1])]
    if len(cards_count) == 3:
        if CHOSEN_PART == 2:
            card = old_card
        if (
            cards_count[0][1] == cards_count[1][1] == 2
            or cards_count[0][1] == cards_count[2][1] == 2
            or cards_count[1][1] == cards_count[2][1] == 2
        ):
            return [transform_hand_into_values(card), 2, int(cards[1])]
        else:
            return [transform_hand_into_values(card), 3, int(cards[1])]
    if len(cards_count) == 2:
        if CHOSEN_PART == 2:
            card = old_card
        if cards_count[0][1] == 4 or cards_count[1][1] == 4:
            return [transform_hand_into_values(card), 5, int(cards[1])]
        else:
            return [transform_hand_into_values(card), 4, int(cards[1])]
    else:
        if CHOSEN_PART == 2:
            card = old_card
        return [transform_hand_into_values(card), 6, int(cards[1])]


# Step 1: Tranform the input to get a list of cards: [hand, bid amount]
cards_list = []
u = 0
for i in range(len(content)):
    if u + 1 < len(content):
        cards_list.append([content[u], content[u + 1]])
        u += 2

# Step 2: Get the type of hand by assigning a score (6 = strongest
# (Five of a kind), 0 = weakest) and return [hand, score]
# Add and sort the list from weakest to strongest
hands_by_type_0 = []
hands_by_type_1 = []
hands_by_type_2 = []
hands_by_type_3 = []
hands_by_type_4 = []
hands_by_type_5 = []
hands_by_type_6 = []
for cards in cards_list:
    card_type = cards_strength(cards)
    if card_type[1] == 0:
        hands_by_type_0.append(card_type)
    if card_type[1] == 1:
        hands_by_type_1.append(card_type)
    if card_type[1] == 2:
        hands_by_type_2.append(card_type)
    if card_type[1] == 3:
        hands_by_type_3.append(card_type)
    if card_type[1] == 4:
        hands_by_type_4.append(card_type)
    if card_type[1] == 5:
        hands_by_type_5.append(card_type)
    if card_type[1] == 6:
        hands_by_type_6.append(card_type)


hands_by_type_0 = sorted(hands_by_type_0, key=itemgetter(0), reverse=True)
hands_by_type_1 = sorted(hands_by_type_1, key=itemgetter(0), reverse=True)
hands_by_type_2 = sorted(hands_by_type_2, key=itemgetter(0), reverse=True)
hands_by_type_3 = sorted(hands_by_type_3, key=itemgetter(0), reverse=True)
hands_by_type_4 = sorted(hands_by_type_4, key=itemgetter(0), reverse=True)
hands_by_type_5 = sorted(hands_by_type_5, key=itemgetter(0), reverse=True)
hands_by_type_6 = sorted(hands_by_type_6, key=itemgetter(0), reverse=True)

# print(f"hands_by_type_0: {hands_by_type_0}")
# print(f"hands_by_type_1: {hands_by_type_1}")
# print(f"hands_by_type_2: {hands_by_type_2}")
# print(f"hands_by_type_3: {hands_by_type_3}")
# print(f"hands_by_type_4: {hands_by_type_4}")
# print(f"hands_by_type_5: {hands_by_type_5}")
# print(f"hands_by_type_6: {hands_by_type_6}")

all_ordered_hands = []
for hand in hands_by_type_0:
    all_ordered_hands.append(hand)
for hand in hands_by_type_1:
    all_ordered_hands.append(hand)
for hand in hands_by_type_2:
    all_ordered_hands.append(hand)
for hand in hands_by_type_3:
    all_ordered_hands.append(hand)
for hand in hands_by_type_4:
    all_ordered_hands.append(hand)
for hand in hands_by_type_5:
    all_ordered_hands.append(hand)
for hand in hands_by_type_6:
    all_ordered_hands.append(hand)


# print(f"ALL HANDS: {all_ordered_hands}")
list_of_winnigs = []
for i, hand in enumerate(all_ordered_hands, 1):
    list_of_winnigs.append(i * hand[2])


# PART 2

if CHOSEN_PART == 1:
    print(f"part 1: {sum(list_of_winnigs)}")
else:
    print(f"part 2: {sum(list_of_winnigs)}")


input_file.close()
