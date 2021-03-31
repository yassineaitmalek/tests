from tkinter import *

def click():
    a=textenetry.get()

c=Tk()
c.title("code generator")
c.configure(background="grey")
c.resizable(width=False , height=False)
c.geometry("480x480+0+0")

Label(c,text="Entrer la longeur du code : ",bg='grey',fg='black',font=('none' , 12,"bold")).grid(row=0,column=0,sticky=W)

textentry1=Entry(c,width=20,bg="grey")
textentry1.grid(row=0,column=1,sticky=W)
textentry2=Entry(c,width=20,bg="grey")
textentry2.grid(row=1,column=1,sticky=W)

Button(c,text='generate',width=20,bg='grey',command=click).grid(row=3,column=1,sticky=W)

Label(c,text="Les codes : ",bg='grey',fg='black',font=('none' , 12,"bold")).grid(row=4,column=0,sticky=W)

output=Text(c,width=60,heith=6,wrap=WORD,background="grey")
output.grid(row=4,column=0,sticky=W)




c.mainloop()
