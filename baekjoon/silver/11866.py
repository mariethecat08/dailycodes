from collections import deque
N, K = map(int, input().split())
circle = deque(range(1, N+1))

result = []
for _ in range(N):
    circle.rotate(-K)
    result.append(circle.pop())
print(f"<{str(result)[1:-1]}>")
