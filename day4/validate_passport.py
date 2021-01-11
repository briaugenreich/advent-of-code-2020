import re
# TODO is there a more elegant solution???

passport = ''
passport_criteria=['byr', 'iyr',"eyr", "hgt", "hcl", "ecl", "pid"]
valid_count=0
with open("input.txt") as input_file:
    for line in input_file.readlines():
        if line == '\n':
            result = [val in passport for val in passport_criteria]
            if result.count(False) == 0:
                valid_count+=1
            passport = ''
        else:
            passport+=line
    result = [val in passport for val in passport_criteria]
    if result.count(False) == 0:
        valid_count += 1
    print(valid_count)


passport = ''
passport_keys=['byr', 'iyr',"eyr", "hgt", "hcl", "ecl", "pid"]
valid_count = 0
valid_vals = True


def valid_kv(k, v):
    valid = False
    if k == 'byr' and int(v) >= 1920 and int(v)<= 2002:
        valid= True
    elif k == 'iyr' and int(v) >= 2010 and int(v) <=2020:
        valid = True
    elif k == 'eyr' and int(v) >= 2020 and int(v) <=2030:
        valid = True
    elif k == 'hgt':
        if v.endswith('cm') and int(v[:-2]) >= 150 and int(v[:-2]) <=193:
            valid = True
        elif v.endswith('in') and int(v[:-2]) >= 59 and int(v[:-2]) <=76:
            valid = True
    elif k == 'hcl' and  re.match('^#[0-9A-Fa-f]{6}$', v):
        valid = True
    elif k == 'ecl' and v in ["amb", "blu", "brn",  "gry", "grn", "hzl", "oth"]:
        valid = True
    elif k == 'pid' and re.match('^[0-9]{9}$', v):
        valid = True
    elif k == 'cid':
        valid = True
    return valid


with open("input.txt") as input_file:
    for line in input_file.readlines():
        if line == '\n':
            result = [key in passport for key in passport_keys]
            if result.count(False) == 0:
                for kv in passport.replace("\n", " ").strip().split(" "):
                    kv_split = kv.split(':')
                    key = kv_split[0]
                    val = kv_split[1]

                    valid_vals = valid_vals and valid_kv(key, val)
                if valid_vals:
                    valid_count+=1
            passport = ''
            result = []
            valid_vals = True
        else:
            passport+=line
    result = [key in passport for key in passport_keys]
    if result.count(False) == 0:
        for kv in passport.replace("\n", " ").strip().split(" "):
            kv_split = kv.split(':')
            key = kv_split[0]
            val = kv_split[1]

            valid_vals = valid_vals and valid_kv(key, val)
        if valid_vals:
            valid_count += 1
    print(valid_count)





