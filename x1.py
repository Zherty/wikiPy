from tkinter import *
from tkinter import messagebox
import wikipedia

win = Tk()

def poisk():
    en = entry.get()
    wikipedia.set_lang("en")
    wiki_poisk = wikipedia.summary(en)
    messagebox.showinfo(title='Wiki',message=wiki_poisk)

win.title("Wiki")
win.geometry('500x500')
win.resizable(width=False,height=False)

entry = Entry(win, width=400,bd=10, font=30)
entry.pack()

button_poisk = Button(win,width=100, height=100,text="find", font=100,activebackground='grey',command=poisk)
button_poisk.pack()

win.mainloop()

#wikipedia.set_lang("ru")
#print(wikipedia.summary("Нью Йорк"))