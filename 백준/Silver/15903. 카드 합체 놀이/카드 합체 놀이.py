n,m = map(int, input().split())
card=list(map(int, input().split()))
card.sort()
for i in range(m):
  k= card[0]+card[1]
  card[0]= k
  card[1]= k
  card.sort()
print(sum(card))