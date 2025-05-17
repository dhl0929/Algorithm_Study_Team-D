n = int(input())
array = [int(input()) for _ in range(n)]


result = []
for i in array:
    if i != 0 :
        result.append(i)
    else:
        result.pop()
print(sum(result))