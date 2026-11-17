a,b,c=map(int,input().split())
while True:
    if a>b:
        a,b=b,a
    elif b>c:
        b,c=c,b
    elif a>c:
        a,c=c,a
    else:
        break
print(a,b,c)