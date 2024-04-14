from tkinter import *

gui = Tk() 
gui.geometry("320x440")  
gui.resizable(0, 0)  
gui.title("Calculator")

def click(item):
    global expression
    if item == 'x':
        expression = expression[:-1]
    else:
        expression = expression + str(item)
    input.set(expression)

def clear(): 
    global expression 
    expression = "" 
    input.set("0")
 
def equal():
    global expression
    result = str(eval(expression)) 
    input.set(result)
    expression = ""
 
expression = ""
input = StringVar()

#Initialize the entry box with "0"
input.set("0")
 
#creating a frame for the entry box
entry_box = Frame(gui, width=300, height=50, bd=4, highlightbackground="gray", highlightthickness=2)
entry_box.pack(side=TOP)
 
#creating entry box space inside the 'Frame'
entry_box_space = Entry(entry_box, font=('arial', 32, 'bold'), textvariable=input, width=45, fg="gray", bg="light blue", bd=5, justify=RIGHT)
entry_box_space.grid(row=0, column=0)
entry_box_space.pack(ipady=45) 
 
#creating another 'Frame' for the button below the 'entry_box'
buttons = Frame(gui, width=312, height=265, bg="sky blue")
buttons.pack()

one = Button(buttons, text = "1", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(buttons, text = "2", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(2)).grid(row = 3, column = 1, padx = 0, pady = 0)
 
three = Button(buttons, text = "3", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

four = Button(buttons, text = "4", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 0)
 
five = Button(buttons, text = "5", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(5)).grid(row = 2, column = 1, padx = 0, pady = 0)
 
six = Button(buttons, text = "6", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

seven = Button(buttons, text = "7", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 0)

eight = Button(buttons, text = "8", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(8)).grid(row = 1, column = 1, padx = 0, pady = 0)
 
nine = Button(buttons, text = "9", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

zero = Button(buttons, text = "0", fg = "black", width = 22, height = 3, bd = 1, bg = "light blue", command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

allclear = Button(buttons, text = "AC", fg = "black", width = 22, height = 3, bd = 1, bg = "light blue", command = lambda: clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)

backspace = Button(buttons, text = "x", fg= "black", width= 10, height= 3, bd = 1, bg = "light blue", command = lambda: click("x")).grid(row = 0, column = 2, padx = 1, pady = 1) 

plus = Button(buttons, text = "+", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click("+")).grid(row = 3, column = 3, padx = 0, pady = 0)

minus = Button(buttons, text = "-", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

multiply = Button(buttons, text = "*", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
   
divide = Button(buttons, text = "/", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
equals = Button(buttons, text = "=", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: equal()).grid(row = 4, column = 3, padx = 0, pady = 0)

point = Button(buttons, text = ".", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

gui.mainloop()