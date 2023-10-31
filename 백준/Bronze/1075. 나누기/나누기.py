a=list(input())
f=int(input())
cnt=""
for i in range(0,len(a)-2):
    cnt+=a[i]
k=int(cnt+'00')
if k%f==0:
    print(0,0,sep="")
elif f-k%f<10:
    print(0,f-k%f,sep="")
else: 
    print(f-k%f)