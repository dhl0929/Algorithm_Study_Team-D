from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))


sum_set = set(sum(combo) for combo in combinations(cards, 3))

print(max([x for x in sum_set if x <= m]))