n = int(input())

for _ in range(n):
    num = int(input())
    cases = [0, 1, 2, 4]
    if num <= 3:
        print(cases[num])
    else:
        for i in range(4, num + 1):
            cases.append(cases[i - 3] + cases[i - 2] + cases[i - 1])
        print(cases[num])
