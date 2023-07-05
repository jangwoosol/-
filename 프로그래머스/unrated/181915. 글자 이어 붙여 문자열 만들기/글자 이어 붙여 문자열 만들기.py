def solution(my_string, index_list):
    answer=list(my_string)
    k=""
    for i in index_list:
        k+=str(answer[i])
    return k