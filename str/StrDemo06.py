word=input('plz input a word:')
if word[len(word)-3:len(word)]!='ing':
    word=word+'ing'
    print(word)
elif word[len(word)-3:len(word)]=='ing':
    word=word+'ly'
    print(word)




str=input('plz input a word:')
if str[-3:]=='ing':
    str = str+'ly'
else:
    str = str+'ing'
print(str)












