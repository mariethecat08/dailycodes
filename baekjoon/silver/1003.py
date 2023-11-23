from collections import deque

n = int(input())
for _ in range(n):
    cal = deque([[1, 0], [0, 1]])
    num = int(input())
    if num == 0 or num == 1:
        print(*cal[num])
    else:
        for _ in range(num - 1):
            cal.append([cal[0][0] + cal[1][0], cal[0][1] + cal[1][1]])
            cal.popleft()
        print(*cal[1])
