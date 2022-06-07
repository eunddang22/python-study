a,b = map(int,input().split())
a_1 = int(str(a)[::-1])
b_1 = int(str(b)[::-1])
if a_1>b_1:
    print(a_1)
else:
    print(b_1)