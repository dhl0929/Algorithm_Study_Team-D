n = int(input())

result = 0

while n >= 0:
    if n % 5 == 0:
        result += (n // 5)
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)


# 5로 한번에 나눠지는 경우
# 3, 5 조합으로 나눠지는 경우
# 3으로 나눠지는 경우
# 다 안됨