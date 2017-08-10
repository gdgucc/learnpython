import tkinter as tk


root = tk.Tk()

# top frame ...
tFrame = tk.Frame(root)
tFrame.pack()

# bottom frame ...
bFrame = tk.Frame(root)
bFrame.pack(side=tk.BOTTOM)

# adding widgets
#  buttons ...
btn1 = tk.Button(tFrame, text="Button 1", fg="red")
btn2 = tk.Button(tFrame, text="Button 2", fg="blue")
btn3 = tk.Button(tFrame, text="Button 3", fg="green")
btn4 = tk.Button(bFrame, text="Button 4", fg="purple")

# packing widgets same as displaying them ....
btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)
btn3.pack(side=tk.LEFT)
btn4.pack(side=tk.BOTTOM)


root.mainloop()