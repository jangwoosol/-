from itertools import permutations
def solution(n, weak, dist):
    length= len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer=len(dist) +1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
    #0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt=1 #투입할 친구
            # 해당 친구가 첨검할 수 있는 마지막 위치
            position=weak[start] + friends[cnt-1]
            #시작점부터 모든 취약 지점을 확인
            for index in range(start,start+length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position<weak[index]:
                    cnt+=1 # 새로운 친구를 투입
                    if cnt>len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position=weak[index]+friends[cnt-1]
            answer=min(answer,cnt) #최솟값 계산
    if answer> len(dist):
        return -1
    return answer
            
    answer = 0
    return answer