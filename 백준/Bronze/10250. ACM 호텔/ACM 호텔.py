a = int(input())

for i in range(a):
    h, w, n = map(int, input().split())
    num = n//h + 1 #호 수
    floor = n % h # 객실 층
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')