def count(sent):
    space =sent.count(' ')
    print ('количество пробелов '+ str(space))
    letters = (len(sent) - space)
    print ('Количество букв ' + str(letters))
    print ('длина строки ' + str(len(sent)))
    words = sent.split()
    print ('количество слов ' + str(len(words)))
count(input())
