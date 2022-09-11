import tkinter as tk
 
# configure window and its dimension
# make window fixed
root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
 
def change():
   
    # change color after button triggers
    color = choice.get()  # tkinter variable get method
    canva.configure(bg=color)
 
choice = tk.StringVar(root, "purple")
 
# create canva to play with background colors
canva = tk.Canvas(root, bg="purple")
canva.place(x=-1, y=-1, width=300, height=300)
 
# create 5 Radio Buttons
for option in ["Brown", "Black", "Orange", "Green", "Red"]:
    tk.Radiobutton(root, text="%s" % option, value=option,
                   variable=choice, padx=10, pady=5).pack()
 
# button to trigger colour change
tk.Button(text="Change BG", command=change, bd=4).place(x=100, y=180)
root.mainloop()