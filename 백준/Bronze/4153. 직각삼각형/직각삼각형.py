# 몇개가 입력되는지 알 수 없기에 while true 쓰고 break으로 반복문 만듬
while True:
  a=list(map(int, input().split()))
  if sum(a)==0:
    break
  maxx=max(a)
  a.remove(maxx) # 가장 큰 값을 제거
  if a[0]**2+a[1]**2==maxx**2:
    print('right')
  else:
    print('wrong')