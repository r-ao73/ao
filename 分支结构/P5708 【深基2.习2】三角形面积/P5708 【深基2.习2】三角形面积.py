i=input().split()
a=float(i[0])
b=float(i[1])
c=float(i[2])
p=(a+b+c)/2
print(f"{(p*(p-a)*(p-b)*(p-c))**0.5:.1f}")