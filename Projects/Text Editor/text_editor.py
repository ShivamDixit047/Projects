#!/usr/bin/python3
from tkinter import *
from tkinter.filedialog import *
import os

filename = None
filepath = None

def newFile():
	global filename
	filename = 'Untitled'
	text.delete(0.0,END)

def saveFile():
	global filename
	global filepath
	if filepath!=None:
		filename = os.path.basename(filepath)
	t = text.get(0.0, END)
	f = open(filename, 'w')
	f.write(t)
	f.close()

def saveAs():
	f = asksaveasfile(mode= 'w', defaultextension='.txt')
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="OOPS!", message = "unable to save file...")

def openFile():
	global filepath
	f = askopenfile(mode = 'r')
	filepath = str(os.path.abspath(f.name))
	t = f.read()
	text.delete(0.0,END)
	text.insert(0.0, t)

root = Tk()
root.title("Text Editor.")
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)

text = Text(root, width = 400, height = 400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Open',command=openFile)
filemenu.add_command(label = 'Save', command=saveFile)
filemenu.add_command(label= 'Save As...', command = saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File',menu=filemenu)

root.config(menu=menubar)
root.mainloop()