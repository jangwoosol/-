def solution(players, callings):
    # 선수위치
    p_idx={i: player for i,player in enumerate(players)}
    race={ player : i for i,player in enumerate(players)}
    for i in callings:
        loc=race[i] #현재등수
        loc2=loc-1 #앞 등수
        i2=p_idx[loc2]
        # 앞선수랑 바꾸기
        p_idx[loc]=i2
        p_idx[loc2]=i
        # 앞등수랑 바꾸기
        race[i]=loc2
        race[i2]=loc
    return list(p_idx.values())