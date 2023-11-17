n1 = input()
nums1 = list(map(float, input().split()))
n2 = int(input())
nums2 = list(map(float, input().split()))
result = [nums1.count(n) for n in nums2]
print(*result)
