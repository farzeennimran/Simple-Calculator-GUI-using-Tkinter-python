from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("320x440")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    if item == 'x':
        # Remove the last character from the expression
        expression = expression[:-1]
    else:
        expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("0")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()

# Initialize the entry box with "0"
input_text.set("0")
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=300, height=50, bd=4, highlightbackground="gray", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 32, 'bold'), textvariable=input_text, width=45, fg="gray", bg="light blue", bd=5, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=45) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=265, bg="sky blue")
 
btns_frame.pack()
 
# first row
 
allclear = Button(btns_frame, text = "AC", fg = "black", width = 22, height = 3, bd = 1, bg = "light blue", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

backspace = Button(btns_frame, text = "x", fg= "black", width= 10, height= 3, bd = 1, bg = "light blue", command = lambda: btn_click("x")).grid(row = 0, column = 2, padx = 1, pady = 1) 

# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 0)

eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 0, pady = 0)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 0)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 0, pady = 0)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 0, pady = 0)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 0, pady = 0)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 22, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equal = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 1, bg = "light blue", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 0, pady = 0)
 
win.mainloop()