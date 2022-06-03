a = []
b = 1
for i in range(3):
    a.append(int(input()))
    b = b * a[i]
b = str(b)
c = {}
for i in range(10):
    c[i] = b.count(str(i))
    print(c[i])


