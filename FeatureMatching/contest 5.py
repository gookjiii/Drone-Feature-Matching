# st = input()
# res = ''
#
# for i in range(len(st)):
#     if (i % 2 == 0):
#         res += st[i].lower()
#     else:
#         res += st[i].upper()
#
# print(res)

# letter = list(str()) * 5
#
# letter = ['*   *', '*  **', '* * *', '**  *', '*   *']
#
# a = int(input())
# b = int(input())
#
# for i in range(a):
#     for row in letter:
#         for j in range(b):
#             print(row,end=' ')
#         print()
#     print()

# f = open('input.txt','r')
# st = f.readline()
# f.close()
#
# def isComplex(st):
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for ch in st:
#         flag1 = flag1 or ch.islower()
#         flag2 = flag2 or ch.isupper()
#         flag3 = flag3 or ch.isdigit()
#     return flag1 and flag2 and flag3
#
# def isRememmber(st):
#     return sum(c.isdigit() for c in st) <= 3 and len(st) <= 10
#
# f = open('output.txt','w')
#
# if isComplex(st):
#     f.write('YES\n')
# else:
#     f.write('NO\n')
#
# if isRememmber(st):
#     f.write('YES')
# else:
#     f.write('NO')
#
# f.close()

# f = open('input.txt','r')
# lines = f.readlines()
# f.close()
#
# def isFile(st):
#
#     flag1 = False
#     for ch in st:
#         flag1 = flag1 or ch.isupper()
#     return (not flag1) and (st.endswith('.hlm') or st.endswith('.brhl') or st.endswith('.hlm.') or st.endswith('.brhl.')) and (not st.startswith('.'))
# f = open('output.txt','w')
#
# for line in lines:
#     message = line
#     words = message.split()
#     for word in words:
#         if isFile(word):
#             if word[-1] == '.':
#                 f.write(word[:-1] + '\n')
#             else:
#                 f.write(word + '\n')
#
# f.close()

f = open('input.txt','r')
lines = f.readlines()
f.close()
f = open('output.txt','w')
lines[-1] += '\n'

for line in lines:
    words = line[:-1].split('\t')
    left_aligned = words[0][:7]
    right_aligned = words[-1]
    f.write("{:<}{:.>73}".format(left_aligned,right_aligned) + '\n')

f.close()

# import re
#
# file1 = open('input.txt', 'r')
# Lines = file1.readlines()
#
# out = []
# for lines in Lines:
#     for file in lines.split():
#         # if file.endswith('.hlm','.hlm.','.brhl','.brhl.'):
#
#         match = re.search('[a-z0-9]\.hlm$', file) or re.search('[a-z0-9]\.brhl$', file) \
#                  or re.search('[a-z0-9]\.brhl\.$', file) or re.search('[a-z0-9]\.hlm\.$', file)
#
#         if match:
#             if file[0] != '.':
#                 out.append(file)
#
# file1 = open('output.txt', 'w')
#
# for lines in out:
#     if lines[-1].isalpha():
#         file1.writelines(lines+'\n')
#     else:
#         file1.writelines(lines[:-1] + '\n')
# file1.close()