n ,m = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(m):
    cards.sort()
    cards[0], cards[1] = sum(cards[:2]), sum(cards[:2])
print(sum(cards))
