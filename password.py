from tkinter import *
from tkinter import messagebox
import string
import random

root=Tk()
root.title("Password genrator.")
root.geometry("400x300")

def generate_password():
    length=int(length1.get())
    if length <= 5:
        messagebox.showerror("ERROR","Password require more than 5 characters")
    elif digits.get():
        password = ''.join(random.choice(string.digits) for _ in range(length))
        output.config(text="password:" +password)
    elif alphabate.get():
        password = "".join(random.choice(string.ascii_letters) for _ in range(length))
        output.config(text="password:" +password)
    elif combine.get():
        password = "".join(random.choice(string.digits+string.ascii_letters+string.punctuation) for _ in range(length))
        output.config(text="password:" +password)


label=Label(text="Enter the Length of Password",font=("arial",15,"bold"),bg="green",fg="black",relief=SUNKEN)
label.pack()

length1=Entry(root,width=2,font=("arial",15,"bold"))
length1.pack(pady=10)
              
digits=BooleanVar()
b1=Checkbutton(root,text="Digits",variable=digits)
b1.pack()

alphabate=BooleanVar()
b2=Checkbutton(root,text="Alphabate",variable=alphabate)
b2.pack()

combine=BooleanVar()
b3=Checkbutton(text="combine",variable=combine)
b3.pack()

get=Button(text="GET PASSWORD",bg="blue",fg="white",relief=SUNKEN,border=5,command=generate_password)
get.pack()

output=(Label(root,font=("arial",15,"bold"),fg="black",border=6))
output.pack(pady=10)

root.mainloop()