a=list(map(int,input().split()))
b=int(input())+30
t=0
for i in range(0,10):
    if a[i]<=b:
        t+=1
print(t)