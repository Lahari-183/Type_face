m=[]
for p in range(4):
    l=list(map(int,input().split()))
    m.append(l)

list1=[]
for i in range(0,4):
    for j in range(0,5):
        if(m[i][j]==0):
            k=[]
            k.append(i)
            k.append(j)
            list1.append(k)
o=[]
o.append(list1[0])
temp=o[0][0]
temp1=o[0][1]
for i in range(temp1+1,5):
    if(m[temp][i]==1):
        temp2=[]
        temp2.append(temp)
        temp2.append(i)
        o.append(temp2)
l1=len(list1)
w=list1[l1-1][0]
for i in range(0,5):
    if(m[w][i]==0):
        w1=[]
        w1.append(w1)
        break
        
w2=len(o)
w3=o[w2-1][1]
for i in range(w3+1,5):
    if(m[w][i]==1):
        t12=[]
        t12.append(w)
        t12.append(i)
        o.append(t12)
print(o)
