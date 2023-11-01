def solution(a, b, n):
    answer = 0
    while n>=a:
        answer+=(n//a*b)
        n=(n%a)+(n//a*b) #교환하지 못하고 남은 병 +새로 얻은 콜라
    return answer