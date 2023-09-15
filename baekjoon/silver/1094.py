pole = int(input())
n = 64
count = 0
while pole != 0:
    if pole < n:
        n /= 2
    else:
        count += 1
        pole -= n
print(count)
