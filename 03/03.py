# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("03_input.txt", "r")
content = input_file.read()
content = content.split("\n")

# print(content)

# PART 1

# Get the special characters in a list
special_char = []
for line in content:
    line = list(line)
    for char in line:
        if (
            not char.isalpha()
            and not char.isdigit()
            and char != "."
            and char not in special_char
        ):
            special_char.append(char)
print(f"Special characters: {special_char}")


def get_number_index(line, original_index):
    if original_index[0] > 0:
        original_index[0] = original_index[0] - 1
    if original_index[-1] < len(line):
        original_index[-1] = original_index[-1] + 1
    index_range = original_index[0], original_index[-1]
    return index_range


# Get all the numbers
def get_numbers(line):
    numbers = []
    line = list(line)
    num = ""
    index = []
    for count, value in enumerate(line):
        # print(count, value)
        if value.isdigit():
            # print(f"enum: {count, value}")
            num += value
            index.append(count)
            # print(num, index)
            if (count + 1) == len(line):
                num_index_range = get_number_index(line, index)
                numbers.append([num, num_index_range])
                break
            continue
        if num:
            # print(f"Num and index: {num, index}")
            num_index_range = get_number_index(line, index)
            numbers.append([num, num_index_range])
            num = ""
            index = []
    return numbers


ok_numbers = []
prev_num = []
next_num = []

for i in range(len(content)):
    numbers_list = []
    line = content[i]
    if i > 0:
        prev_line = content[i - 1]
    else:
        prev_line = None
    if i < (len(content) - 1):
        next_line = content[i + 1]
    else:
        next_line = None

    retrieved_numbers = get_numbers(line)
    for item in retrieved_numbers:
        numbers_list.append(item)

    for index, char in enumerate(line):
        if char in special_char:
            # print(f"index: {char} -> {index}")
            for number in numbers_list:
                # print(index)
                if index in range(number[1][0], number[1][1] + 1):
                    ok_numbers.append(int(number[0]))

    if prev_line:
        for index, char in enumerate(prev_line):
            if char in special_char:
                for number in numbers_list:
                    if index in range(number[1][0], number[1][1] + 1):
                        ok_numbers.append(int(number[0]))

    if next_line:
        for index, char in enumerate(next_line):
            if char in special_char:
                for number in numbers_list:
                    if index in range(number[1][0], number[1][1] + 1):
                        ok_numbers.append(int(number[0]))


# print(f"OK numbers: {ok_numbers}")

print(f"part 1: {sum(ok_numbers)}, but it's too low, so...")


# PART 2

print(f"part 2: ")

input_file.close()
