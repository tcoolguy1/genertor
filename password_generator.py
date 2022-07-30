from tkinter import*
import random

root = Tk()
root.title("Password generator")
root.geometry("400x400")

label = Label(root)
array_3d =[[["1,3,7,6,2"],["tree","school","sheeesh","cloud","dogfish"],["$","*","#","%","&"]]]

def new_password():
    random_1 = random.randint(0,4)
    random_2 = random.randint(0,4)
    random_3 = random.randint(0,4)
    letter_1 = str(array_3d[0][0][random_1])
    letter_2 = (array_3d[0][0][random_2])
    letter_3 = (array_3d[0][0][random_3])
    label["text"] = letter_1+""+letter_2+""+letter_3
btn = Button(root, text = "Generate password", command = new_password)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
