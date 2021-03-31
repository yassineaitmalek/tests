from tkinter import *
from math import *

c=Tk()
c.title("scientific calculator")
c.configure(background="grey")
c.resizable(width=False , height=False)
c.geometry("480x568+0+0")


ca=Frame(c)
ca.grid()

txtdisplay=Entry(ca, font=('arial',20,'bold'),bg='grey',bd=30 ,width=29,justify=RIGHT)
txtdisplay.grid(row=0 , column=0, columnspan=4,pady=1)
txtdisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(ca,width=6 , height=2,font=('arial',20,'bold') , bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        i=i+1
        
        
#========MENU============

def iexit():
    iexit =tkinter.Message.askyesno("scientific calculator",'confirm if you want to exit')
    if iexit >0 :
        c.destroy()
        return
        
def scientific() :
    c.resizable(width=False , height=False)
    c.geometry("944x568+0+0")

def standard() :
    c.resizable(width=False , height=False)
    c.geometry("480x568+0+0")



menubar = Menu(ca)

filemenu = Menu(menubar ,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="standard",command=standard)
filemenu.add_command(label="scientific",command=scientific)
filemenu.add_separator()
filemenu.add_command(label="exit" , command=iexit)

editmenu = Menu(menubar ,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="cut")
editmenu.add_command(label="copy")
editmenu.add_separator()
editmenu.add_command(label="past")

helpmenu = Menu(menubar ,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help")

c.configure(menu=menubar)
c.mainloop()
