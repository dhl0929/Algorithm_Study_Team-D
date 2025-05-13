n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

array = list(a-b)

if len(array) == 0:
    print(0)
else:
    array.sort()
    print(len(array))
    for i in array:
        print(i, end = ' ')