n = int(input())
found = False

for i in range(max(1, n - len(str(n)) * 9), n):
    result = sum(map(int, str(i))) + i
    if result == n:
        print(i)
        found = True
        break
if not found:
    print(0)