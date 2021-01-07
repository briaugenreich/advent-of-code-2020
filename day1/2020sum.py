
def find_2_multiple(input):
    small_index=0
    large_index=len(input) - 1

    while small_index != large_index:
        sum = input[small_index] + input[large_index]

        if sum > 2020:
            large_index = large_index - 1
        elif sum < 2020:
            small_index = small_index + 1
        else:
            print("Found values: ", input[small_index], input[large_index])
            return  input[small_index] * input[large_index]

    return -1

def find_3_multiple(input):
    curr = 0
    for elem in input:
        small_index = curr + 1
        large_index = len(input) - 1

        while small_index != large_index:
            sum = input[small_index] + input[large_index] + elem
            if sum > 2020:
                large_index = large_index - 1
            elif sum < 2020:
                small_index = small_index + 1
            else:
                print("Found values: ", elem, input[small_index], input[large_index])
                return elem * input[small_index] * input[large_index]
        curr = curr + 1
    return -1


input_file = open('input.txt', 'r')
input = [int(line.strip()) for line in input_file.readlines()]
input.sort()
print(find_2_multiple(input))
print(find_3_multiple(input))
