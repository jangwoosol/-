def solution(numbers, target):
    all=[0]
    cnt=0
    for i in numbers:
        result=[]
        for j in all:
            result.append(j+i)
            result.append(j-i)
        all=result
    for i in all:
        if i==target:
            cnt+=1
    return cnt