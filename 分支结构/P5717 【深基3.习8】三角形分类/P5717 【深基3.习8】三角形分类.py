a,b,c=map(int,input().split())
a2=a*a
b2=b*b
c2=c*c
# if a<=b<=c or b<=a<=c:
    # d1=a
    # d2=b
    # d3=c
# elif a<=c<=b or c<=a<=b:
    # d1=a
    # d2=c
    # d3=b
# elif c<=b<=a or b<=c<=a:
    # d1=b
    # d2=c
    # d3=a
d1,d2,d3=sorted([a,b,c])
de=d1**2+d2**2
if d1+d2>d3:
    if de == d3**2:
        print('Right triangle')
    if de > d3**2:
        print('Acute triangle')
    if de < d3**2:
        print('Obtuse triangle')
    if d1==d2 or d1==d3 or d2==d3:
        print('Isosceles triangle')
    if  d1==d2 and d2==d3:
        print('Equilateral triangle')
else:
    print('Not triangle')