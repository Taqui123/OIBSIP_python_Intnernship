import string
import random
from tkinter import *

root = Tk()
root.title("Random_Pass_Generator")
root.geometry("350x250")
root.config(bg="silver")
root.resizable(False, False)

image_icon = PhotoImage(file="Ricon.png")
root.iconphoto(False, image_icon)

label_title = Label(root, text="please choose the Strength you Want!!",
                    bg='lightgreen', fg='red', font='Arial 13')
label_title.pack()


def selected():
    selected_choice = choice.get()


choice = IntVar()
rb1 = Radiobutton(root, text="weak Password", variable=choice, value=1, command=selected)
rb1.pack()
rb1.config(bg="silver")

rb2 = Radiobutton(root, text="Average Password", variable=choice, value=2, command=selected)
rb2.pack()
rb2.config(bg="silver")

rb3 = Radiobutton(root, text="Strong Password", variable=choice, value=3, command=selected)
rb3.pack()
rb3.config(bg="silver")

label_pass = Label(root, text="Choose the Length of your Password")
label_pass.pack(pady=10)
label_pass.config(bg="silver")

val = IntVar()
pass_len = Spinbox(root, from_=6, to=24, textvariable=val, width=15)
pass_len.pack()


def backcall():
    result.config(text=passgen())


lock = Button(root, text="Generate Password", command=backcall)
lock.pack(pady=10)

result = Message(root, text="", relief=RAISED, width=200, font=18)
result.pack()
result.config(bg="silver", fg="red", font="Arial")


weak = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
Strong = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(weak, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(Strong, val.get()))
    else:
        return "".join("please select password strength!!!")


root.mainloop()
