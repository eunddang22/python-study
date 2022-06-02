a = list(map(int,input().split()))
sum_a = 0
for i in range(5):
    sum_a += (a[i]**2)
trash_a = sum_a % 10
print(trash_a)