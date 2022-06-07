n = []
n1 = []
for i in range(10):
    n.append(int(input()))

for i in range(len(n)):
    n1.append(n[i]%42)

print(len(set(n1)))


