def solution(n, m, section):
    result=1 
    paint=section[0]
    for i in range(1,len(section)):
        if section[i]-paint>=m:
            result+=1
            paint=section[i]
    return result