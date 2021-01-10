
def get_tree_count(right, down, input):
    x = 0
    y = 0
    tree_count = 0
    while y < len(input) - 1:
        x = x + right
        y = y + down
        curr_path = input[y]
        if curr_path[x % len(curr_path)] == '#':
            tree_count = tree_count + 1
    return tree_count

with open("input.txt", "r") as input_file:
    input = [line.strip() for line in input_file.readlines()]
    print(get_tree_count(3,1, input))
    answer2 = get_tree_count(1,1, input) * get_tree_count(3,1, input) * get_tree_count(5,1, input) * get_tree_count(7,1, input) * get_tree_count(1,2, input)
    print(answer2)


