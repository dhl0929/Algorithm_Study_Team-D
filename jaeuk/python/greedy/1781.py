import heapq
n = int(input())
table = [tuple(map(int, input().split())) for _ in range(n)]
table = sorted(table, key=lambda x: x[0])
print(table)
cup_ramen_heap = []

for problem in table:
    heapq.heappush(cup_ramen_heap, problem[1]) #problem[1]은 각 문제의 컵라면 개수
    print(cup_ramen_heap)


# for problem in table:
#     heapq.heappush(cup_ramen_heap, problem[1]) #problem[1]은 각 문제의 컵라면 개수
#     #이때 len(cup_ramen_heap)이 문제를 푸는데 걸리는 시간이라고 생각하는 것이 중요하다.
#     #1문제 풀때 시간이 1 흐르니까
#     if len(cup_ramen_heap) > problem[0]:#problem[0]은 각 문제의 데드라인
#     	#데드라인을 초과했을 때, 가장 컵라면을 적게 받는 문제를 제거
#         heapq.heappop(cup_ramen_heap)
#         #이렇게 되면 len(cup_ramen_heap)시간 내에 얻을 수 있는 가장 많은 양의 컵라면이 heapq에 담긴다.

# print((cup_ramen_heap))