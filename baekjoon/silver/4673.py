def separator(x):
    """_summary_

    Args:
        x (int): 각 자리수를 따로 계산하고 싶은 integer
        
    Returns:
        int : 각 자리수를 합한 integer
    """
    a = x//1000 # x의 천의 자리 수
    b = (x - a*1000) // 100 # x의 백의 자리 수
    c = (x - a*1000 - b*100) // 10 # x의 십의 자리 수
    d = x % 10 # x의 일의 자리 수
    return a+b+c+d # 각 자리 수의 합

origin = set(list(range(1,10001))) # 1에서 10000 사이의 모든 정수
                                    # 전체 origin에서 집합의 차의 연산과 여집합을 이용하여 생성자가 없는 셀프 넘버만 추출해낼 것이다.
ops = []
for n in range(1, 10000):
    ops.append(separator(n)+n) # separator로 각 자리 수를 합하고, 해당 수를 더하여 d(n)을 계산한다.
    
ops = set(ops)
result = sorted(list(origin - ops)) #셀프 넘버를 구한다.
for n in result:
    print(n)