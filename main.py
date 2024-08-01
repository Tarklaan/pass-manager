from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import pandas as pd
from pandastable import Table


# ----------------------------------- Library------------------------------------ #
def libr():

    df=pd.read_csv("data.txt")
    top=Toplevel()
    top.title("Password Library")
    top.minsize(height=500,width=640)
    table = Table(top, dataframe=df, showtoolbar=False)
    table.show()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    passwordL=password_numbers+password_symbols+password_letters
    shuffle(passwordL)
    password="".join(passwordL)
    pText.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    w=wText.get()
    e=eText.get()
    p=pText.get()
    if len(w) ==0 or len(p)==0:
        messagebox.showinfo(title="ERROR",message="Dont leave the fileds Empty")
    else:
        dic=f"\n{w},{e},{p}\n"
        k=messagebox.askyesno(title=f"{w}", message=f"these are the deatials:\nEmail:{e}\nPassowrd:{p}"
                                                    f"\nIs it ok to save...")
        if k:
            with open("data.txt","a") as file:
                file.write(f"{dic}\n")
                pText.delete(0,END)
                wText.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("password manager")
window.config(padx=50, pady=50)
c=Canvas(height=300, width=300)
p = PhotoImage(file="logo.png")
c.create_image(150,150,image=p)
website=Label(text="Website :")
wText=Entry(width=42)
wText.focus()
email=Label(text="Email :")
eText=Entry(width=42)
eText.insert(index=END,string="@gmail.com")
password=Label(text="Password :")
pText=Entry(width=25)
generate=Button(text="Generat",command=generatepass)
lib=Button(text="Library",command=libr,bg="green")
add=Button(text="Save",width=35,command=save,bg="red")

c.grid(row=0,column=1,columnspan=2)
website.grid(row=1,column=0)
wText.grid(row=1,column=1,columnspan=2)
email.grid(row=2, column=0)
eText.grid(row=2, column=1,columnspan=2)
password.grid(row=3, column=0)
pText.grid(row=3, column=1,columnspan=1)
generate.grid(row=3, column=2)
lib.grid(row=4,column=0)
add.grid(row=4, column=1,columnspan=3)

mainloop()
