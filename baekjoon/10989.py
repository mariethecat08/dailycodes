from collections import defaultdict
num_dict = defaultdict(lambda : 0)
N = int(input())

for i in range(N):
    number = int(input())
    num_dict[number] += 1

nums = list(num_dict.keys())
nums.sort()
sorted_dict = {i : num_dict[i] for i in nums}

for num in nums:
    cnt = num_dict[num]
    for i in range(cnt):
        print(num)