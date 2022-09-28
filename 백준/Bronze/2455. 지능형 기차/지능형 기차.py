on=[]
people=0
for i in range(4):
  a,b=map(int,input().split())
  people-=a
  people+=b
  on.append(people)
print(max(on))