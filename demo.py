from tkinter import *
from tkinter import filedialog
import easygui
from PIL import ImageTk,Image

root = Tk()
root.geometry('500x500')
root.title("Logo Recognition")

# def open():
#     file = easygui.fileopenbox()
#     if file is not None:
#         content = file.read()
#         print(content)

def open():
    global my_image
    root.filename = filedialog.askopenfilename(title="Select a file",filetypes=(("jpg files","*.jpg"),("all types","*.*")))
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image)
    my_image_label.place(x=80, y=200)

label_0 = Label(root, text="Logo Recognition",width=20,font=("bold",20))
label_0.place(x=90, y=53)

b1 = Button(root, text="Select Picture",width=12,command=open)
b1.place(x=80, y=130)

root.mainloop()