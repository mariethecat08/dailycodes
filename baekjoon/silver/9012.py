n = int(input())
for _ in range(n):
    cnt = 0
    ps = list(input())
    for s in ps:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            cnt += 1000
            break
    if cnt == 0 :
        print("YES")
    else:
        print("NO")
