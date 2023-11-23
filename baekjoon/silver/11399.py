n = int(input())
time = sorted(map(int, input().split()))
result = 0
for i in range(n):
    result += sum(time[: i + 1])
print(result)
