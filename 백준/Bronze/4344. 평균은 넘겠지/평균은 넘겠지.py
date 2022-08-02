a=int(input())
for i in range(a):
  c=list(map(int, input().split()))
  mean=sum(c[1:])/c[0]
  score=0
  for j in c[1:]:
    if j>mean:
      score+=1
    rate=score/c[0]*100
  print('{0:0.3f}%'.format(rate))