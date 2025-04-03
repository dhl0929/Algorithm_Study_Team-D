n, m = map(int, input().split())
tree_list = list(map(int, input().split()))
tree_list.sort()

def binary_search(start, end, target, tree_list):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        total_cut = 0
        for tree in tree_list:
            if tree > mid:
                total_cut += (tree - mid)

        if total_cut >= target:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

print(binary_search(0, tree_list[-1], m, tree_list))