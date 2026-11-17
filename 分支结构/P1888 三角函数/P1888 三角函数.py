import math
short,long,xiebian=sorted(map(int,input().split()))
a=math.gcd(short,xiebian)
print(f"{short//a}/{xiebian//a}")