import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num)) #heapq는 min heap만을 지원하므로 -를 통해 뒤집어 준다.
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)