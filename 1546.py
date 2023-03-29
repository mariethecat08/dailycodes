def new_score(num,high):
    return num/high*100

subject = int(input())
scores = list(map(int,input().split()))
highest = max(scores)

sum = 0
for i in range(subject):
    sum += new_score(scores[i],highest)
print(sum/subject)
