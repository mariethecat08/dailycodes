n = int(input())
judges = [input() for _ in range(n)]
judges1 = sorted([peo for peo in judges if peo[1]==' '], key=lambda x:x[0:1]) 
judges2 = sorted([peo for peo in judges if peo[2]==' '], key=lambda x:x[0:2])
judges3 = sorted([peo for peo in judges if peo[2] in '0123456789'], key=lambda x:x[0:3])
judges_re = judges1+judges2+judges3

print(*judges_re,sep='\n')