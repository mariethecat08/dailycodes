import sys
n = int(sys.stdin.readline().strip())  # 입력받을 횟수를 n에 저장.
spec = [] # 몸무게와 키 정보를 저장할 리스트를 정의한다.
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())  # weight와 height를 int로 변환하여 각각 w,h에 저장한다.
    spec.append((w, h))  # 각 w,h를 리스트 spec에 추가한다.

result = [0]*n  # 메모리를 줄이기 위해 리스트의 사이즈를 정의한다.
for i in range(n):
    cnt = 1  # 등수는 본인보다 큰 덩치 수 + 1 이므로 cnt를 0이 아닌 1로 저장해둔다.
    tmp = spec[i]
    for j in range(n):
        if tmp[0] < spec[j][0] and tmp[1] < spec[j][1]:  # 몸무게와 키가 모두 본인보다 큰 학생 수를 센다.
            cnt += 1
    result[i] = cnt
print(*result)x
