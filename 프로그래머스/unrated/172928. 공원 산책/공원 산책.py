def solution(park, routes):
    x,y=0,0
    # 시작점  찾기
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col]=='S':
                x,y=row, col
    # 이동 방향 정의
    op = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    # 이동
    for i in routes:
        dx, dy=op[i.split()[0]]
        # 이동횟수
        n= int(i.split()[1])
        # 좌표저장
        xx,yy=x,y
        canmove=True
        # n번 이동해보기
        for _ in range(n):
            nx = xx + dx  # 이동한 위치
            ny = yy + dy  # 이동한 위치
            
            # 공원 안에 있고, 장애물이 아니면 이동 가능(True)
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                canmove = True
                xx, yy = nx, ny
            else:  # 공원을 벗어낫거나, 장애물이면 이동 불가(False)
                canmove = False
                break
                
        if canmove:  # 이동이 가능하면 위치 반영해주기
            x, y = nx, ny  
        
    return [x, y]
