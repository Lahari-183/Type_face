str1=input()
str2=input()
str3=str2[len(str2)-1]
count=0
for i in str1:
    if i==str3:
        count+=1

print(count)
