n = int(input())
table = list(map(int, input().split()))
d = table[:]

for i in range(n):
    for j in range(i):
        if table[i] > table[j]:
            d[i] = max(table[i] + d[j], d[i])

print(max(d))