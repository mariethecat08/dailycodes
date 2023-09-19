n = int(input()) # 입력받을 단어 수를 변수 n에 저장한다.
cnt = 0 # 그룹 단어를 셀 변수 cnt이다.

for _ in range(n): # n만큼 반복한다.
    word = input()
    answer = len(set(word)) # 단어의 문자 개수이다.
    
    tmp = word[0]
    diff = 1 # 단어의 각 문자를 하나씩 확인하면서 문자 종류가 바뀔 때마다 변수 diff가 하나씩 오를 것이다.
                # 첫 문자가 tmp에 저장되었으므로, 공백에서 tmp로 바뀌었다. 
                # 첫번째 문자를 확인한 순간부터 diff는 하나 증가한 것이다.
    
    for w in word: # 입력받은 단어의 문자를 하나씩 확인한다.
        if tmp != w: # 이전 문자와 현재 문자 w가 서로 다르면 문자가 바뀌었으므로, diff를 1 증가시킨나.
            diff += 1
        tmp = w # 다음 문자를 확인하기 위해 tmp에 w를 저장한다.
    if answer == diff: # 문자가 바뀐 횟수가 문자 종류 개수와 같다면 해당 단어는 그룹 단어이다.
        cnt += 1
print(cnt)