from Tkinter import Button
from Tkinter import *
import tkMessageBox
import random as r
import time

def button(frame):
    b=Button(frame,padx=1,bg="green",width=3,text=" ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def changeplayer():  #this function runs when there is another player's turn
    global mark
    for i in ['O','X']:
        if not(i==mark):
            mark=i
            break

def reset(): #when dashboard needs to get reset
    global mark
    for i in range(3):
        for j in range(3):
            b[i][j]["text"]=""
            b[i][j]["state"]=NORMAL

def updateScoreboard(mark):
    global score1
    global score2
    if mark=="O":
        score1+=1
    else:
        score2+=1
    scoreboard.config(text="Score O : " + str(score1) + " X : "+ str(score2),font=('Times',30,'bold'))

def check():
    for i in range(3):
        if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==mark or  #to check all rows
        b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==mark):
            updateScoreboard(mark)
            tkMessageBox.showinfo("Congratulations!!!","'"+mark+"' has won")
            reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==mark or   #to check diagonal-wise
    b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==mark):
        updateScoreboard(mark)
        tkMessageBox.showinfo("Congratulations!!!", "'" + mark + "' has won")
        reset()
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]
         == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"]==DISABLED):  #no more box to use
        tkMessageBox.showinfo("Tied!!!","This match ended in a draw!!!")
        reset()
def click(row,col):
    b[row][col].config(text=mark,state=DISABLED,disabledforeground=colour[mark])
    check()
    changeplayer()
    label.config(text=mark+"'s Turn")

###### Main Code is below #######
root=Tk() #window
root.title("Tic-Tac-Toe") #title
mark=r.choice(['O','X']) #Two operators which are sign for each player
colour={'O':"black",'X':"red"}
b=[[],[],[]]
score1=0
score2=0
for i in range(3):
    for j in range(3):
        b[i].append(button(root))
        b[i][j].config(command=lambda row=i,col=j:click(row,col))
        b[i][j].grid(row=i,column=j)
label=Label(text=mark+"'s Turn",font=('Times',25,'bold'))
scoreboardLabel=Label(text="ScoreBoard",font=('Times',30,'bold'))
scoreboard=Label(text="Score  O : "+ str(score1)+" X : "+str(score2),font=('Times',27,'bold'))
label.grid(row=3,column=0,columnspan=3)
scoreboardLabel.grid(row=4,column=0,columnspan=3)
scoreboard.grid(row=5,column=0,columnspan=3)
root.mainloop()
