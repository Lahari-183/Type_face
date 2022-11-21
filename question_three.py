digits_valid=[0,1,2,5,6,8,9]

def validity(s):
    s=str(s)
    for i in s:
        if int(i) not in digits_valid:
            return False
    return True

n=int(input())

if n<len(digits_valid):
    print(digits_valid[n-1])
else:
    count=len(digits_valid)
    s=digits_valid[-1]
    while(count<=n):
        s+=1
        if validity(s):
            count+=1
    print(s)
