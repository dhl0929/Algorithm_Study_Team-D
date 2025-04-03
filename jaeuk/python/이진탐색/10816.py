from collections import Counter
m = int(input())
total_list = list(map(int, input().split()))
total_list.sort()
n = int(input())
search_list = list(map(int, input().split()))

# 이진 탐색
def binary_search(start, end, target, total_list, dic):
    while start <= end:
        mid = (start + end) // 2

        if total_list[mid] == target:
            print(dic[target], end = ' ')
            return 
        elif total_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    print(0, end=' ')

dic = dict(Counter(total_list))
for i in search_list:
    binary_search(0, len(total_list) - 1, i, total_list, dic)


# Counter 활용
# dic = dict(Counter(total_list))
# for i in search_list:
#     if i in dic.keys():
#         print(dic[i], end = ' ')
#     else:
#         print(0, end=' ')
