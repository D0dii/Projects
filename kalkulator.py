import tkinter 
import math


root = tkinter.Tk()
root.title("Kalkulator")

e = tkinter.Entry(root,width=20)
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)
score = 0
turn = None
should_clear = False

def button_click(number):
    global should_clear
    if should_clear:
        e.delete(0,"end")   
        should_clear = False
    if number == 0 and not e.get():
            return None
    s = e.get() + str(number)
    e.delete(0,"end") 
    e.insert(0,s)

def button_add():
    global score
    global turn
    if e.get():
        score += float(e.get())
        e.delete(0,"end")
        turn = "add"
    else:
        turn = "add"

def button_minus():
    global score
    global turn
    if e.get():
        score += float(e.get())
        e.delete(0,"end")
        turn = "minus"
    else:
        turn = "minus"

def button_times():
    global score
    global turn
    if e.get():
        score += float(e.get())
        e.delete(0,"end")
        turn = "times"
    else:
        turn = "times"


def button_divide():
    global score
    global turn
    if e.get():    
        score += float(e.get())
        e.delete(0,"end")
        turn = "divide"
    else:
        turn = "divide"

def button_clear():
    global score
    global turn
    score = 0
    turn = None
    e.delete(0,"end")

def button_root():
    global score
    if e.get():    
        number = float(e.get())
        score = math.sqrt(number)
        e.delete(0,"end")
        e.insert(0,score)
        score = 0
    else:
        return None

def button_power():
    global score
    if e.get():
        number = float(e.get())
        score = number*number
        e.delete(0,"end")
        e.insert(0,score)
        score = 0
    else:
        return None


def button_equals():
    global score
    global turn  
    global should_clear
    if turn == "add":
        score += float(e.get())
        e.delete(0,"end")
        e.insert(0,score)
    elif turn == "minus":
        score -= float(e.get())
        e.delete(0,"end")
        e.insert(0,score)
    elif turn == "times":
        score *= float(e.get())
        e.delete(0,"end")
        e.insert(0,score)
    elif turn == "divide":
        score /= float(e.get())
        e.delete(0,"end")
        e.insert(0,score)
    score = 0
    turn = None
    should_clear = True




#buttons
button_1 = tkinter.Button(root,text="1",padx=20,pady=20,command=lambda:button_click(1))
button_2 = tkinter.Button(root,text="2",padx=20,pady=20,command=lambda:button_click(2))
button_3 = tkinter.Button(root,text="3",padx=20,pady=20,command=lambda:button_click(3))
button_4 = tkinter.Button(root,text="4",padx=20,pady=20,command=lambda:button_click(4))
button_5 = tkinter.Button(root,text="5",padx=20,pady=20,command=lambda:button_click(5))
button_6 = tkinter.Button(root,text="6",padx=20,pady=20,command=lambda:button_click(6))
button_7 = tkinter.Button(root,text="7",padx=20,pady=20,command=lambda:button_click(7))
button_8 = tkinter.Button(root,text="8",padx=20,pady=20,command=lambda:button_click(8))
button_9 = tkinter.Button(root,text="9",padx=20,pady=20,command=lambda:button_click(9))
button_0 = tkinter.Button(root,text="0",padx=20,pady=20,command=lambda:button_click(0))


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear = tkinter.Button(root,text="C",padx=19.5,pady=20,command=button_clear)
button_equals = tkinter.Button(root,text="=",padx=19,pady=20,command=button_equals)
button_minus = tkinter.Button(root,text="-",padx=23,pady=20,command=button_minus)
button_add = tkinter.Button(root,text="+",padx=20,pady=20,command=button_add)
button_divide = tkinter.Button(root,text="/",padx=23,pady=20,command=button_divide)
button_times = tkinter.Button(root,text="*",padx=22,pady=20,command=button_times)
button_root = tkinter.Button(root,text="√",padx=22,pady=51,command=button_root)
button_power = tkinter.Button(root,text="x^2",padx=13,pady=51,command=button_power)

button_clear.grid(row=4,column=1)
button_equals.grid(row=4,column=2)
button_minus.grid(row=2,column=3)
button_add.grid(row=1,column=3)
button_divide.grid(row=4,column=3)
button_times.grid(row=3,column=3)
button_root.grid(row=0,column=4,rowspan=4)
button_power.grid(row=3,column=4,rowspan=4)

root.mainloop()