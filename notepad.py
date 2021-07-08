from tkinter import *
from tkinter import filedialog
import time

window = Tk()
window.title('Notepad')
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

my_menu = Menu(window)
window.config(menu=my_menu)
global_filename = ''
def open_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"),("all files", "*.*")))
    return filename

def our_command():
    my_label = Label(window, text="Clicked!!").pack()

def get_opened_file_name():
    global_filename = open_file()
    return global_filename

def save_opened_file():
    text = textArea.get("1.0", END)
    global_filename = get_opened_file_name()
    f = open(global_filename, "w")
    f.write('')
    time.sleep(1)
    f.write(text)

def open_edit_file():
    filename = get_opened_file_name()
    with open(file=filename) as file:
        data = file.read()        
        textArea.insert(END, data)    

file_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New",command=our_command)
file_menu.add_command(label="Open",command=open_edit_file)
file_menu.add_command(label="Save",command=save_opened_file)

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
