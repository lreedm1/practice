# credit to source - https://dev.to/insidiousthedev/make-a-simple-text-editor-using-python-31bd

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
'''
import fomrat_menu
import help_menu
'''

#create the main window
root = Tk()
root.title("Text Editor")

#define the size of the window
root.geometry("800x600")
root.minsize(300,300)


#define the scrollbar behavior
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


#define the text widget
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH, expand=1)
scrollbar.config(command=text.yview)

#define the font
font = Font(family="Arial", size=14)
text.config(font=font)


#create the menu bar
menubar = Menu(root)


#add menus to the menu bar
file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
#format_menu.main(root, text, menubar)
#help_menu.main(root, text, menubar)

#run the main window
root.mainloop()