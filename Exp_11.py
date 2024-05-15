from tkinter import *


def add():
  num1 = float(num1_ent.get())
  num2 = float(num2_ent.get())
  result.config(text=num1 + num2)

def sub():
  num1 = float(num1_ent.get())
  num2 = float(num2_ent.get())
  result.config(text=num1 - num2)

def prod():
  num1 = float(num1_ent.get())
  num2 = float(num2_ent.get())
  result.config(text=num1 * num2)

def div():
  num1 = float(num1_ent.get())
  num2 = float(num2_ent.get())
  result.config(text=num1 / num2)



root = Tk()

root.title("Calculator")
root.geometry("200x300")
root.config(bg="#FFFAB7")

num1 = Label(text="First Number", bg="#F7C566")
num1_ent = Entry(root)
num1.pack(pady=(10,0))
num1_ent.pack()

num2 = Label(text="Second Number", bg="#F7C566")
num2_ent = Entry(root)
num2.pack(pady=(10,0))
num2_ent.pack(pady=(0,10))

plus = Button(text="[+]", bg="#0079FF", command=add)
minus = Button(text="[-]", bg="#00DFA2", command=sub)
multi = Button(text="[*]", bg="#F6FA70", command=prod)
dvd = Button(text="[/]", bg="#FF0060", command=div)
plus.pack()
minus.pack()
multi.pack()
dvd.pack(pady=(0,10))

calc = Label(text="Calcultion - ", bg="#5DEBD7")
result = Label(text="")
calc.pack(pady=(0,10))
result.pack()

root.mainloop()
