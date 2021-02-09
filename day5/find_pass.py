import math



def find_seat_id(seat_str, str_index, row_min, row_max, col_min, col_max):
    #base case
    if row_max == row_min and col_max == col_min:
        print("Found Row:", row_max, "Found Col:", col_max, "---> Seat:", row_max * 8 + col_max)
        return row_max * 8 + col_max
    #row search
    if str_index <= 6:
        split_point = math.floor((row_max - row_min)/2)
        if seat_str[str_index] == 'F':
            row_max = row_min + split_point
        else:
            row_min = row_max - split_point
    #col search
    else:
        split_point = math.floor((col_max - col_min) / 2)
        if seat_str[str_index] == 'L':
            col_max = col_min + split_point
        else:
            col_min = col_max - split_point

    str_index = str_index + 1
    return find_seat_id(seat_str, str_index, row_min, row_max, col_min, col_max)


# seat = "FBFBBFFRLR"
# print(find_seat_id(seat, 0, 0, 127, 0, 7))
max_seat_id=0
seats = []
with open("input.txt") as input_file:
    for line in input_file.readlines():
        max_seat_id = max(max_seat_id, find_seat_id(line, 0, 0, 127, 0, 7))
        seats.append(find_seat_id(line, 0, 0, 127, 0, 7))
print("Max Seat Id is....", max_seat_id)

# another way to find missing seat?
seats.sort()
for x in range(len(seats)-1):
    if seats[x] + 2 == seats[x +1]:
        print("found missing seat", seats[x]+1 )
