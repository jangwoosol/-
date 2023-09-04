import itertools
def solution(number):
    num=itertools.combinations(number, 3)
    result=0
    for i in list(num):
        if sum(i)==0:
            result+=1
    return result
            
