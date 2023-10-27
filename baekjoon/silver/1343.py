board = input()  # "X"와 "."로 이루어진 string 타입의 보드를 입력받는다.
n = 0  # "X"가 몇 번 연속해서 나오는지 셀 때 사용할 변수이다.
result = ""  # 마지막에 출력할 string을 저장한다.
for i in range(len(board)):  # 입력받은 board의 문자를 하나씩 확인한다.
    if board[i] == "X":  # 만약 현재 문자가 "X"라면 n을 하나 더한다.
        n += 1
    else:  # "X"가 아닌 "."이라면 n을 세는 것을 멈춘다.
        if n % 2 == 0:  # 지금까지 연속적으로 나온 "X"의 수가 짝수라면 폴리오미노로 덮을 수 있다.
            result += (("AAAA")*(n//4) + ("B")*(n%4))
            n = 0  # 폴리오미노로 "X"를 모두 덮었으니, 다시 n을 0으로 초기화시킨다.
            result += "."
        else:
            result = -1  # 지금까지 연속적으로 나온 "X"의 수가 홀수라면 폴리오미노로 덮을 수 없다.
            break  # for문을 중단시킨다.
    if (i+1) == len(board): # 만약 현재 인덱스가 마지막 인덱스일 때.
        if n % 2 == 0: # n이 짝수라면 폴리오미노로 덮는다.
            result += (("AAAA")*(n//4) + ("B")*(n%4))
        else:
            result = -1
print(result)
