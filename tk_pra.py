from tkinter import *
from tkinter.ttk import*
#window = Tk()
#tex= StringVar()
#tex1=StringVar()
#opt1 = IntVar()
#def clear_text(tex):
    #tex.set("")
#def label_change(tex):
    #tex.set("good job")
#def end():
    #window.destroy()
#def incognito():
    #if opt1.get() == 0:
        #s.theme_use("clam")
    #else:
        #s.theme_use("classic")
#tex.set("Hi I am Ted, change this sentence to continue")
#tex1.set("futile attempt")
#label1 = Label(window, textvariable=tex, width=20)
#label1.pack(side="top")
#entry1 = Entry(window, width = 25, text= "try me", textvariable=tex1)
#entry1.pack(side="top")
#button1 = Button(window, text="Click me", command=lambda: label_change(tex))
#s= Style()
#button2 = Button(window, text="destroy EVERYTHING", command=lambda: clear_text(tex1))
#button2.pack(side="left")
#s.configure('Tbutton', font='helvetica 24', foreground='blue')
#s.theme_use('clam')
#button1.pack(side="right")
#button3 = Button(window, text="Close me", command=lambda: end())
#button3.pack(side="bottom")
#check1 = Checkbutton(window, text="incognito", variable=opt1, command=lambda: incognito(), onvalue=1, offvalue=0)
#check1.pack(side="bottom")
#window.mainloop()

#import tkinter as tk

#root = tk.Tk()

#v = tk.IntVar()

#tk.Label(root, 
        #text="""Choose a 
#programming 
#language:""",
        #justify = tk.CENTER,
        #padx = 20).pack()

#tk.Radiobutton(root, 
               #text="Python",
               #padx = 20, 
               #variable=v, 
               #value=1).pack(anchor=tk.W)

#tk.Radiobutton(root, 
               #text="Perl",
               #padx = 20, 
               #variable=v, 
               #value=2).pack(anchor=tk.W)

#root.mainloop()

#from tkinter import *
#from tkinter import messagebox
#master = Tk()
#master.geometry('500x200')
#def func():
    #messagebox.showinfo( "Hello Educba", "Press any key on the keyboard")
#b1 = Button( master, text='Click me for next step', background = 'Cyan', fg = '#000000', command = func)
#b1.pack()
#def Keyboardpress( key):
    #key_char = key.char
    #print( key_char, 'key button is pressed on the keyboard')
#master.bind( '<Key>', lambda i : Keyboardpress(i))
#master.mainloop()

#from tkinter import *
#from tkinter.ttk import * 
#def add_one():
    #value.set(value.get()+1)

#def wow(event):
    #label2.config(text="WWWWOOOOWWWW")

#window = Tk()
#value = IntVar(0)
#label = Label(window, textvariable=value)
#label.pack()
#label2 = Label(window)
#label2.pack()
#button = Button(window, text="Add one", command=add_one)
#button.bind("<Shift-Button-3>", wow)
#button.pack()
#window.mainloop()

#from tkinter import *
#from tkinter.ttk import * 
#window = Tk()
#for label_num in range(6):
    #button = Button(window, text="Button" + str(label_num))
    #button.grid(row=label_num // 2, column=label_num % 3)
    #if label_num==1:
        #button.grid(columnspan=2, sticky="we")
    #elif label_num==3:
        #button.grid(rowspan=2, sticky="ns")
#window.columnconfigure(1, weight=1)
#window.rowconfigure(1, weight=1)
#window.rowconfigure(2, weight=1)
#window.mainloop()

#from tkinter import *

#from tkinter.ttk import *

#board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

#def add_text(text, char):
    #text.set(text.get()+char)
#def clear_text(text):
    #text.set("")    
#window = Tk()
#window.title("lab1_q3")
#tex = StringVar()

#label = Label(window, width=24, textvariable=tex)
#label.grid(row=0, column=0, sticky="we")

#clear_button = Button(window, text="Clear", command=lambda: clear_text(tex))
#clear_button.grid(row=0, column=1)

#frame = Frame(window, borderwidth=4, relief=RAISED)
#frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=2, padx=2)

#for row in range(len(board)):
    #frame_row = Frame(frame)
    #frame_row.grid(row=row, column=0, columnspan=2)
    #for col in range(len(board[row])):
        #char = board[row][col]
        #button = Button(frame_row, text=char, width=2, command=lambda x=char: add_text(tex, x))
        #button.grid(row=row, column=col)

#window.columnconfigure(0, weight=1)
#window.rowconfigure(0, weight=1)
#frame.columnconfigure(0, weight=1)
#frame.rowconfigure(0, weight=1)
#s = Style()
#s.theme_use('alt')

#window.mainloop()


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

##def button_click(text, char):
    ##"""everytime I click the letter on the label 
    ##it moves on to the next one in sample"""
    ##if len(text) != 0:
        ##if char == text[0]:
            

board = ['lgehobuckz', 'qsyipfnam', 'jwxdrvt']
#ALPHABET = "abcdefghijklmnopqrstuvwxyz"
sample = "abcdef"
window = Tk()
window.title("lab2_q2")
tex = StringVar()
tex.set(sample[0])
label = Label(window, width=24, textvariable=tex, anchor=CENTER)
label.grid(row=0, column=0, sticky="we")
frame = Frame(window, borderwidth=4, relief=RAISED)
frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=2, padx=2)
for row in range(len(board)):
    frame_row = Frame(frame, height=32, width=32)
    frame_row.grid(row=row, column=0, columnspan=2)
    frame_row.pack_propagate(0)
    for col in range(len(board[row])):
        char = board[row][col]
        button = Button(frame_row, text=char, width=2)
        button.grid(row=row, column=col)

        
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
s = Style()
s.theme_use('alt')
window.mainloop()