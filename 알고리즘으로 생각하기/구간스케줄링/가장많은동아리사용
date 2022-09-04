a=[['wldur',8,13],['tj',9,11],['xh',10,12],['qk',11,14],['ans',13,16],['ehr',14,15],['tk',15,17]]
a.sort(key=lambda i : i[2]) #종료시간을 기준으로 정렬 
s=[a[0]]
i=0
for j in range(1,len(a)):
  if a[j][1]>=a[i][2]: #동아리시작시간이 직전에 동아리가 끝나는시간보다 크면 s에 추가.
    s.append(a[j])
    i=j
print(s)
