sum = 0
num = 1
while num<=4:
    if num==9:
        num += 1
        continue
    sum+=num
    num+=1

print(sum)