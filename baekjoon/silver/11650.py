n = int(input())
coor = []  # 좌표들을 저장할 리스트를 정의한다.
for _ in range(n):
    x, y = input().split()  # 좌표들을 입력받을 때, 공백을 기준으로 x와 y로 분류하여 저장한다.
    coor.append((int(x), int(y)))  # 입력받은 x와 y를 하나의 집합으로 리스트에 추가한다.
coor = sorted(coor)  # 리스트를 정렬하면, 문제의 조건에 맞게 x 기준으로 먼저 정렬 후 y순으로 정렬된다.
for i in range(n):
    print(f"{coor[i][0]} {coor[i][1]}")
