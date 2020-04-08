#
#mon=(int(input('plz input 1 :')))
#空位 = 0
#if mon>=1:
#   print('可以上车')
#   if 空位 >= 1:
#        print('可以坐')
#    else:
#        print('不可以坐')
#else:
#    print('不能上车')

money=int(input('money:'))
seat=int(input('seat:'))
result='you cannot get on the bus' if money<2 else 'welcome'+'seat' if seat>=1 else 'welcome'+'stand by'
print(result)