# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("01_input.txt", "r")
content = input_file.read()
content = content.split("\n")

listy = []


def get_calibration(item):
    digits_only = []
    all_numbers = []
    num_alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_alpha_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for group in item:
        numbers = []
        digits = []
        for char in group:
            if type(char) is list:
                for item in char:
                    if item in num_alpha:
                        chara = num_alpha_dict[item]
                        numbers.append(chara)
            else:
                numbers.append(int(char))
                digits.append(int(char))
        digits_combo = int(f"{digits[0]}{digits[-1]}")
        all_numbers_combo = int(f"{numbers[0]}{numbers[-1]}")
        digits_only.append(digits_combo)
        all_numbers.append(all_numbers_combo)
    return digits_only, all_numbers


for i in content:
    if i:
        listy.append(i)

calibration_list = []

""" For part 2: one must take into account alpha numbers ("one", "two", etc.)
Problem: they are stuck to each other, there is a specific order, AND some letters
were erased such as the "t" in "eightwo" instead of "eighttwo".
First step: separate the alpha characters from the digit.
Second: check if they is misspelling in the strings (if so, correct them).
Third: separate the numbers with ".", which allows me to split the string
and keep the order of the numbers.
Fourth: convert the alpha numbers into digits by using a dictionary."""
letters = ""
all_lines = []
for line in listy:
    for char in line:
        if char.isalpha():
            letters += char
        else:
            letters += f".{char}."

    letters = letters.split(".")
    for g in letters:
        if g == "":
            letters.remove(g)

    num_alpha = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for u in num_alpha:
        for i in range(len(letters)):
            if "eightwo" in letters[i]:
                letters[i] = letters[i].replace("eightwo", "eighttwo")
            if "eighthree" in letters[i]:
                letters[i] = letters[i].replace("eighthree", "eightthree")
            if "oneight" in letters[i]:
                letters[i] = letters[i].replace("oneight", "oneeight")
            if "twone" in letters[i]:
                letters[i] = letters[i].replace("twone", "twoone")
            if "threeight" in letters[i]:
                letters[i] = letters[i].replace("threeight", "threeeight")
            if "fiveight" in letters[i]:
                letters[i] = letters[i].replace("fiveight", "fiveeight")
            if "sevenine" in letters[i]:
                letters[i] = letters[i].replace("sevenine", "sevennine")
            if "nineight" in letters[i]:
                letters[i] = letters[i].replace("nineight", "nineeight")
            if u in letters[i]:
                letters[i] = letters[i].replace(u, f".{u}.")
    for t in range(len(letters)):
        item = letters[t]
        if not item.isdigit():
            item = item.split(".")
            for f in item:
                if f == "":
                    item.remove(f)
            letters[t] = item

    all_lines.append(letters)

    letters = ""

digits_list, numbers_list = get_calibration(all_lines)
print(f"part 1: {sum(digits_list)}")
print(f"part 2: {sum(numbers_list)}")


input_file.close()
