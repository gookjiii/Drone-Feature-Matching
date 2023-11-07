from collections import defaultdict

nums = [1,1,1,1]
dict = {i:nums[i] for i in range(len(nums))}
d = defaultdict(list)
for k, v in dict.items():
    d[v].append(k)
sum = 0
for v in d.values():
    sum += int((len(v) * (len(v) - 1))/2)
print(sum)
