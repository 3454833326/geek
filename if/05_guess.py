import random
bot = (random.randint(1,3))

print(bot)
player = int(input('pls type in your number 1 = rock 2= paper 3 = sisor:'))
if player == 1 and bot ==3 or player == 2 and bot ==1 or player ==3 and bot ==2:
    print('player won')
elif player == bot:
    print('tie')
else:
    print('bot won')