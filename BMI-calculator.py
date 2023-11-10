import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI-Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)


def BMI_repo():
    h = float(Height.get())
    w = float(Weight.get())

    m = h / 100
    bmi = round(float(w / m ** 2), 1)
    # print(bmi)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text="Under-Weight!")
        label3.config(text="Embrace a Healthy \nJourney to Thrive!!", fg="orange")

    elif 18.5 < bmi <= 24.9:
        label2.config(text="Normal_Weight!")
        label3.config(text="Maintain the Balance, \nLive Life to the Fullest!!", fg="green")

    elif 25 < bmi <= 29.9:
        label2.config(text="Over-Weight!")
        label3.config(text="Take Charge of Your Wellness, \nYou Can Do It!!", fg="red")

    else:
        label2.config(text="Obese!")
        label3.config(text="Your Health, Your Future \n- Time for Transformation!!!", fg="red")


image_icon = PhotoImage(file="Icon.png")
root.iconphoto(False, image_icon)

top = PhotoImage(file="top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)


Label(root, width=72, height=18, bg="lightgreen").pack(side=BOTTOM)


box = PhotoImage(file="box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="lightgreen").place(x=20, y=310)

current_value = tkinter.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_moved(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("man.png"))
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2

style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale",
                   command=slider_moved, variable=current_value)

slider.place(x=80, y=250)

current_value2 = tkinter.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_moved2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale",
                    command=slider_moved2, variable=current_value2)

slider2.place(x=300, y=250)


# Add a label for "Height"
height_label = Label(root, text="Height (in cm)", font="Lato 12 bold", bg="white")
height_label.place(x=40, y=75)

weight_label = Label(root, text="Weight (in kg)", font="Lato 12 bold", bg="white")
weight_label.place(x=260, y=75)

Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font="Arial 50", bg="#fff", fg="#000", bd=0,
               justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font="Arial 50", bg="#fff", fg="#000", bd=0,
               justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

secondimage = Label(root, bg="lightgreen")
secondimage.place(x=70, y=530)

Button(root, text="Calculate BMI", width=15, height=2, font="Arial 12 bold",
       bg="#1f6e68", fg="white", command=BMI_repo).place(x=290, y=340)

label1 = Label(root, font="Arial 60 bold", bg="lightgreen", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="Arial 18 bold", bg="lightgreen", fg="#3b3a3a")
label2.place(x=250, y=430)

label3 = Label(root, font="Arial 13 bold", bg="lightgreen")
label3.place(x=200, y=500)

root.mainloop()
