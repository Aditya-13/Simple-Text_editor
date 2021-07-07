from tkinter import *
import os

window = Tk()
window.title('Notepad')
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

my_menu = Menu(window)
window.config(menu=my_menu)

def our_command():
    my_label = Label(window, text="Clicked!!").pack()

def get_saved_text():
    def get_file_name(): 
        window1 = Toplevel(window)
        window1.title('Enter File Name ')
        label = Label(window1, text='Enter File Name To Save:', font="Montserrat 10")
        label.pack()
        textArea1 = Entry(window1, bg="white", fg="black", font="Lato 12", )
        textArea1.pack()
        label1 = Label(window1, text=' ', font="Montserrat 10")
        label1.pack()
        save_button = Button(window1, text='Save', font="Lato 10", command=textArea1.get())
        save_button.pack()
        label2 = Label(window1, text=' ', font="Montserrat 10")
        label2.pack()
        exit_button = Button(window1, text='Exit', font="Lato 10", command=window1.destroy)
        exit_button.pack()
        window1.geometry('400x200')
        return textArea1.get
    get_file_name()
    text = textArea.get("1.0",END)
    print(get_file_name())
    return text


file_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New",command=our_command)
file_menu.add_command(label="Open",command=our_command)
file_menu.add_command(label="Save",command=get_saved_text)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=our_command)
edit_menu.add_command(label="Copy",command=our_command)

option_menu = Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Exit",command=window.quit)


textArea = Text(window, width=width, bg="white", fg="black", font="Lato 14",)
textArea.pack()

window.mainloop()