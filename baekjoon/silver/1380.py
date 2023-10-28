scenario = 0  # 시나리오 횟수
students = []  # 귀걸이를 돌려받지 못한 학생 명단
while (True):
    scenario += 1  # while문이 새로 돌 때마다 시나리오 횟수가 늘어난다.
    n = int(input())  # 학생 수를 입력받아 n에 저장한다.
    if n <= 0:  # 0을 입력받으면 while문을 중단시킨다.
        break
    name = []  # 현재 시나리오에 등장하는 학생들 이름 명단이다.
    for _ in range(n):  # 학생 수만큼 반복하며 리스트 name에 학생 이름을 저장한다/
        name.append(input())
    records = {n:0 for n in name}  # 딕셔너리 records의 key값에 학생들의 이름을 저장한다.
    for _ in range((2*n)-1):
        records[name[int(input().split()[0])-1]] += 1  # for문을 돌며 학생의 번호가 나올 때마다
                                                        # 해당 학생 번호의 value에 1을 더한다.
    number = list(records.values()).index(1)  # records의 values를 리스트로 변환한 후, 1인 인덱스를 찾는다.
    students.append(str(scenario)+" "+name[number])  # 값이 1이었던 인덱스를 활용해, 해당 학생의 이름을 저장한다.
for s in students:
    print(s)
