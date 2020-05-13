# def twos(array):
#     tf = True
#     for i, v in enumerate(array):
#         if v == 2:
#             if i == 0:
#                 if array[i + 1] != 2:
#                     tf = False
#                     break
#             elif i == (len(array) - 1):
#                 if array[i - 1] != 2:
#                     tf = False
#                     break
#             elif array[i - 1] != 2:
#                 if array[i + 1] != 2:
#                     t_f = False
#                     break
#     return tf
# #
#
# arr = [2, 2, 1]
# print(twos(arr))
# lis = ['s', 'd']
# course = {'h': 1, 'b': 2}
# print(list(course.keys()))
# print(course)
#
# print(course['h'])
#
# x = [2,2,2,3,3,2]
# print(twos(x))

# def non_zero_digits(x):
#     nnz = [int(d) for d in str(x)]
#     sum = 0
#     for i in nnz:
#         if i != 0:
#             sum += 1
#     return sum
#
# print(non_zero_digits(100))

# for i in range(11, 1001):
#     if i % 10 > 0:
#         print(i, end=' ')
#     else:
#         print(i)

# def matches(x):
# #     dic = {}
# #     l = [i for i in x]
# #     for i in l:
# #         if i in dic:
# #             return i
# #         else:
# #             dic[i] = 0
# #     return "none"
# #
# # x = "ABA"
# # print(matches(x))
fn = lambda x, y : x + y > 10

#lambda definition is equivalent to
#def fn(x, y):
#  return x + y > 10

print(fn(5, 2))
