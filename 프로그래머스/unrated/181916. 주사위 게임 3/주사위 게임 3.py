def solution(a, b, c, d):
    nums={a,b,c,d} #set으로 중복 제거
    count={}
    for i in (a,b,c,d):
        count[i]=count.get(i,0)+1
    if len(nums)==4:
        return min(nums)
    elif len(nums)==1:
        return 1111*nums.pop()
    elif len(nums) == 2:
        if 3 in count.values():
            p = [k for k, v in count.items() if v == 3][0]
            q = [k for k in nums if k != p][0]
            return (10 * p + q) ** 2
        else:
            p, q = count.keys()
            return (p + q) * abs(p - q)
    else:
        p = [k for k, v in count.items() if v == 2][0]
        q, r = [k for k in nums if k != p]
        return q * r

        

        