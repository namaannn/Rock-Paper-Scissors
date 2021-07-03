#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
r=Tk()
r.geometry('400x450')
r.resizable(0,0)
r.title('ROCK-PAPER-SCISSOR')
r.configure(bg='seashell3')
Label(r, text='Rock Paper Scissor', font ='arial 20', bg= 'seashell2').pack()
n1=StringVar()
Label(r, text='Choose among rock, paper, scissor', font='arial 15', bg='seashell2').place(x=25,y=50)
Entry(r,font='arial 15', textvariable=n1, bg='antiquewhite2').place(x=80,y=125)
comp=random.randint(1,3)
if(comp==1):
    comp='rock'
elif(comp==2):
    comp='paper'
else:
    comp='scissors'

Ans=StringVar()
def game():
    n=n1.get()
    if(n==comp):
        Ans.set('Its a draw')
    elif(n=='rock' and comp=='paper'):
        Ans.set('Computer selects paper and wins')
    elif(n=='rock' and comp=='scissors'):
        Ans.set('You win as computer selects scissors')
    elif(n=='paper' and comp=='scissors'):
        Ans.set('Computer selects scissors and wins')
    elif(n=='paper' and comp=='rock'):
        Ans.set('You win as computer selects rock')
    elif(n=='scissors' and comp=='rock'):
        Ans.set('Computer selects rock and wins')
    elif(n=='scissors' and comp=='paper'):
        Ans.set('You win as computer selects paper')
    else:
        Ans.set('Invalid choice')
        
def Reset():
    Ans.set("")
    n1.set("")

def Exit():
    r.destroy()

Entry(r, font = 'arial 10 ', textvariable = Ans, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
Button(r, font = 'arial 13 ', text = 'PLAY'  ,padx =5, bg ='seashell4' ,command = game).place(x=150,y=190)
Button(r, font = 'arial 13 ', text = 'RESET'  ,padx =5, bg ='seashell4' ,command = Reset).place(x=70,y=310)
Button(r, font = 'arial 13 ', text = 'EXIT'  ,padx =5, bg ='seashell4' ,command = Exit).place(x=230,y=310)
r.mainloop()


# In[ ]:




