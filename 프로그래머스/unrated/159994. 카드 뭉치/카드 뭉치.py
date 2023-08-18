def solution(cards1, cards2, goal):
    answer='Yes'
    c1, c2= 0,0
    for word in goal:
        if len(cards1) > c1 and word==cards1[c1]:
            c1+=1
        elif len(cards2) > c2 and word==cards2[c2]:
            c2+=1
        else:
            answer='No'


    return answer