n=int(input())
min_m=float('inf')

for i in range(1,4):
    a,b=map(int,input().split())
    num=(n+a-1)//a
    total=num*b
    if total<min_m:
        min_m=total
print(min_m)