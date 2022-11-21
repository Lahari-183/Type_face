def funct(n):
    base = 3
    if n==0:
        return (0)
    arr=[]
    while n:
        n, r=divmod(n,base)
        arr.append(str(r))
    return ''.join(reversed(arr))

n=int(input())
print(funct(n))
