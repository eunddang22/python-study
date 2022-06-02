n = int(input())
score = list(map(int,input().split()))
max = max(score)
new_score=[]
for i in range(n):
    new_score.append((score[i]/max)*100)
sum_score = 0
for i in range(n):
    sum_score += new_score[i]
print(sum_score/n)










