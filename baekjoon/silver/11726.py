n = int(input())
cases = [1, 2]
if n <= 2:
    print(n)
else:
    for i in range(2, n):
        cases.append(cases[i - 2] + cases[i - 1])
    print(cases[-1] % 10007)
