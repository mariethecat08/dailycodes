"""
    how to solve (초안)
    1. 입력받은 단어 word를 sort하여 가장 앞 두문자를 변수 std1, std2에 저장한다.
    2. std1와 std2가 word에서 각각 몇번째 인덱스에 있는지 확인하여 std1, std2에 새로 저장한다.
    3. word에서 인덱스 0부터 (min(std1,std2)+1) 까지 슬라이싱하여 뱐수 one에 저장한다.
    4. word에서 인덱스 (min(std1,std2)+1) 부터 (max(std1,std2)+1)까지 슬라이싱 하여 변수 two에 저장한다.
    5. word에서 인덱스 (max(std1,std2)+1)부터 끝까지 슬라이싱하여 변수 three에 저장한다.
    6. 세 변수 one, two, three를 one[::-1]와 같이 다시 저장한다.
    7. "".join()을 활용하여 세 변수를 다시 하나의 문자열로 합친다.
"""

word = input()
result = 'z' * len(word)
for i in range(len(word)):
    one = word[:i+1][::-1]
    for j in range(i+1,len(word)-1):
        two = word[i+1:j+1][::-1]
        three = word[j+1:][::-1]
        result = min(result, (one+two+three))
print(result)

#dcaaaba
#>>>aaacdba

#bcaaaba
#>>>aaacbba

#cadacaca
#>>>acacadac

#cba
#>>>cba