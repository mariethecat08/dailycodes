import math

def fac(x):
    return math.factorial(x)

count = int(input())
for i in range(count):
    n, m = list(map(int, input().split()))
    print(fac(m)//(fac(n)*fac(m-n)))