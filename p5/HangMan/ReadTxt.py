from random import randint

file = open("HangMan1kWords.txt", "r")
Words=file.read()
Words = Words.split('\n')
GoodWords=[]
for Word in Words:
    if len(Word)>=4 and len(Word)<=9:
        GoodWords.append(Word)

Word=GoodWords[randint(0,len(GoodWords))]
print(Word)
file.close()
