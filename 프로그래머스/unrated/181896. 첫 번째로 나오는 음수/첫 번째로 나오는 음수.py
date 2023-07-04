def solution(num_list):
    a=[]
    for i in num_list:
        if i<0:
            a.append(num_list.index(i))
    if len(a)==0:
        return -1
    else:
        return a[0]