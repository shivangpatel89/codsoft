from tkinter import *
from tkinter import END
import random
root =Tk()
root.geometry("600x700")
root.minsize(100,100)
root.title("Rock Paper scissors Game")

title_label=Label(text='Welcome to the game shivang!',bg='black',fg="white",font='comicsansms 18 bold',border=5,relief=SUNKEN)
title_label.pack()

game=['Rock','Paper','Scissors']
user_score=0
computer_score=0
game_tie=0
i=0

def Rock():
    round=int(rounds.get())
    global user_score,computer_score,game_tie,i
    computer=random.choice(game)
    while i < round:
        if (b1 and computer == "Scissors"):
            user_score+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Rock""\nUser wins"+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))

        elif(b1 and computer=="Rock"):
            game_tie+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Rock""\ngame tie"+str(game_tie)+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))

        else:
            computer_score+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Rock""\nComputer wins "+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))
        i+=1
        break

def Paper():
    round=int(rounds.get())
    computer=random.choice(game)
    global user_score,computer_score,game_tie,i
    while i < round:
        if (b2 and computer == "Rock"):
            user_score+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Paper""\nUser wins"+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))

        elif(b2 and computer=="Paper"):
            game_tie+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Paper""\ngame tie"+str(game_tie)+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))
        else:
            computer_score+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Paper""\nComputer wins "+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))
        i+=1
        break

def Scissors():
    round=int(rounds.get())
    computer=random.choice(game)
    global user_score,computer_score,game_tie,i
    while i < round:
        if (b3 and computer == "Paper"):
            user_score+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Scissors""\nUser wins"+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))

        elif(b3 and computer=="Scissors"):
            game_tie+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Scissros""\ngame tie"+str(game_tie)+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))
        else:
            computer_score+=1
            output.config(text="Computer choice:"+computer+"\nUser choice:Scissors""\nComputer wins "+"\nUser score:"+str(user_score)+"\nComputer score:"+str(computer_score))
        i+=1
        break

def result():
    if user_score > computer_score:
        output.config(text="You wins game.")
    elif user_score == computer_score:
        output.config(text="game draws.")
    else:
        output.config(text="computer wins game.")

def try_again():
    global user_score,computer_score,game_tie,i
    user_score=0
    computer_score=0
    game_tie=0
    i=0
    rounds.delete(0,END)
    

photo = PhotoImage(file='rock.png')
shiv = Label(image=photo)
shiv.pack()

label1=Label(root,font=('arial',15,'bold'),text="Enter Number of Rounds:")
label1.pack()
rounds=Entry(root,font=('arial',15,'bold'),width=3)
rounds.pack()

b1 = Button(root,text='Rock',bg='silver',fg='black',font='comicsansms 15 bold',command=Rock)
b1.pack(padx=0,pady=10)

b2 = Button(root,text='Paper',bg='silver',fg='black',font='comicsansms 15 bold',command=Paper)
b2.pack(padx=0,pady=10)

b3 = Button(root,text='Scissors',bg='silver',fg='black',font='comicsansms 15 bold',command=Scissors)
b3.pack(padx=0,pady=10)

output=Label(root,font=('arial',17,'bold'))
output.pack()
result1=Button(root,text="check results",font=("arial",15,"bold"),bg="green",command=result)
result1.pack()

b4=Button(root,text="Try Again!",font=("arial",15,"bold"),bg="red",command=try_again)
b4.place(x=450,y=325)

root.mainloop() 
