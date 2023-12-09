# That messy code was brought to you by munchou. At least it works. Yay!

input_file = open("08_input.txt", "r")
content = input_file.read()
content = content.replace(" ", "")
content = content.replace("(", "")
content = content.replace(")", "")
content = content.replace("=", ",")
content = content.split("\n")

# print(content)

CHOSEN_PART = 2

# PART 1
path = list(content[0])
# print(path)
nodes = content[1:]
nodes_dico = {}
for node in nodes:
    node = node.split(",")
    nodes_dico[node[0]] = (node[1], node[2])
# print(nodes_dico)


def get_number_of_steps(path, nodes_dico):
    steps = 0
    starting_node = list(nodes_dico.keys())[0]

    current_node = starting_node
    i = 1
    while True:
        if i > len(path):
            i = 1
        direction = path[i - 1]
        node_left = nodes_dico[current_node][0]
        node_right = nodes_dico[current_node][1]
        # print(current_node, nodes_dico[current_node])
        if direction == "L":
            new_node = node_left
        else:
            new_node = node_right
        # print(f"direction: {direction}, NEW NODE: {new_node}")
        current_node = new_node
        i += 1
        steps += 1
        # print(f"STEPS: {steps}")
        if new_node == "ZZZ":
            return steps


result_part1 = get_number_of_steps(path, nodes_dico)


# PART 2
""" Nope, couldn't do it, cannot afford to spend
too many hours on one challenge. I'm not responsible
if your eyes start bleeding while having a look at
the following code."""


def check_if_same_steps(steps, nodes):
    nodes = list(nodes.values())
    if len(nodes) != 6:
        return False
    # print(nodes)
    first_step = nodes[0]
    # print(f"first step: {first_step}")
    for node in nodes:
        if node != first_step:
            return False
        continue
    return True


def get_number_of_steps_p2(path, starting_nodes, nodes_dico):
    steps = 0
    node_steps = {}

    if check_if_same_steps(steps, node_steps):
        print(f"YAAAAAY: {steps}")

    while not check_if_same_steps(steps, node_steps):
        for i in range(len(starting_nodes)):
            # print(starting_nodes[i])
            starting_node = starting_nodes[i]
            current_node = starting_node
            i = 1

            while True:
                if i > len(path):
                    i = 1
                direction = path[i - 1]
                node_left = nodes_dico[current_node][0]
                node_right = nodes_dico[current_node][1]
                if direction == "L":
                    new_node = node_left
                else:
                    new_node = node_right
                current_node = new_node
                i += 1
                steps += 1
                if new_node[-1] == "Z":
                    # print(current_node, new_node, steps)
                    node_steps[starting_node] = steps
                    # print(f"NODEAAAA: {node_steps}")
                    break

    return steps


starting_nodes = []
ending_nodes = []  # To make sure what the input gives back
for node in nodes_dico:
    if node[-1] == "A":
        starting_nodes.append(node)
    if node[-1] == "Z":
        ending_nodes.append(node)
print(starting_nodes)
# ['MXA', 'VQA', 'CBA', 'JBA', 'AAA', 'HSA']
print(ending_nodes)

result_part2 = get_number_of_steps_p2(path, starting_nodes, nodes_dico)

print(result_part2)

# print(f"part 1: {result_part1}")
print(f"part 2: ")


input_file.close()
