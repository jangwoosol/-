a=int(input())
p=1 # 벌집의 개수, 1개부터 시작
c=1 # 방 개수, 1개부터 시작
while a>p:
  p+=6*c  # 벌집이 6의 배수로 증가
  c+=1
print(c)