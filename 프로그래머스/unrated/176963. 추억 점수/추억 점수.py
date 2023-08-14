def solution(name, yearning, photo):
    result =[]
    cnt=0
    for i in photo:
        cnt=0
        for j in i:
            if j in name:
                cnt += yearning[name.index(j)]
        result.append(cnt)
    return result