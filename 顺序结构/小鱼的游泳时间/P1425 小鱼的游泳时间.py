a,b,c,d=map(int,input().split())
e=c*60+d-a*60-b
h=e//60
m=e%60
print(h,m)