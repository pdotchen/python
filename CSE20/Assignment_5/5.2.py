# from 5.1
numbers = input()
numbers = numbers.split(',')  # becomes list of numbers
numbers = [int(i) for i in numbers]

ord_nums = numbers
ord_nums.sort()
mode_ord = []
for i in ord_nums:
    mode_ord.append(i // 10)  # makes all numbers in list mode_ord % 10

mode_dict = {}  # dictionary of elements and all occurrences
for v in mode_ord:
    if v in mode_dict:
        mode_dict[v] += 1
    else:
        mode_dict[v] = 1

mode_k = 0  # range of largest occurrences
mode_val = 0  # biggest occurrences of values
for k in mode_dict:
    if mode_dict[k] > mode_val:
        mode_val = mode_dict[k]
        mode_k = k

max = ord_nums[-1]

# 5.2
all_nums = []
for i in range(0, max + 1, 10):
    all_nums.append(i)

mode_dict_vals = []  # all values in mode_dict
mode_dict_keys = [i * 10 for i in mode_dict]  # all keys in mode_dict
pounds = []
for i in mode_dict.values():
    mode_dict_vals.append(i)
for i in mode_dict_vals:
    pounds.append(int((i / mode_val) * 16))

for i in all_nums:
    if i not in mode_dict_keys:
        if i == 0:
            print('  0', (" " * 16), '0')
        elif 10 <= i < 100:
            print('', i, (" " * 16), '0')
        elif 100 <= i <= max:
            print(i, (" " * 16), '0')
    else:
        if i == 0:
            print('  0', ('#' * pounds[mode_dict_keys.index(i)]) + (" " * (16 - pounds[mode_dict_keys.index(i)])),
                  mode_dict_vals[mode_dict_keys.index(i)])
        elif 10 <= i < 100:
            print('', i, ('#' * pounds[mode_dict_keys.index(i)]) + (" " * (16 - pounds[mode_dict_keys.index(i)])),
                  mode_dict_vals[mode_dict_keys.index(i)])
        elif 100 <= i <= max:
            print(i, ('#' * pounds[mode_dict_keys.index(i)]) + (" " * (16 - pounds[mode_dict_keys.index(i)])),
                  mode_dict_vals[mode_dict_keys.index(i)])
