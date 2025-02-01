
import tkinter as tk
from tkinter import ttk

window= tk.Tk()
window.title('SSD Studio')
window.geometry('200x200')

#frame 1
frame1 = ttk.Frame(window, borderwidth=5, relief='raised')
label1 = ttk.Label(frame1, text= 'Label 1', background='lightpink', anchor='center' )
label2 = ttk.Label(frame1, text= 'Label 2', background= 'lightblue', anchor='center')
label1.pack(fill='both', expand=True, side='left')
label2.pack(fill='both', expand=True, side='left')


# label3
label3 = ttk.Label(window, text= 'Label 3', background='darkgray', anchor='center')


# frame2
frame2 = ttk.Frame(window, borderwidth=5, relief='sunken')
frame3 = ttk.Frame(frame2)
frame4 = ttk.Frame(frame2, borderwidth=5, relief='ridge')

# style 
style = ttk.Style()
style.configure("TButton", font=("Arial", 8, 'bold'), padding=5, foreground="black", relief = 'solid')


button1 = tk.Button(frame3, text= 'Button 1', borderwidth=5, relief='raised')
button2 = ttk.Button(frame3, text= 'Button 2', style='TButton')
button3 = ttk.Button(frame3, text= 'Button 3')
button1.pack(expand=True, fill='both')
button2.pack(expand=True, fill='both')
button3.pack(expand=True, fill='both')



label4 = ttk.Label(frame4, text = 'Label 4', background= 'lightgreen', anchor='center')
label4.pack(fill= 'both', side='left', expand=True)



# Main layout
frame1.pack(expand=True, fill='both')
label3.pack(fill='both', expand=True)
frame3.pack(fill='both', side='left', expand=True)
frame4.pack(expand=True, fill='both', side= 'left')
frame2.pack(expand=True, fill='both')



window.mainloop()
