# n = int(input())
# command = input()
# print(command[:n])
# for char in command[n:len(command)]:
#     print('&'*(n-1) + char)

# def int_to_Roman(num):
#     val = [10, 9, 5, 4, 1]
#     syb = ["X", "IX", "V", "IV", "I"]
#     roman_num = ''
#     i = 0
#     while num > 0:
#         for _ in range(num // val[i]):
#             roman_num += syb[i]
#             num -= val[i]
#         i += 1
#     return roman_num
# Greek = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa"]
# m = int(input())
# n = int(input())
# res_mat = [[(Greek[i] + '_' +int_to_Roman(j + 1)) for j in range(n)] for i in range(m)]
# for x in res_mat:
#     print(*x, sep=' ')

# def Get_Sym(x1,y1,x2,y2):
#     d = x1 - x2
#     print(x1 + d)
#     d = y1 - y2
#     print(y1 + d)
#
#
# xa = int(input())
# ya = int(input())
#
# xb = int(input())
# yb = int(input())
#
# xc = int(input())
# yc = int(input())
#
# if xc >= min(xa,xb) and xc <= max(xa,xb) and yc >= min(ya,yb) and yc <= max(ya,yb):
#     print(False)
# else:
#     Get_Sym(xc,yc,xa,ya)
#     Get_Sym(xc,yc,xb,yb)


# def check(num):
#     count = 0
#     n = num
#     while n != 0:
#         rem = n % 10
#         if rem == 3:
#             count += 1
#         n = n // 10
#     return count == 3
# dict = [None] * 100000
# dict[0] = 333
# cnt = 1
# for i in range(1333,99993333):
#     if check(i):
#         dict[cnt] = i
#         cnt += 1
#     if cnt == 10003:
#         break
# n = int(input())
# print(dict[n - 1])

# import math
#
# def check(num):
#     count = 0
#     n = num
#     while n != 0:
#         rem = n % 10
#         if rem == 3:
#             count += 1
#         n = n // 10
#     return count == 0
#
# able = [0]
# for i in range(1500):
#     if check(i):
#         able.append(i)
#
# dict = [9999999999] * 43033600
# cnt = 0
# for i in able:
#     for j in able:
#         num = j
#         num = num + 333 * (10 ** (int(math.log10(num)) + 1) if num != 0 else 1)
#         num = num + i * (10 ** (int(math.log10(num)) + 1) if num != 0 else 1)
#         dict[cnt] = num
#         cnt += 1
#
# dict.sort()
# n = int(input())
# print(dict[n])
#

a = int(input())
b = int(input())
list1 = []
input_sum = 0
while True:
    c = input()
    if c != "0":
        list1.append(c)
        input_sum += 1
    else:
        break
num_sum_end = 0
len_sum = 0
num_sum_begin = 0
cur_num_word = 0
while input_sum - num_sum_begin >= 1:
    for j in range(num_sum_end + 1, input_sum + 1, 1):
        len_sum += len(str(list1[j - 1])) + 1
        num_sum_end += 1
        cur_num_word += 1
        if len_sum > a + 1 or cur_num_word > b:
            print(*list1[num_sum_begin:num_sum_end - 1:1])
            num_sum_begin = num_sum_end - 1
            cur_num_word = 0
            num_sum_end -= 1
            len_sum = 0
            break
    if input_sum == num_sum_end:
        print(*list1[num_sum_begin:num_sum_end:1])
        break

# a = int(input())
# b = int(input())
# comment = list()
# while True:
#     word = input()
#     if(word == "0"):
#         break
#     comment.append(word)
# cur_len = 0
# cur_word = 0
# for word in comment:
#     if cur_len + len(word) + (cur_len != 0) > a or cur_word >= b:
#         print()
#         cur_len = 0
#         cur_word = 0
#     if cur_len != 0:
#         print(' ' + word,end='')
#         cur_len += len(word) + 1
#         cur_word += 1
#     else:
#         print(word, end='')
#         cur_len += len(word)
#         cur_word += 1