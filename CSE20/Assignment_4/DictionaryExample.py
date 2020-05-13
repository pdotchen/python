import copy

dict1 = {"a": 1, "b": 1, "c": 1, "d": 2, "e": 3, "f": 4, "g": 0}
print(dict1)

dict2 = dict()
for key in dict1.keys():
    value = dict1[key]
    if value in dict2.keys():
        dict2[value].append(key)
    else:
        dict2[value] = [key]

print(dict2)
min_point = min(dict2.keys())
print(min_point)

list_attacks = dict2[min_point]
print(list_attacks)

lowest_attack = 'zzz'
for attack in list_attacks:
    if attack < lowest_attack:
        lowest_attack = attack
print(lowest_attack)

def extract_max(dictionary):
    dict2 = dict()
    for key in dictionary.keys():
        value = dictionary[key]
        if value in dict2.keys():
            dict2[value].append(key)
        else:
            dict2[value] = [key]
    max_val = max(dict2.keys())
    list_names = dict2[max_val]
    lowest_attack = 'zzz'
    for attack in list_names:
        if attack < lowest_attack:
            lowest_attack = attack
    return  lowest_attack

copy_dict1 = copy.deepcopy(dict1)
list = []
while len(list) < len(dict1):
    name = extract_max(copy_dict1)
    list.append(name)
    del copy_dict1[name]

print(list)