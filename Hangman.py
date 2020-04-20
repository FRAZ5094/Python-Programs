string="Fraser"
found=[]
guesscount=0
maxguess=len(string)+2
guess=""
answer=""
print("*"*len(string))
while answer!=string and guesscount<maxguess:

    print("You have {} guesses left".format(maxguess-guesscount))
    guess=input("Guess a letter:\n").lower()
    #guess=guess.lower()
    guesscount+=1
    for i in range(len(string)):
        if string[i].lower()==guess:
            found.append(i)
    print("")
    answer=""
    for i in range(len(string)):
        if i in found:
            answer+=string[i]
        else:
            answer+="*"
    print(answer)
    print("")


for i in range(len(string)):
    pass

if len(found)==len(string):
    print("")
    print("You won")
    print("It took you {} guesses".format(guesscount))
    print("")
else:
    print("You can out of guesses")
    print("")
