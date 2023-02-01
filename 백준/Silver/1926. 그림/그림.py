import sys
imput=sys.stdin.readline
n,m= map(int, input().split())
map= [list(map(int, input().split())) for _ in range(n)]
chk=[[False]*m for _ in range(n)]

# 오른쪽, 밑, 왼쪽, 위
dy=[0,1,0,-1] 
dx=[1,0,-1,0]

def bfs(y,x):
  rs=1 # 그림 사이즈 
  q=[(y,x)]
  while q:
    ey, ex= q.pop() # 각각 q 뽑기
    # 동서남북 옮겨가면서 새로운 1이 있는지 확인
    for k in range(4):
      ny=ey+dy[k]
      nx=ex+dx[k]
      # 범위 넘어가면 안된다.
      if 0<=ny<n and 0<=nx<m:
        # 1이고 방문안한 경우에는 새로운 곳 방문했다고 말해
        if map[ny][nx]==1 and chk[ny][nx]==False:
          rs+=1
          chk[ny][nx]=True
          q.append((ny,nx))
  return rs



cnt=0
maxp=0
for j in range(n):
  for i in range(m):
    if map[j][i]==1 and chk[j][i]==False:
      chk[j][i]=True
      # 전체 그림 개수 늘리기, 그림 크기 늘리기
      cnt+=1
      maxp=max(maxp,bfs(j,i))
print(cnt)
print(maxp)
