n,k=map(float,input().split())
A=[]
B=[]
for i in range(int(n)):
    if (i+1)%k==0:
        A.append(i+1)
    else:
        B.append(i+1)
tA=sum(A)
tB=sum(B)
print(f"{tA/len(A):.1f} {tB/len(B):.1f}")