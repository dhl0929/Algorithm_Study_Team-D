n = int(input())
line = list(map(int, input().split()))
line.sort()
print(line)

result = 0
for i in range(1, len(line) + 1):
    result += sum(line[:i])
print(result)   