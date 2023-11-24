n = int(input())
num = [0] * (n + 1)
# 리스트 num은 각 원소가 해당 인덱스의 최소 계산 횟수를 의미한다.
# 예를 들어 num[10]은 10의 최소 계산 횟수가 3이므로 num[10]=3이 된다.
for i in range(2, n + 1):
    num[i] = num[i - 1] + 1  # 1을 빼는 경우
    if i % 3 == 0:  # 3으로 나누는 경우
        num[i] = min(num[i], num[i // 3] + 1)  # 1을 뺸 경우와 3으로 나눈 경우 중 더 작은 값을 저장한다.
    if i % 2 == 0:  # 2로 나누는 경우
        num[i] = min(num[i], num[i // 2] + 1)
print(num[n])
