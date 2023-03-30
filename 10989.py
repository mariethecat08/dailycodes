from collections import defaultdict
n = int(input())
numbers = defaultdict(lambda : 0)

for _ in range(n):
    num = input()
    numbers[num] += 1

sort_nums = sorted(numbers.keys())

for n in sort_nums:
    for cnt in range(int(numbers[n])):
        print(n)