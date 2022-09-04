s=[1,4,7,13,26,64,125,260,550]
k=85
solution=[]
i=len(s)-1 #파이썬은 0부터 세니까
while k>0:
  if s[i]<=k:
    solution.append(s[i])
    k-=s[i]
  i-=1 #else: 생략과 마찬가지

print(solution)
