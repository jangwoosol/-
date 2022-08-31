n = int(input())
 
data = [] # 입력받은 정보를 저장할 리스트 
sor = [] # 등수정보를 저장할 리스트 
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) # 몸무게와 키를 합침
 
for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 셈
            count += 1 
    sor.append(count + 1) # 덩치 등수는 자신보다 몸무게 키 모두 큰 사람의 수 + 1 이므로 count + 1을 sor에 합한다.
 
for d in sor:
    print(d,end=" ")
