#1
# code = input()
#
# Greek = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa"]
# def romanToInt(S: str) -> int:
#     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     summ = 0
#     for i in range(len(S) - 1, -1, -1):
#         num = roman[S[i]]
#         if 3 * num < summ:
#             summ = summ - num
#         else:
#             summ = summ + num
#     return summ
#
# coor = code.split('_')
# print(Greek.index(coor[0]) + 1, romanToInt(coor[1]))

#2
# str = input()
# print(len(set(str)) < len(str))

# 3
# str = input()
# N = int(input())
# tmp = [str[idx: idx + N] for idx in range(len(str) - N + 1)]
# d=dict()
# for i in tmp:
#     d[i]=str.count(i)
# res = [key for key, val in d.items() if val >= 2]
# res.sort()
# print(res)


# class Sol():
#     def __init__(self, n):
#         self.n = n
#
#     def Count(self,remain, last_pos, i, arg , total):
#         if remain == 0:
#             arg[total] += 1
#         elif i <= self.n:
#             if last_pos < i - 1:
#                 self.Count(remain - 1, i, i + 1, arg, total)
#             self.Count(remain, last_pos, i + 1, arg, total)
#         else:
#             return
#
#     def Get(self):
#         sum = [0] * 20
#         res = 2 ** self.n + self.n * (2 ** (self.n-1))
#         for i in range(2, self.n // 2 + 1 + (self.n % 2 == 1)):
#             self.Count(i,-1, 1, sum, i)
#             res += sum[i] * (2 ** (self.n - i))
#         print(res)
#
# for i in range(1,21):
#     sol = Sol(i)
#     sol.Get()

# n = int(input())
# k = int(input())
# s = [set()] * (n + 1)
# for i in range(1,n + 1):
#     s[i] = set(map(int,input().split()))
# fault = set(map(int,input().split()))
# res = [0] * (10**6)
# res[0] = -1
# for wire in fault:
#     res[wire] = -1
# for connector in s:
#     for wire in connector:
#         if res[wire] != -1:
#             res[wire] = res[wire] + 1
# res.sort(reverse=True)
# Res = []
# for i in range(k):
#     if res[i] != -1:
#         Res.append(res[i])
# Res.sort()
# print(*Res[:k], sep = '\n')

# class Graph:
#
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = []
#
#     def addEdge(self, u, v, w):
#         self.graph.append([u,v,w])
#
#     def find(self, parent, i):
#         if parent[i] == i:
#             return i
#         return self.find(parent, parent[i])
#
#     def union(self, parent, rank, x, y):
#         xroot = self.find(parent, x)
#         yroot = self.find(parent, y)
#
#         if rank[xroot] < rank[yroot]:
#             parent[xroot] = yroot
#         elif rank[xroot] > rank[yroot]:
#             parent[yroot] = xroot
#         else:
#             parent[yroot] = xroot
#             rank[xroot] += 1
#
#     def KruskalMST(self):
#         result = []
#         i = 0
#         e = 0
#         self.graph = sorted(self.graph, key=lambda item:item[2])
#         parent = []
#         rank = []
#         for node in range(self.V):
#             parent.append(node)
#             rank.append(0)
#
#         while e < self.V - 1:
#             u, v, w = self.graph[i]
#             i = i + 1
#             x = self.find(parent, u)
#             y = self.find(parent, v)
#             if x != y:
#                 e = e + 1
#                 result.append([u, v, w])
#                 self.union(parent, rank, x, y)
#         minimunCost = 0
#         for u, v, w, in result:
#            minimunCost += w
#         print(minimunCost)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     g = Graph(n + 1)
#     for i in range(n):
#         adj = list(map(int, input().split()))
#         j = -1
#         for w in adj:
#             j += 1
#             if i < j:
#                 g.addEdge(i,j,w)
#     adj = list(map(int, input().split()))
#     i = -1
#     for w in adj:
#         i += 1
#         g.addEdge(i, n, w)
#     g.KruskalMST()

# str = input()
# N = int(input())
# print(sorted([key for key, val in {str[idx: idx + N]:str.count(str[idx: idx + N]) for idx in range(len(str) - N + 1)}.items() if val >= 2]))
