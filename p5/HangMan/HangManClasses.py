import p5

class HangmanDrawing:
    def __init__(self,BottomLeft_x,BottomLeft_y,w,h,initstage):

        self.bottomLeft=p5.Vector(BottomLeft_x,BottomLeft_y)
        self.height=h
        self.width=w
        self.stage=initstage
        self.linewidth=10
        self.GameWon=False
        self.GameOver=False

    def stageInc(self):
        self.stage+=1

    def checkIfGameOver(self,Game):
        if Game.revealed==Game.word:
            self.GameWon=True
        elif self.stage>8:
            self.GameOver=True

    def draw(self):
        p5.stroke_weight(0.01)
        if self.stage>0:
            p5.rect((self.bottomLeft.x,self.bottomLeft.y),self.linewidth,-self.height)
        if self.stage>1:
            p5.rect((self.bottomLeft.x,self.bottomLeft.y-self.height),self.width/2+self.linewidth/2,self.linewidth)
        if self.stage>2:
            p5.rect((self.bottomLeft.x+self.width/2-self.linewidth/2,self.bottomLeft.y-self.height),self.linewidth,self.height/4)
        if self.stage>3:
            p5.no_fill()
            p5.circle((self.bottomLeft.x+self.width/2,self.bottomLeft.y-self.height+self.height/4+(self.linewidth*2.5)),self.linewidth*5,mode="CENTER")
        if self.stage>4:
            p5.fill(255)
            p5.rect((self.bottomLeft.x+self.width/2-self.linewidth/4,self.bottomLeft.y-self.height+self.height/4+(self.linewidth*5)),self.linewidth/2,self.height/4)
        if self.stage>5:
            p5.rect((self.bottomLeft.x+self.width/2-self.linewidth/4,self.bottomLeft.y-self.height+self.height/4+(self.linewidth*5)+10),-self.width/4,self.linewidth/2)
        if self.stage>6:
            p5.rect((self.bottomLeft.x+self.width/2+self.linewidth/4,self.bottomLeft.y-self.height+self.height/4+(self.linewidth*5)+10),self.width/4,self.linewidth/2)
        if self.stage>7:
            p5.stroke(255)
            p5.stroke_weight(4)
            p5.line((self.bottomLeft.x+self.width/2,self.bottomLeft.y-self.height+self.height/4+(self.linewidth*5)+self.height/4),(self.bottomLeft.x+self.width-self.width/4,self.bottomLeft.y-self.height/12))
        if self.stage>8:
            p5.line((self.bottomLeft.x+self.width/2,self.bottomLeft.y-self.height+self.height/4+(self.linewidth*5)+self.height/4),(self.bottomLeft.x+self.width-self.width*3/4,self.bottomLeft.y-self.height/12))

class HangmanWordDisplay:
    def __init__(self,y,w):
        self.width=w
        self.y=y


    def displayWord(self,word):
        self.word=word
        self.wordLength=len(word)
        self.spacing=(self.width/(self.wordLength))/2

        self.offset=(width/2-self.width/2)+self.spacing/2

        self.txt_size=int(self.spacing*4/3)
        self.GuessFont=p5.create_font("arial.ttf",self.txt_size)
        p5.text_font(self.GuessFont,self.txt_size)
        p5.text_align("CENTER","BASELINE")
        self.txt_width=p5.text_width("A")


        for i in range(self.wordLength):
            p5.fill(255)
            p5.text(word[i],((i*2*self.spacing)+self.spacing/2+self.offset,self.y-(self.txt_width*4/3)-2))
            p5.line((i*2*self.spacing+self.offset,self.y),(((i*2)+1)*self.spacing+self.offset,self.y))

class HangmanGame:
    def __init__(self,word):
        self.word=word
        self.foundIndex=[]
        self.guessedLetters=[]

    def enterLetter(self,letter,Man):
        self.guessedLetters.append(letter)
        #print(self.guessedLetters)
        initialFoundLen=len(self.foundIndex)
        for i in range(len(self.word)):
            if self.word[i].lower()==letter:
                self.foundIndex.append(i)

        self.revealed=""

        for i in range(len(self.word)):
            if i in self.foundIndex:
                self.revealed+=self.word[i]
            else:
                self.revealed+="*"

        if len(self.foundIndex)==initialFoundLen:
            Man.stageInc()
            

