numbers = input()
numbers = numbers.split(',')    # becomes list of numbers
numbers = [int(i) for i in numbers]
print(len(numbers))

sum_of_nums = 0
for i in numbers:
    sum_of_nums += i

mean = sum_of_nums / len(numbers)
print('Mean    {:.2f}'.format(mean))

# median
median = 0
ord_nums = numbers
ord_nums.sort()
half = len(ord_nums) // 2

if len(ord_nums) % 2 == 0:
    median = (ord_nums[half] + ord_nums[half - 1]) / 2
else:
    median = ord_nums[half]

print('Median  {0:.2f}'.format(median))

# mode
mode_ord = []
for i in ord_nums:
    mode_ord.append(i // 10)    # makes all numbers in list mode_ord % 10

mode_dict = {}      # dictionary of elements and all occurrences
for v in mode_ord:
    if v in mode_dict:
        mode_dict[v] += 1
    else:
        mode_dict[v] = 1

mode_k = 0
mode_val = 0
for k in mode_dict:
    if mode_dict[k] > mode_val:
        mode_val = mode_dict[k]
        mode_k = k
        # looks through the dictionary for the biggest values and stores the multiple in mode_k
print('Mode   ', mode_k * 10)

# min
print('Minimum', ord_nums[0])

# max
print('Maximum', ord_nums[-1])