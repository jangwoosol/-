def solution(num_list):
    hole = ""
    chak=""
    for i in num_list:
        if i%2==1:
            hole+=str(i)
        else:
            chak+=str(i)
    
    return int(hole)+int(chak)