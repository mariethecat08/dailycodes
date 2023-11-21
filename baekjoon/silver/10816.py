import sys
from collections import Counter

n1 = input()
nums1 = list(map(float, sys.stdin.readline().split()))
nums1 = sorted(nums1)
count = Counter(nums1)


n2 = int(input())
nums2 = list(map(float, sys.stdin.readline().split()))
result = [count[n] for n in nums2]

# result = [0] * len(nums2)
# for num in nums2:
#     cnt = 0
#     for i in range(len(nums1)):
#         if num < nums1[i]:
#             nums1 = nums1[i:]
#             break
#         if nums1[i] == num:
#             cnt += 1
#     result[nums2_dict[num]] = cnt

print(*result)
