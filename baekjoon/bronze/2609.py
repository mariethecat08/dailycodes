def get_divisor(x):
    div = []
    n = 2
    while (True):
        tmp = x
        cal = tmp%n
        if tmp == 1.0:
            break
        if cal == 0:
            tmp = cal/n
            div.append(n)
            n = 2
        else:
            n += 1
    return div
        
def get_gcd(a, b):
    tmp_set = set(set(a)+set(b))
    result = 0
    for n in tmp_set:
        result += n**(max(a.count(n), b.count(n)))
    return result

def get_lcm(a,b):
    tmp_set = set(set(a)+set(b))
    result = 0
    for n in tmp_set:
        minimum = min(a.count(n), b.count(n))
        if minimum == 0:
            continue
        else:
            result += n**(minimum)
    return result
    
#n = int(input())
print(get_divisor(2))