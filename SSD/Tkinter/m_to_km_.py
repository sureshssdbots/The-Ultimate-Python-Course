import tkinter as tk
from tkinter import ttk

def mtokm():
    x = inputvar.get()
    y = x/1000
    outputvar.set(y)
    
window = tk.Tk()
window.title('App')
window.geometry('400x400')

heading = ttk.Label(master= window, text = 'm to km converter', font = ('Arial', 12))
heading.pack()

inputvar = tk.IntVar()
frame = ttk.Frame(master= window) 
inputbox = ttk.Entry(master= frame, textvariable=inputvar)
button = ttk.Button(master = frame, text = 'Convert', command= mtokm)
inputbox.pack(side = 'left' , padx=10)
button.pack(side= 'left')
frame.pack(pady=20)

outputvar = tk.StringVar()
output = ttk.Label(master= window, text= 'Calculated value', textvariable= outputvar)
output.pack()

window.mainloop()
