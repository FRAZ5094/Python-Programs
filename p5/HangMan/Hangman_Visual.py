import p5 
import time
from HangManClasses import HangmanDrawing,HangmanWordDisplay,HangmanGame
from random import randint


global word,newLetter

file = open("HangMan1kWords.txt", "r")
Words=file.read()
Words = Words.split('\n')
GoodWords=[]
for Word in Words:
    if len(Word)>=4 and len(Word)<=9:
        GoodWords.append(Word)

word=GoodWords[randint(0,len(GoodWords))]
file.close()

newLetter=" "


def setup():
    global Man,wordDisplay,newLetter,Game
    print(word)
    p5.size(400,500)
    Man=HangmanDrawing(width/4,200,width/2,200,0)
    Game=HangmanGame(word)
    Game.revealed="*"*len(word)
    wordDisplay=HangmanWordDisplay(height/2+20,width)
    newLetter=" "
def draw():
    global Man,wordDisplay,newLetter,Game
    p5.background(0)
    p5.fill(255)
    p5.stroke(255)
    p5.stroke_weight(1)
    if not Man.GameWon and  not Man.GameOver:
        wordDisplay.displayWord(Game.revealed)
    p5.fill(255)
    p5.stroke(255)
    Man.draw()
    if not Man.GameWon and not Man.GameOver:
        if key_is_pressed:
            if key not in ["ENTER","SHIFT","BACKSPACE","UNKNOWN","tab","UP","DOWN","LEFT","RIGHT"]:
                newLetter=str(key).lower()
            elif key=="BACKSPACE":
                newLetter=""
            elif key=="ENTER":
                if len(newLetter)!=0 and  newLetter not in Game.guessedLetters:
                    Game.enterLetter(newLetter,Man)
                    newLetter=""

    if len(newLetter)!=0:
        txt_size=40
        EnteredLetterFont=p5.create_font("arial.ttf",txt_size)
        p5.text_font(EnteredLetterFont,txt_size)
        p5.text_align("CENTER","CENTER")
        p5.text(newLetter,(width/2,height*3/4-20))
    
    guessedLettersstring=""
    for i in range(len(Game.guessedLetters)):
        guessedLettersstring+=Game.guessedLetters[i]
        guessedLettersstring+=" "

    guessedLetterFont=p5.create_font("arial.ttf",20)
    p5.text_font(guessedLetterFont,20)
    
    p5.text_align("CENTER","CENTER")
    p5.text(("Already used Letters:"),(width/2,height*7/8))
    p5.text(str(guessedLettersstring),(width/2,(height*7/8)+25))
   
    Man.checkIfGameOver(Game)
    
    if Man.GameWon:
        txt_size=30
        #txt_size=int((width/7)*4/3)
        GameWonFont=p5.create_font("arial.ttf",txt_size)
        p5.text_font(GameWonFont,txt_size)
        p5.text_align("CENTER","CENTER")
        p5.text("YOU WON",(width/2,height/2))
        p5.text("The Right word was:",(width/2,height/2+30))
        p5.text("{}".format(word),(width/2,height/2+60))
        newLetter=""
    if Man.GameOver:
        txt_size=30
        #txt_size=int((width/9)*4/3)
        GameOverFont=p5.create_font("arial.ttf",txt_size)
        p5.text_font(GameOverFont,txt_size)
        p5.text_align("CENTER","CENTER")
        p5.text("YOU LOST",(width/2,height/2))
        p5.text("The Right word was:",(width/2,height/2+30))
        p5.text("{}".format(word),(width/2,height/2+60))
        newLetter=""

p5.run(frame_rate=60)