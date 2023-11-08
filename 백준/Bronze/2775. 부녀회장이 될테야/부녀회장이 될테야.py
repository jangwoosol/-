for t in range(int(input())): 
    k= int(input().rstrip()) # 층 입력받음
    n = int(input().rstrip()) # 호 입력받음
    arr = [num for num in range(1, n+1)] # 0층에 사는 친구
    for i in range(k):
        new = [] # 값 담아줄 임시 저장소
        for j in range(n):
            new.append(sum(arr[:j+1])) # n호까지의 합을 더하여 new에 추가
        arr= new.copy() # arr로 반환해줌 위 과정을 k층까지 반복
    print(arr[-1]) # k층의 n호 값 출력
