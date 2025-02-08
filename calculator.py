from tkinter import *
from tkinter import END

root=Tk()
root.title("Welcome To Calculator")
root.geometry("400x400")
root.resizable(False,False)

def add():
    num1=int(e1.get())
    num2=int(e2.get())
    if b1:
        sum = num1+num2
    output.config(text="Result:"+str(sum))

def sub():
    num1=int(e1.get())
    num2=int(e2.get())
    if b2:
        sum = num1-num2
        output.config(text="Result:"+str(sum))
   
def multi():
    num1=int(e1.get())
    num2=int(e2.get())
    if b3:
        sum = num1*num2
    output.config(text="Result:"+str(sum))
  
def div():
    num1=int(e1.get())
    num2=int(e2.get())
    if b4:
        sum = num1/num2
    output.config(text="Result:"+str(sum))

def reset():
    e1.delete(0,END)
    e2.delete(0,END)


l1=Label(root,text="Welcome to Calculator",font=("arial",15,"bold"),bg="black",fg="gold")
l1.pack()
l2=Label(root,text="Enter The First Number:",font=("arial",10,"bold"),bg="gray",fg="black")
l2.pack(pady=5)
e1=Entry(root,width=4,font=("arial",10,"bold"))
e1.pack(pady=5)
l3=Label(root,text="Enter The Second Number:",font=("arial",10,"bold"),bg="gray",fg="black")
l3.pack()
e2=Entry(root,width=4,font=("arial",10,"bold"))
e2.pack(pady=5)

b1=Button(root,text="+",width=4,font=("arial",10,"bold"),bg="orange",command=add)
b1.place(x=50,y=150)
b2=Button(root,text="-",width=4,font=("arial",10,"bold"),bg="orange",command=sub)
b2.place(x=100,y=150)
b3=Button(root,text="*",width=4,font=("arial",10,"bold"),bg="orange",command=multi)
b3.place(x=150,y=150)
b4=Button(root,text="/",width=4,font=("arial",10,"bold"),bg="orange",command=div)
b4.place(x=200,y=150)
b5=Button(text="RESET",bg="green",font=("arial",10,"bold"),command=reset)
b5.place(x=300,y=150)

output=(Label(root,font=("arial",15,"bold"),fg="black"))
output.pack(pady=100)

root.mainloop()


















# print("Welcome To Calculator")
# print("For addition press:+\n""For subtrack press:- \n""For multiplication press:*\n""For divition press:/")

# select=input("Enter the choice:")
# num1=int(input("Enter The first number:"))
# num2=int(input("Enter The second number:"))


# if add == "+":
#     output.config("Addition of" ,num1, "and", num2 ,"is" ,add(num1,num2))
# elif sub == "-":
#     print("subtact of ",num1 ,"and",num2 ,"is",sub(num1,num2))
# elif multi == "*":
#     print("Multiply of ",num1 ,"and",num2 ,"is",multi(num1,num2))
# elif div == "/":
#     print("Divsion of ",num1 ,"and",num2 ,"is",div(num1,num2))

# else:
#     print("Please scelect again")