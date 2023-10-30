n = int(input())
dasom = int(input())
candidates = [0]*50
for i in range(n-1):
    candidates[i] = int(input()) # 다솜이를 제외한 각 후보의 득표수를 리스트에 저장.

cnt = 0
while (True):
    candidates = sorted(candidates, reverse=True)
    if dasom > candidates[0]:
        break
    else:
        candidates[0] -= 1
        dasom += 1
        cnt += 1
print(cnt)
