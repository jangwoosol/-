# 고정비용이 아무리 크더라도 c가 b보다 크다면 손익분기점을 넘길 수 있다. b>c인 경우 손익분기점이 존재하지 않는다.
a,b,c=map(int,input().split())
if b>=c :
  print(-1)
else :
  print(a//(c-b)+1) #소수점 나오는거 없애기 위해 몫으로 구한다.