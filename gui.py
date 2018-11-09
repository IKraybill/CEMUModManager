import shutil
from tkinter import *
import tkinter.messagebox
import os


class MenuBar(Menu):
    def __init__(self, master):
        Menu.__init__(self, master)

        file_menu = Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project...", command=print_message)


class PathWindow(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)

        self.wm_title("Path Settings")


class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        path_selection = PathWindow(self)


def print_message():
    print("Wow, this actually worked!")


root = Tk()
app = MainWindow(root)

menu_bar = MenuBar(root)
root.config(menu=menu_bar)

root.mainloop()
