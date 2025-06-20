n = int(input())
cnt = 0
for hour in range(n + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in str(second) or '3' in str(minute) or '3' in str(hour):
                cnt += 1
print(cnt)