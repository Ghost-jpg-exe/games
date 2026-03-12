import time 
import tkinter as t
import pyautogui as p 
from os import path 
radio=0 
RadioRecord=path.dirname(__file__) 
if path.exists(f'{RadioRecord}/RADIO RECORD.txt') :
    with open (f'{RadioRecord}/RADIO RECORD.txt','r') as file :
        radio=file.readline()
class Osn:
    def __init__(self):
        self.lopata=1
        self.y=1
        self.shar=1
        self.h1=1
        self.h2=1
    def skokorost(self):
        x,y,x1,y1=Excel.coords(self.lopata) 
        if y<=0 and self.h1:
            self.y=0
            self.h1=0
        if y1>=600 and self.h2:
            self.y=0
            self.h2=0
        Excel.move(self.lopata,0,self.y)
class Player1(Osn):
    def __init__(self):
        super().__init__()
        self.lopata=Excel.create_rectangle(10,250,30,350,fill='white')
        self.y=2
        self.h1=1
        self.h2=1
        Excel.bind_all('<KeyPress>',self.dviz)
        Excel.bind_all('<KeyRelease>',self.stop)
    def dviz(self,sobitie):
        if sobitie.keysym=='w':
            self.y=-2
            self.h1=1
        if sobitie.keysym=='s':
            self.y=2
            self.h2=1
    def stop(self,sobitie):
        if sobitie.keysym in ['w','s']:
            self.y=0
class Player2(Osn):
    def __init__(self):
        super().__init__()
        self.lopata=Excel.create_rectangle(590,250,570,350,fill='white')
        self.y=2
        self.h1=1
        self.h2=1
        Excel.bind_all('<KeyPress>',self.dviz1,add='+')
        Excel.bind_all('<KeyRelease>',self.stop2,add='+')
    def dviz1(self,sobitie1):
        if sobitie1.keysym=='Up':
            self.y=-2
            self.h1=1
        if sobitie1.keysym=='Down':
            self.y=2
            self.h2=1
    def stop2(self,sobitie1):
        if sobitie1.keysym in['Up','Down']:
            self.y=0
class mahik:
    def __init__(self):
        self.shar=Excel.create_oval(290,290,310,310,fill='White')
        self.x=2
        self.y=2
        self.otbitie=0
        self.nadpis=Excel.create_text(190,15,text=f'Счёт равен:{self.otbitie}',fill='White',font=('ariel',20))
        self.record=Excel.create_text(410,15,text=f'Рекорд равен:{radio}',fill='White',font=('ariel',20))
    def skokorost(self):
        Excel.move(self.shar,self.x,self.y)
        x,y,x1,y1=Excel.coords(self.shar)
        if x<=0:
            p.alert('GAME OVER')
            if self.otbitie>int(radio):
                with open(f'{RadioRecord}/RADIO RECORD.txt','w') as file:
                    file.write(f'{self.otbitie}')
            exit()
        elif y<=0:
            self.y=2
        elif x1>=600:
            p.alert('GAME OVER')
            if self.otbitie>int(radio):
                with open(f'{RadioRecord}/RADIO RECORD.txt','w') as file:
                    file.write(f'{self.otbitie}')
            exit()
        elif y1>=600:
            self.y=-2 
        self.ydar2(one.lopata)
        self.ydar(two.lopata)
    def ydar(self,lopata):
        x,y,x1,y1=Excel.coords(self.shar)
        x2,y2,x3,y3=Excel.coords(lopata)
        y=(y+y1)/2
        if self.x==2:
            if y>=y2 and y<=y3 and x1==x2:
                self.x=-2
                self.otbitie+=1 
                Excel.itemconfig(self.nadpis,text=f'Счёт равен:{self.otbitie}')
    def ydar2(self,lopata):
        x,y,x1,y1=Excel.coords(self.shar)
        x2,y2,x3,y3=Excel.coords(lopata)
        y=(y+y1)/2
        if self.x==-2:
            if y2<=y and y3>=y and x==x3:
                self.x=2
                self.otbitie+=1 
                Excel.itemconfig(self.nadpis,text=f'Счёт равен:{self.otbitie}')           
ikran=t.Tk()
ikran.title('i')
ikran.resizable(False,False)
Excel=t.Canvas(ikran,width=600,height=600,bg='black')
Excel.pack()
one=Player1()
two=Player2() 
three=mahik()
while True:
    Excel.update() 
    Excel.update_idletasks()
    one.skokorost()
    two.skokorost()
    three.skokorost()
    time.sleep(0.02)


























t.mainloop()