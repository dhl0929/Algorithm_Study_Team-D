from sys import stdin

N = stdin.readline().rstrip()

for i in range(int(N)):
    numbers = str(i)
    generator = sum(list(map(int,numbers))) + int(numbers)
    if generator == int(N):
        print(i)
        break
else:
    print(0)