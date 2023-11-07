# a = int(input())
# b = int(input())
# if a < 0:
#     print(-(abs(a) % b))
# else:
#     print(a % b)

# st = input()
# st = ' ' + st + ' '
# check1 = (bool(st.find('massiv ') != -1) or (bool(st.find(' massiv') != -1)))
# check2 = (bool(st.find('hahaha ') != -1) or (bool(st.find(' hahaha') != -1)))
# check3 = (bool(st.find('manul ') != -1) or (bool(st.find(' manul') != -1)))
# print(check1 + check2 + check3 >=2)

# a = int(input())
# b = int(input())
# print(str(a + b) + str(a ** b) + str(a * b))

# a = int(input())
# b = int(input())
# res = a & b
# if a*b != 0:
#     print(res == 0)
# else:
#     print(a != 0)

# import sys
#
# def Dist(x, y, x_guess, y_guess):
#     return int(abs(x - x_guess) + abs(y - y_guess))
#
# x1, y1 = 0, 0
# print("?",x1, y1,"\n")
# sys.stdout.flush()
# dist1 = dist2 = int(input())
# x2, y2 = dist1, 0
# print("?", x2, y2,"\n")
# sys.stdout.flush()
# dist3 = int(input())
# x3 = int(((dist1 + dist2 - dist3) / 2))
# y3 = (dist2 - x3)
# print("?",x3,y3,"\n")
# sys.stdout.flush()
# dist = int(input())
# if dist == 0:
#     print('!', x3, y3, "\n")
#     sys.stdout.flush()
# else:
#     list = list()
#     for i in range(dist):
#         if (Dist(x3 + i, y3 + dist - i, x1, y1) == dist1) and (Dist(x3 + i, y3 + dist - i, x2, y2) == dist3):
#             list.append((x3 + i, y3 + dist - i))
#         if (Dist(x3 - i, y3 + dist - i, x1, y1) == dist1) and (Dist(x3 - i, y3 + dist - i, x2, y2) == dist3):
#             list.append((x3 - i, y3 + dist - i))
#         if (Dist(x3 + i, y3 - dist + i, x1, y1) == dist1) and (Dist(x3 + i, y3 - dist + i, x2, y2) == dist3):
#             list.append((x3 + i, y3 - dist + i))
#         if (Dist(x3 - i, y3 - dist + i, x1, y1) == dist1) and (Dist(x3 - i, y3 - dist + i, x2, y2) == dist3):
#             list.append((x3 - i, y3 - dist + i))
#     coor = set(list)
#     print(coor)
#     for coor_t in coor:
#         print("?", coor_t[0], coor_t[1], "\n")
#         sys.stdout.flush()
#         dist_check = int(input())
#         if dist_check == 0:
#             print('!', coor_t[0], coor_t[1], "\n")
#             sys.stdout.flush()
#             break

# print("!",x3,y3,"\n")
# sys.stdout.flush()
#

import math
import random
# import sys
#
# def Dist(x, y, x_guess, y_guess):
#     return int(abs(x - x_guess) + abs(y - y_guess))
#
# def Check(x, y):
#     return (Dist(x, y, x2, y2) == dist2) and (Dist(x, y, x3, y3) == dist3) and (Dist(x, y, x4, y4) == dist4) and (Dist(x, y, x5, y5) == dist5)
#
# x1, y1 = 0, 0
# print("?", x1, y1, "\n")
# sys.stdout.flush()
# dist1 = int(input())
# if dist1 == 0:
#     print('!', x1, y1, "\n")
#     sys.stdout.flush()
# else:
#     x2 = x1 + 1
#     y2 = y1 + 1
#     print("?", x2, y2, "\n")
#     sys.stdout.flush()
#     dist2 = int(input())
#     x3 = x1 - 1
#     y3 = y1 - 1
#     print("?", x3, y3, "\n")
#     sys.stdout.flush()
#     dist3 = int(input())
#     x4 = x1 - 1
#     y4 = y1
#     print("?", x4, y4, "\n")
#     sys.stdout.flush()
#     dist4 = int(input())
#     x5 = x1
#     y5 = y1 - 1
#     print("?", x5, y5, "\n")
#     sys.stdout.flush()
#     dist5 = int(input())
#     coor = list()
#     for i in range(dist1 + 1):
#         if Check(x1 + i, y1 + dist1 - i):
#             coor.append((x1 + i, y1 + dist1 - i))
#         if Check(x1 - i, y1 + dist1 - i):
#             coor.append((x1 - i, y1 + dist1 - i))
#         if Check(x1 + i, y1 - dist1 + i):
#             coor.append((x1 + i, y1 - dist1 + i))
#         if Check(x1 - i, y1 - dist1 + i):
#             coor.append((x1 - i, y1 - dist1 + i))
#     res_coor = set(coor)
#     for coor_t in res_coor:
#         print("?", coor_t[0], coor_t[1], "\n")
#         sys.stdout.flush()
#         dist_check = int(input())
#         if dist_check == 0:
#             print('!', coor_t[0], coor_t[1], "\n")
#             sys.stdout.flush()
#             break

# import math
# import random
# import sys
#
#
# def Dist(x, y, x_guess, y_guess):
#     return int(abs(x - x_guess) + abs(y - y_guess))
#
# x, y = 0, 0
# print("?", x, y, "\n")
# sys.stdout.flush()
# dist = int(input())
# if dist == 0:
#     print('!', x, y, "\n")
#     sys.stdout.flush()
# x2_pos, y2 = dist, 0
# x2_neg = -dist
#
# print("?", x2_pos, y2, "\n")
# sys.stdout.flush()
# dist_pos = int(input())
#
# print("?", x2_neg, y2, "\n")
# sys.stdout.flush()
# dist_neg = int(input())
#
# if dist_pos < dist_neg:
#     x3 = int((dist + dist - dist_pos) / 2)
#     y3 = int((dist + dist_pos - dist) / 2)
#     print("?", x3, y3, "\n")
#     sys.stdout.flush()
#     dist_check = int(input())
#     if dist_check == 0:
#         print('!', x3, y3, "\n")
#         sys.stdout.flush()
#     else:
#         print('!', x3, -y3, "\n")
#         sys.stdout.flush()
# else:
#     x3 = -int((dist + dist - dist_neg) / 2)
#     y3 = -int((dist + dist_neg - dist) / 2)
#     print("?", x3, y3, "\n")
#     sys.stdout.flush()
#     dist_check = int(input())
#     if dist_check == 0:
#         print('!', x3, y3, "\n")
#         sys.stdout.flush()
#     else:
#         print('!', x3, -y3, "\n")
#         sys.stdout.flush()


import math
import random
import sys

x1, y1 = int(1e6), int(1e6)
x2, y2 = int(-1e6), int(1e6)
print("?", x1, y1, "\n")
sys.stdout.flush()
d1 = int(input())
print("?", x2, y2, "\n")
sys.stdout.flush()
d2 = int(input())
if d1 < d2:
    x = (d2 - d1)/2
    y = d1 - abs(x1 - x)
    if y > 1e6:
        y -= 1e6
        y *= -1
    else:
        y = y1 - y
else:
    x = -(d1 - d2)/2
    y = d2 - abs(x2 - x)
    if y > 1e6:
        y -= 1e6
        y *= -1
    else:
        y = y2 - y
print("!", int(x), int(y), "\n")
sys.stdout.flush()
