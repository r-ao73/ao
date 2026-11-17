max_total=0
time=0
for i in range(1,8):
    a,b=map(int,input().split())
    total=a+b
    if total>8 and total>max_total:
        max_total=total
        time=i
print(time)