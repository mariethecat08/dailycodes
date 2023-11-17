n1 = input()
nums = sorted(map(int, input().split()))
n2 = input()
inputs = map(int, input().split())

for n in inputs:
    if n in nums:
        print(1)
    else:
        print(0)
