k, n = map(int, input().split())
total_list = [int(input()) for i in range(k)]
total_list.sort()

def binary_search(start, end, total_list, target):
    lst = []

    while start <= end:
        mid = (start + end) // 2
        result = 0
        for i in total_list:
            result += (i // mid)
        
        if result >= target:    # 오른쪽으로 이동
            start = mid + 1
            lst.append(mid)

        elif result < target:   # 왼쪽으로 이동
            end = mid - 1
    return max(lst)

print(binary_search(1, total_list[-1], total_list, n))