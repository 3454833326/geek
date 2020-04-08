num = 1
sum = 0
while num<=100:
    if num%2==0:
        if num == 66:
            num+=1
            continue
        sum+=num
    num+=1
else:
     print(sum)