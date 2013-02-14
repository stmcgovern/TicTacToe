#Tic Tac Toe Game
#Strategy is to have a player class and a board class. The 

#make a dictionary so that X and O will be displayed in board display
output = { 0 : "_", 1 : "X", -1: "O"}

class Board:
    state= [0,0,0,0,0,0,0,0,0]
    def display(self):
        print output[self.state[0]], "|",  output[self.state[1]], "|", output[self.state[2]], "\n"
        print output[self.state[3]], "|",  output[self.state[4]], "|", output[self.state[5]], "\n"
        print output[self.state[6]], "|",  output[self.state[7]], "|", output[self.state[8]], "\n"
    
    def winStatus(self):
        full=0;
        for value in self.state:
            full+=abs(value)
        

        if(self.state[0]+self.state[1]+self.state[2]==3):
            return 1
        elif(self.state[3]+self.state[4]+self.state[5]==3):
            return 1
        elif(self.state[6]+self.state[7]+self.state[8]==3):
            return 1
        elif(self.state[0]+self.state[3]+self.state[6]==3):
            return 1
        elif(self.state[1]+self.state[4]+self.state[7]==3):
            return 1
        elif(self.state[2]+self.state[5]+self.state[8]==3):
            return 1
        elif(self.state[0]+self.state[4]+self.state[8]==3):
            return 1
        elif(self.state[2]+self.state[4]+self.state[6]==3):
            return 1
        elif(self.state[0]+self.state[1]+self.state[2]==-3):
            return 2
        elif(self.state[3]+self.state[4]+self.state[5]==-3):
            return 2
        elif(self.state[6]+self.state[7]+self.state[8]==-3):
            return 2
        elif(self.state[0]+self.state[3]+self.state[6]==-3):
            return 2
        elif(self.state[1]+self.state[4]+self.state[7]==-3):
            return 2
        elif(self.state[2]+self.state[5]+self.state[8]==-3):
            return 2
        elif(self.state[0]+self.state[4]+self.state[8]==-3):
            return 2
        elif(self.state[2]+self.state[4]+self.state[6]==-3):
            return 2
        elif full ==9:
            return 3
        else:
            return 0

class Player:
    name = ""
    def go(self, Board):
        print self.name, "Your turn!"
        move = int(raw_input("Where do you want to move (enter 0-8)?"))
       # while(move >8 or move <0 or Board.state[move]!=0):
       #     print "Try again"
       #     move = int(raw_input("Where do you want to move (enter 0-8)?"))
            
        return move
        
        

#main


Human1 = Player()
Human2 = Player()
myBoard = Board()

Human1.name = "Gerald"
Human2.name = "Winifred"

#game play
while myBoard.winStatus() == 0:

    myBoard.display()
    move1= Human1.go(myBoard)
    myBoard.state[move1]=1
    if myBoard.winStatus() != 0 :
        break
    else:
        myBoard.display()
        move2= Human2.go()
        myBoard.state[move2]=-1


myBoard.display()

if myBoard.winStatus() ==1:
    print Human1.name, " you won!"
elif  myBoard.winStatus() ==2:
    myBoard.display()
    print Human2.name, " you won!"
else:
    print "It's a tie!"
