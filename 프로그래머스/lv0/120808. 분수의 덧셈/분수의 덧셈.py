def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

def solution(numer1, denom1, numer2, denom2):
    up= (numer1*denom2)+(numer2*denom1)
    down=denom1*denom2
    value=gcd(up,down)
    answer=[up/value,down/value]
    return answer