from collections import Counter

lst = list(map(int, input()))
dic = dict(Counter(lst))

tmp = 0
result = []
for key, value in dic.items():
    if key == 6 or key == 9:
        tmp += dic[key]
        continue
    result.append(value)

if tmp % 2 ==0:
    result.append(tmp // 2)
else:
    result.append(tmp // 2 + 1)

print(max(result))