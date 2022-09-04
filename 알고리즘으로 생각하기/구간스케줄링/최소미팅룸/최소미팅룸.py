a=[['wldur',8,13],['tj',9,11],['xh',10,12],['qk',11,14],['ans',13,16],['ehr',14,15],['tk',15,17]]
a.sort(key=lambda i : i[1]) #시작시간을 기준으로 정렬 
solution=[[a[0]]] #가장 일찍 시작하는 동아리
finish=[a[0][2]] 
k=0 #미팅룸
for i in range(1,len(a)):
  flag=False #기존의 미팅룸에 배정 가능하면 true로 바뀜
  # 현재 동아리 a[i]를 미팅룸 j에 배정하고 j미팀룽 종료시각 갱신
  for j in range(k+1):
    if a[i][1]>finish[j]:
      solution[j].append(a[i])
      finish[j]=a[i][2]
      flag=True
      break
  #a[i]를 새 미팅룸에 배정
  if not flag:
    k+=1
    solution.append([a[i]])
    finish.append(a[i][2])

for i in range(k+1):
  print('미팅룸',i+1, ':', solution[i])
