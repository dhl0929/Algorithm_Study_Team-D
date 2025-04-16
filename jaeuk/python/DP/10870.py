x = int(input())
d = [0] * (x + 1)

# bottom-up
d = [0] * 21
d[1] = 1

for i in range(2, x + 1):
    d[i] = d[i-1] + d[i-2]
print(d[x])

# top-down
# d[1] = 1

# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
# print(fibo(x))


