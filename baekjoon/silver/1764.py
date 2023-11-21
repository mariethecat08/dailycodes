N, M = map(int, input().split())

not_listened = set([input() for _ in range(N)])
not_seen = set([input() for _ in range(M)])

result = sorted(not_listened & not_seen)
print(len(result))
print(*result, sep='\n')
