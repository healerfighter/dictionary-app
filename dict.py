from tkinter import *
from PIL import Image,ImageTk
import json
from difflib import get_close_matches
data_load=json.load(open("dictionary.json"))
def search_word(word):
    if word in data_load:
        meaning.delete(1.0,END)
        meaning.config(fg="black")
        meaning.insert(END,data_load[word])
    elif len(get_close_matches(word,data_load.keys()))>0:
        meaning.delete(1.0,END)
        meaning.config(fg="black")
        meaning.insert(END,"were you finding {} and meaning is:{}".format(get_close_matches(word,data_load.keys())[0],data_load[get_close_matches(word,data_load.keys())[0]]))
        final=get_close_matches(word,data_load.keys())
root=Tk()
root.title("MY OWN DICTIONARY")
image=Image.open("Add a heading.png")
image_picture=ImageTk.PhotoImage(image)
dest_pic=Label(root,image=image_picture)
dest_pic.pack()

a=StringVar()
word1=Entry(root,textvariable=a,background="lightblue",fg="black",font=("arial",20,"bold"))
word1.place(relx=.185,rely=.83,relheight=.13,relwidth=.60)
button=Button(root,text="search",command=lambda:search_word(a.get()),background="red",fg="white",font=("arial",20,"bold"))
button.place(relx=0.70,rely=0.83,relwidth=0.10,relheight=0.13)
meaning=Text(root,background="white",font=("arial",10,"bold"))
meaning.place(relx=0.200,rely=0.03,relheight=0.16,relwidth=0.63)
root.mainloop()