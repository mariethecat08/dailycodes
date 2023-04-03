import sys
input = sys.stdin.readline

N = int(input())
nums_vec = [0 for _ in range(10001)]
for _ in range(N):
    number = int(input())
    nums_vec[number] += 1

num = 0
while(N != 0):
    if nums_vec[num] != 0:
        cnt = nums_vec[num]
        for _ in range(cnt):
            print(num)
        N -= cnt
    num += 1
        



# num = 0
# while (sum(nums_vec) != 0):
#     if nums_vec[num] != 0:
#         cnt = nums_vec[num]
#         nums_vec[num] = 0
#         for _ in range(cnt):
#             print(num)
#     num += 1