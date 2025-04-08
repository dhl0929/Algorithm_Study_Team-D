n = int(input())

target = 0
num = 0
while True:
    if '666' in str(num):
        target += 1
    if target == n:
        print(num)
        break
    num += 1
