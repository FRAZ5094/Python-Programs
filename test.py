sentence=["My","Name","is","jeff","is","is","is","jeff"]
toRemoveList=[]
for i,word in enumerate(sentence):
    if len(word)<3:
        toRemoveList.append(i)

print(sentence)
print(toRemoveList)

for i in reversed(toRemoveList):
    sentence.pop(i)

print(sentence)