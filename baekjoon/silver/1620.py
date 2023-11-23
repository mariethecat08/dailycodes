N, M = map(int, input().split())
dogam_num = {}
dogam_str = {}
for i in range(N):
    name = input()
    dogam_num[str(i + 1)] = name
    dogam_str[name] = str(i + 1)
for _ in range(M):
    question = input()
    if question[0] in "0123456789":
        print(dogam_num[question])
    else:
        print(dogam_str[question])
