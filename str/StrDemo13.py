str="abcdef"
new_str=""
i=0
while i<=len(str)-1:
    if  i%2==0:
        new_str+=str[i]
    i+=1
print(new_str)

