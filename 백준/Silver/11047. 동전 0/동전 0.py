a,b=map(int, input().split())
coin=[]
for i in range(a):
  coin.append(int(input()))

coin=sorted(coin,reverse=True)
count=0
for i in coin:
  count+=b//i
  b%=i
print(count)