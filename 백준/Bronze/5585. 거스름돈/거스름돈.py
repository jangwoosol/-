a=1000-int(input())
mon=[500,100,50,10,5,1]
cnt=0
for i in mon:
  cnt+=a//i
  a=a%i
print(cnt)