def binary_search(start, end, target, total_list):
    while start <= end:
        mid = (start + end) // 2

        if total_list[mid] == target:
            print("yes", end = ' ')
            return
        elif total_list[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    print("no", end = ' ')

n = int(input())
total_list = list(map(int, input().split()))
total_list.sort()
m = int(input())
search_list = list(map(int, input().split()))

for x in search_list:
    binary_search(0, len(total_list) - 1, x, total_list)