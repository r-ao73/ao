def jiec(n):
    re = 0
    for i in range(n):
        re+=n*(i+1)
    return re
s=int(input())
print(jiec(s))