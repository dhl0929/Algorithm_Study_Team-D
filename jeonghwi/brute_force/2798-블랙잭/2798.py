from itertools import combinations
from sys import stdin

#stdin = open("input.txt","r")

N, M = map(int,stdin.readline().split())

cards = list(map(int,stdin.readline().split()))

max_sum = 0
for combs in combinations(cards,3):
    sum_combs = sum(combs)
    if M-sum_combs < 0:
        continue
    max_sum = max(sum_combs,max_sum)

print(max_sum)