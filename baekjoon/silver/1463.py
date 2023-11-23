n = int(input())

cnt = 0
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    while True:
        if n == 1:
            print(cnt)
            break
        if n % 3 == 0:
            n /= 3
            cnt += 1
        else:
            n -= 1
            cnt += 1
            if n % 3 != 0 and n % 2 == 0:
                n /= 2
                cnt += 1
