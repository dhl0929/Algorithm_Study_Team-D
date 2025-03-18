n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(len(a)):
    a_min = min(a)
    b_max = max(b)

    a.remove(a_min)
    b.remove(b_max)

    result += (a_min * b_max)

print(result)