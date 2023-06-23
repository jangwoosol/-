def possible(answer):
    for x,y,a in answer:
        if a==0 : #설치된 것이 기둥일 경우
            # 바닥 위 또는 보의 한쪽 끝 부분 위 또는 다른 기둥 위
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif a==1:
            #보는 한쪽 끝 부분이 기둥 위 혹은 양쪽 끝 부분이 다른 보와 동시에 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True
def solution(n, build_frame):    
    answer = []
    for frame in build_frame: # 작업 수는 쵣 1000개
        x,y,a,b =frame
        if b==0: #삭제하는 경우
            answer.remove([x,y,a])
            if not possible(answer): # 가능하면
                answer.append([x,y,a])
        if b==1: # 설치하는 경우
            answer.append([x,y,a])
            if not possible(answer): 
                answer.remove([x,y,a])
    return sorted(answer)
                