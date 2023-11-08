def solution(arr):
    n=len(arr)
    answer = [0,0]
    def quad(y,x,length):
        flag=arr[y][x]
        for i in range(y,y+length):
            for j in range(x,x+length):
                if arr[i][j]!=flag:
                    length=length//2
                    quad(y,x,length)
                    quad(y+length,x,length)
                    quad(y,x+length,length)
                    quad(y+length,x+length,length)
                    return
        answer[flag]+=1
    quad(0,0,n)
    return answer