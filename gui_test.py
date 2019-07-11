import tkinter as tk
from tkinter import *

# root = Tk()
window = tk.Tk()
str_var = tk.StringVar()
window.title('my windows')
window.geometry('450x300')
# l = tk.Label(window, textvariable=str_var, bg='green', font=('consolas', 12), width=15,
#              height=3)
# l.pack() # locate the lable
#
# on_hit = False
#
#
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         str_var.set('you hit me')
#         on_hit = True
#     else:
#         on_hit = False
#         str_var.set('')

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)

e = tk.Entry(window,show=None,)
e.pack()



b1 = tk.Button(window, text = 'insert point', width = 15, height = 2, command= insert_point)
b1.pack(fill=X)
b2 = tk.Button(window, text = 'insert end', width = 15, height = 2, command= insert_end)
b2.pack()
t = tk.Text(window, height=2,)
t.pack()

window.mainloop()