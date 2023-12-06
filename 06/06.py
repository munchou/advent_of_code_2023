# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("06_input.txt", "r")
content = input_file.read()
content = content.split()

# print(content)

# PART 1
content_length_half = int(len(content) / 2)
content_p1 = content[1:content_length_half]  # race duration in milliseconds
content_p2 = content[content_length_half + 1 :]  # distance in millimeters


def num_of_ways(duration, distance):
    finished_races = 0
    for i in range(duration + 1):
        remaining_time = duration - i
        traveled_distance = i * remaining_time
        if traveled_distance > distance:
            finished_races += 1
    return finished_races


def get_duration_distance(content_p1, content_p2):
    total_done_races = []
    for s in range(len(content_p1)):
        duration = int(content_p1[s])
        distance = int(content_p2[s])
        total_done_races.append(num_of_ways(duration, distance))

    num_of_ways_to_beat_the_record = 1
    for i in range(len(total_done_races)):
        num_of_ways_to_beat_the_record *= total_done_races[i]
    return num_of_ways_to_beat_the_record


def part2_get_duration_distance(content_p1, content_p2):
    total_done_races = []
    duration = content_p1
    distance = content_p2
    total_done_races.append(num_of_ways(duration, distance))

    num_of_ways_to_beat_the_record = 1
    for i in range(len(total_done_races)):
        num_of_ways_to_beat_the_record *= total_done_races[i]
    return num_of_ways_to_beat_the_record


# PART 2
part2_duration = ""
for num in content_p1:
    part2_duration += str(num)
part2_duration = int(part2_duration)

part2_distance = ""
for num in content_p2:
    part2_distance += str(num)
part2_distance = int(part2_distance)


print(f"part 1: {get_duration_distance(content_p1, content_p2)}")
print(f"part 2: {part2_get_duration_distance(part2_duration, part2_distance)}")


input_file.close()
