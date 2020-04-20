sentence=["My","Name","is","jeff","is","is","is","jeff"]
toRemoveList=[]

"""
#create a  list of words to remove, then remove them in reverse order after
for i,word in enumerate(sentence):
    if len(word)<3:
        toRemoveList.append(i)
for i in reversed(toRemoveList):
    sentence.pop(i)
"""



for i,word in enumerate(sentence,1):
    i*=-1
    if len(word)<3:
        toRemoveList.append(i)
for i in reversed(toRemoveList):
    sentence.pop(i)



print(sentence)