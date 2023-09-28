# Import all the relevant packages
from tkinter import *
from tkinter import ttk

var = 0
a = ttk.Notebook()

frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)

root = ttk.Frame(a)

# To display question numbers to choose from
def quiz(var):
    a.add(frame1, text = "Q1")
    a.add(frame2, text = "Q2")
    a.add(frame3, text = "Q3")
    a.add(frame4, text = "Q4")
    a.add(frame5, text = "Q5")

    # To display the questions and its options
    Label(frame1, text = "What is the diameter of earth?", font = ("Courier",20,"bold")).grid(row=2,column=2)
    Button(frame1, text = "12000", font = ("Courier",15,"bold"),bg="blue", command = a1_correct).grid(row=3,column=1)
    Button(frame1, text = "32000",font = ("Courier",15,"bold"),bg="light green", command = a1_wrong).grid(row=5,column=1)
    Button(frame1, text = "25000",font = ("Courier",15,"bold"),bg="light yellow", command = a1_wrong).grid(row=7,column=1)

    Label(frame2, text = "What is the capital of Nigeria?", font = ("Courier",20,"bold")).grid(row=2,column=2)
    Button(frame2, text = "Lagos", font = ("Courier",15,"bold"),bg="blue", command = a2_wrong).grid(row=3,column=1)
    Button(frame2, text = "Abuja",font = ("Courier",15,"bold"),bg="light green", command = a2_correct).grid(row=5,column=1)
    Button(frame2, text = "Adis Ababa",font = ("Courier",15,"bold"),bg="light yellow", command = a2_wrong).grid(row=7,column=1)

    Label(frame3, text = "Which is the tallest mountain on earth?", font = ("Courier",20,"bold")).grid(row=2,column=2)
    Button(frame3, text = "Everest", font = ("Courier",15,"bold"),bg="blue", command = a3_correct).grid(row=3,column=1)
    Button(frame3, text = "Kilimanjaro",font = ("Courier",15,"bold"),bg="light green", command = a3_wrong).grid(row=5,column=1)
    Button(frame3, text = "K2",font = ("Courier",15,"bold"),bg="light yellow", command = a3_correct).grid(row=7,column=1)

    Label(frame4, text = "What is the output of np.arange(1,5)?", font = ("Courier",20,"bold")).grid(row=2,column=2)
    Button(frame4, text = "[1,2,3,4]", font = ("Courier",15,"bold"),bg="blue", command = a4_correct).grid(row=3,column=1)
    Button(frame4, text = "[0,1,2,3,4]",font = ("Courier",15,"bold"),bg="light green", command = a4_wrong).grid(row=5,column=1)
    Button(frame4, text = "[1,2,3,4,5]",font = ("Courier",15,"bold"),bg="light yellow", command = a4_wrong).grid(row=7,column=1)

    Label(frame5, text = "What is the output of 13*6?", font = ("Courier",20,"bold")).grid(row=2,column=2)
    Button(frame5, text = "35", font = ("Courier",15,"bold"),bg="blue", command = a5_wrong).grid(row=3,column=1)
    Button(frame5, text = "77",font = ("Courier",15,"bold"),bg="light green", command = a5_wrong).grid(row=5,column=1)
    Button(frame5, text = "78",font = ("Courier",15,"bold"),bg="light yellow", command = a5_correct).grid(row=7,column=1)


# To display the right or wrong choices
def a1_correct():
    Label(frame1, text = "correct", font = ("Courier",25,"bold"),bg="green",fg="yellow").grid(row=1,column=2)
    Label(frame1, text = "marks obtained:1", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a1_wrong():
    Label(frame1, text = "wrong", font = ("Courier",25,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame1, text = "marks obtained:0", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a2_correct():
    Label(frame2, text = "correct", font = ("Courier",25,"bold"),bg="green",fg="yellow").grid(row=1,column=2)
    Label(frame2, text = "marks obtained:1", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a2_wrong():
    Label(frame2, text = "wrong", font = ("Courier",25,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame2, text = "marks obtained:0", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a3_correct():
    Label(frame3, text = "correct", font = ("Courier",25,"bold"),bg="green",fg="yellow").grid(row=1,column=2)
    Label(frame3, text = "marks obtained:1", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a3_wrong():
    Label(frame3, text = "wrong", font = ("Courier",25,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame3, text = "marks obtained:0", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a4_correct():
    Label(frame4, text = "correct", font = ("Courier",25,"bold"),bg="green",fg="yellow").grid(row=1,column=2)
    Label(frame4, text = "marks obtained:1", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a4_wrong():
    Label(frame4, text = "wrong", font = ("Courier",25,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame4, text = "marks obtained:0", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a5_correct():
    Label(frame5, text = "correct", font = ("Courier",25,"bold"),bg="green",fg="yellow").grid(row=1,column=2)
    Label(frame5, text = "marks obtained:1", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)

def a5_wrong():
    Label(frame5, text = "wrong", font = ("Courier",25,"bold"),bg="red",fg="yellow").grid(row=1,column=2)
    Label(frame5, text = "marks obtained:0", font = ("Courier",25,"bold"),bg="black",fg="white").grid(row=1,column=3)
  
quiz(var)
a.pack()
a.mainloop()

