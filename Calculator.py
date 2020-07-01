from tkinter import *
from tkinter import messagebox

# part 1: functions for number

val = ""
val2 = ""
def on1click():
    global val
    val = val + "1"
    data.set(val)

def on2click():
    global val
    val = val + "2"
    data.set(val)

def on3click():
    global val
    val = val + "3"
    data.set(val)

def on4click():
    global val
    val = val + "4"
    data.set(val)

def on5click():
    global val
    val = val + "5"
    data.set(val)

def on6click():
    global val
    val = val + "6"
    data.set(val)

def on7click():
    global val
    val = val + "7"
    data.set(val)

def on8click():
    global val
    val = val + "8"
    data.set(val)

def on9click():
    global val
    val = val + "9"
    data.set(val)

def on0click():
    global val
    val = val + "0"
    data.set(val)

# part 2: function for operator
A = 0
opt = ""

# result = 0

def plus():
    global val
    global A
    global opt
    A = int(val)
    opt = "+"
    val += "+"
    data.set(val)

def minus():
    global val
    global A
    global opt
    A = int(val)
    opt = "-"
    val += "-"
    data.set(val)

def mul():
    global val
    global A
    global opt
    A = int(val)
    opt = "*"
    val += "*"
    data.set(val)

def div():
    global val
    global A
    global opt
    A = int(val)
    opt = "/"
    val += "/"
    data.set(val)


# part 3: function for clear label
def clear():
    global val
    global A
    global opt
    val = ""
    A = 0
    opt = ""
    data.set(val)


# part 4: function for equals to
def result():
    global val
    global A
    global val2
    val2 = val
    if opt == "+":
        x = int(val2.split("+")[1])
        C = A + x
        data.set(C)
        val = str(C)
    elif opt == "-":
        x = int(val2.split("-")[1])
        C = A - x
        data.set(C)
        val = str(C)
    elif opt == "*":
        x = int(val2.split("*")[1])
        C = A * x
        data.set(C)
        val = str(C)
    elif opt == "/":
        x = (int(val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","Divison by O is not Allowed")
            val = ""
            A = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)
            val = str(C)


# main function
def main_screen():
    cal = Tk()
    cal.title("Calculator")
    cal.geometry("350x450+300+300")
    cal.resizable(0,0)


    global data
    data = StringVar()

    lbl = Label(cal, text = "", anchor = SE,font=("Verdana", 19), textvariable = data,bg = "white", fg ="black")
    lbl.pack(expand = True, fill = "both")

    # take 4 frames for particular row wised
    # btnrow1 contains 4 btn as it's every frame contains four four btns
    btnrow1 = Frame(cal,bg="white")
    btnrow1.pack(expand = True, fill = "both") #expand for frame expand and fill for x or y

    btnrow2 = Frame(cal, bg="black")
    btnrow2.pack(expand= True, fill="both")

    btnrow3 = Frame(cal, bg="grey")
    btnrow3.pack(expand= True, fill="both")

    btnrow4 = Frame(cal, bg="black")
    btnrow4.pack(expand= True, fill="both")

    # Take btn for btnrow1
    btn1 = Button(btnrow1,
                  text = "1",
                  font = ("Verdana", 19),
                  relief = GROOVE,
                  border = 0,
                  command = on1click
                  )
    btn1.pack(side = LEFT, expand = True, fill = "both")

    btn2 = Button(btnrow1,
                  text="2",
                  # bg = "lightgrey",
                  font=("Verdana", 19),
                  relief=GROOVE,
                  border=0,
                  command = on2click
                  )
    btn2.pack(side=LEFT, expand=True, fill="both")

    btn3 = Button(btnrow1,
                  text="3",
                  # bg = "lightgrey",
                  font=("Verdana", 19),
                  relief=GROOVE,
                  border=0,
                  command = on3click
                  )
    btn3.pack(side=LEFT, expand=True, fill="both")

    btn_plus = Button(btnrow1,
                  text="+",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                      command = plus)
    btn_plus.pack(side=LEFT, expand=True, fill="both")

    # Take btn for btnrow2
    btn4 = Button(btnrow2,
                  text="4",
                  activebackground="yellow",
                  font=("Verdana", 19),
                  relief=GROOVE,
                  border=0,
                  command = on4click
                  )
    btn4.pack(side=LEFT, expand=True, fill="both")

    btn5 = Button(btnrow2,
                  text="5",
                  # bg = "lightgrey",
                  font=("Verdana", 19),
                  relief=GROOVE,
                  border=0,
                  command = on5click
                  )
    btn5.pack(side=LEFT, expand=True, fill="both")

    btn6 = Button(btnrow2,
                  text="6",
                  # bg = "lightgrey",
                  font=("Verdana", 19),
                  relief=GROOVE,
                  border=0,
                  command = on6click
                  )
    btn6.pack(side=LEFT, expand=True, fill="both")

    btn_minus = Button(btnrow2,
                  text="-",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                      command = minus)
    btn_minus.pack(side=LEFT, expand=True, fill="both")

    # Take btn for btnrow1
    btn7 = Button(btnrow3,
                  text="7",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                  command = on7click)
    btn7.pack(side=LEFT, expand=True, fill="both")

    btn8 = Button(btnrow3,
                  text="8",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                  command = on8click)
    btn8.pack(side=LEFT, expand=True, fill="both")

    btn9 = Button(btnrow3,
                  text="9",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                  command = on9click)
    btn9.pack(side=LEFT, expand=True, fill="both")

    btn_mul = Button(btnrow3,
                  text="*",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                      command = mul)
    btn_mul.pack(side=LEFT, expand=True, fill="both")

    # Take btn for btnrow1
    btn_clear = Button(btnrow4,
                  text="CE",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                  command = clear)
    btn_clear.pack(side=LEFT, expand=True, fill="both")

    btn0 = Button(btnrow4,
                  text="0",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                  command = on0click)
    btn0.pack(side=LEFT, expand=True, fill="both")

    btn_equal = Button(btnrow4,
                  text="=",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                       command = result)
    btn_equal.pack(side=LEFT, expand=True, fill="both")

    # btn_per = Button(btnrow4,
    #                  text="%",
    #                  # bg = "lightgrey",
    #                  font=("Verdana", 19), relief=GROOVE,
    #                  border=0,
    #                  command= percentage)
    # btn_per.pack(side=LEFT, expand=True, fill="both")

    btn_div = Button(btnrow4,
                  text="/",
                  # bg = "lightgrey",
                  font=("Verdana", 19), relief = GROOVE,
                  border = 0,
                      command = div)
    btn_div.pack(side=LEFT, expand=True, fill="both")


    cal.mainloop()
main_screen()

# value = IntVar()
#
# global value
# global value_entry
#
# Button(text="Enter Value",width= "20", height="1", bg="white").pack()
# value_entry = Entry(textvariable = value)
# value_entry.pack()