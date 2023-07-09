def solution(n):
    a= list(str(n))
    answer=[]
    for i in range(len(a)-1,-1,-1):
        answer.append(int(a[i]))
    
    return answer