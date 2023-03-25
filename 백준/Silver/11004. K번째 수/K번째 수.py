n,m = map(int, input().split())
card=list(map(int, input().split()))
card.sort()
print(card[m-1])