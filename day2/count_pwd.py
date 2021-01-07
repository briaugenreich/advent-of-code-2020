

def count_valid_password1(password, key, min, max):
    count = password.count(key)
    if count >= min and count <= max:
        # print('Password is valid! ', password, '|', min, '-', max, ':', key)
        return 1
    else:
        return 0

def count_valid_password2(password, key, pos1, pos2):
    pos1 = pos1 -1
    pos2 = pos2 - 1
    if key == password[pos1] and key == password[pos2]:
        return 0
    elif key == password[pos1] or key == password[pos2]:
        return 1

    return 0

valid_count1=0
valid_count2=0
with open('input.txt', 'r') as input_file:
    for line in input_file.readlines():
        arr = line.split(' ')
        arr2 = arr[0].split('-')
        pos1 = int(arr2[0])
        pos2 = int(arr2[1])
        key = arr[1].replace(':', '').strip()
        pwd = arr[2]
        valid_count1 = valid_count1 + count_valid_password1(pwd, key, pos1, pos2)
        valid_count2 = valid_count2 + count_valid_password2(pwd, key, pos1, pos2)

print("Valid passwords problem 1:", valid_count1)
print("Valid passwords problem 2:", valid_count2)
