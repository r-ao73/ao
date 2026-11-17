a=int(input())
if a%100==0:
    if a%400==0:
        b=1
    else:
        b=0
elif a%4==0:
    b=1
else:
    b=0
print(b)