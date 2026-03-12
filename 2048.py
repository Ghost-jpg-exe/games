import tkinter as t
import pyautogui as p
import random as r
import sqlalchemy as s
from pygame_menu.widgets.widget import table
from sqlalchemy import create_engine,Column,String
from sqlalchemy.orm import sessionmaker,declarative_base
engine = create_engine('sqlite:///igra2048.db')
base = declarative_base()
class Table(base):
    __tablename__='tagil'
    id = Column(s.Integer, primary_key=True)
    nickname = Column(s.String)
    score = Column(s.Integer)
base.metadata.create_all(engine)
session=sessionmaker(bind=engine)
localssession=session()
ikran=t.Tk()
ikran.geometry('800x800')
ikran.resizable(0,0)
kolst=t.Canvas(ikran,width=800,height=800)
kolst.pack()
slovar={'':'#ffffff',
        2:'#540cf0',
        4:'#54b0b0',
        8:'#e3ba54',
        16:'#ff00d5',
        32:'#44cf49',
        64:'#533fd9',
        128:'#ba6d56',
        256:'#f9e8e9',
        512:'#db2392',
        1024:'#d9d9d9',
        2048:'#5e5e3a'}
spisok=[[[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]],
        [[],[],[],[]]]
def setspawn():
    global spisok
    empty=0
    for i in range(0,4):
        for j in range(0,4):
            if spisok[i][j][2]=='':
                empty+=1
    if empty!=0:
        tt=r.randint(0,3)
        gg=r.randint(0,3)
        while spisok[tt][gg][2]!='':
            gg=r.randint(0,3)
            tt=r.randint(0,3)
        spisok[tt][gg][2]=2
        kolst.itemconfig(spisok[tt][gg][0],fill=slovar[spisok[tt][gg][2]])
        kolst.itemconfig(spisok[tt][gg][1],text=spisok[tt][gg][2])
def vverx(e):
    global spisok
    for o in range(2):
        for x in range(4):
           for y in [3,2,1]:
                if spisok[y][x][2]==spisok[y-1][x][2]!='':
                    spisok[y-1][x][2]*=2
                    kolst.itemconfig(spisok[y-1][x][0], fill=slovar[spisok[y-1][x][2]])
                    kolst.itemconfig(spisok[y-1][x][1], text=spisok[y-1][x][2])
                    spisok[y][x][2]=''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
                elif spisok[y-1][x][2]=='' and spisok[y][x][2]!='':
                    spisok[y-1][x][2]=spisok[y][x][2]
                    kolst.itemconfig(spisok[y - 1][x][0], fill=slovar[spisok[y - 1][x][2]])
                    kolst.itemconfig(spisok[y - 1][x][1], text=spisok[y - 1][x][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
    setspawn()
def vniz(e):
    global spisok
    for o in range(2):
        for x in range(4):
            for y in [0, 1, 2]:
                if spisok[y][x][2] == spisok[y + 1][x][2] != '':
                    spisok[y + 1][x][2] *= 2
                    kolst.itemconfig(spisok[y + 1][x][0], fill=slovar[spisok[y + 1][x][2]])
                    kolst.itemconfig(spisok[y + 1][x][1], text=spisok[y + 1][x][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
                elif spisok[y + 1][x][2] == '' and spisok[y][x][2] != '':
                    spisok[y + 1][x][2] = spisok[y][x][2]
                    kolst.itemconfig(spisok[y + 1][x][0], fill=slovar[spisok[y + 1][x][2]])
                    kolst.itemconfig(spisok[y + 1][x][1], text=spisok[y + 1][x][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
    setspawn()
def vpravo(e):
    global spisok
    for o in range(2):
        for y in range(4):
            for x in [0,1,2]:
                if spisok[y][x][2] == spisok[y][x + 1][2] != '':
                    spisok[y ][x + 1][2] *= 2
                    kolst.itemconfig(spisok[y][x + 1][0], fill=slovar[spisok[y][x + 1][2]])
                    kolst.itemconfig(spisok[y][x + 1][1], text=spisok[y][x + 1][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
                elif spisok[y][x + 1][2] == '' and spisok[y][x][2] != '':
                    spisok[y][x + 1][2] = spisok[y][x][2]
                    kolst.itemconfig(spisok[y][x + 1][0], fill=slovar[spisok[y][x + 1][2]])
                    kolst.itemconfig(spisok[y][x + 1][1], text=spisok[y][x + 1][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
    setspawn()
def vlevo(e):
    global spisok
    for o in range(2):
        for y in range(4):
            for x in [3,2,1]:
                if spisok[y][x][2] == spisok[y][x - 1][2] != '':
                    spisok[y][x - 1][2] *= 2
                    kolst.itemconfig(spisok[y][x - 1][0], fill=slovar[spisok[y][x - 1][2]])
                    kolst.itemconfig(spisok[y][x - 1][1], text=spisok[y][x - 1][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
                elif spisok[y][x - 1][2] == '' and spisok[y][x][2] != '':
                    spisok[y][x - 1][2] = spisok[y][x][2]
                    kolst.itemconfig(spisok[y][x - 1][0], fill=slovar[spisok[y][x - 1][2]])
                    kolst.itemconfig(spisok[y][x - 1][1], text=spisok[y][x - 1][2])
                    spisok[y][x][2] = ''
                    kolst.itemconfig(spisok[y][x][0], fill=slovar[spisok[y][x][2]])
                    kolst.itemconfig(spisok[y][x][1], text=spisok[y][x][2])
    setspawn()
def ochki():
    ochiki=0
    for o in range(4):
        for y in range(4):
            ochiki += spisok[y][o][2]
    return ochiki
def control(ivent):
    if proverka():
        if ivent.keysym == 'Left':
            vlevo(ivent)
        elif ivent.keysym == 'Right':
            vpravo(ivent)
        elif ivent.keysym == 'Up':
            vverx(ivent)
        elif ivent.keysym == 'Down':
            vniz(ivent)
def proverka():
    for o in range(4):
        for y in range(4):
            if spisok[y][o][2] == '':
                return True
    for i in range(4):
        for j in range(3):
            if spisok[i][j][2] == spisok[i][j + 1][2]:
                return True
    for i in range(4):
        for y in range(3):
            if spisok[y][i][2] ==spisok[y+1][i][2]:
                return True
    return False
kolst.create_line(200,0,200,800)
kolst.create_line(400,0,400,800)
kolst.create_line(600,0,600,800)
kolst.create_line(0,200,800,200)
kolst.create_line(0,400,800,400)
kolst.create_line(0,600,800,600)
for x in range(4):
    for y in range(4):
        rect=kolst.create_rectangle(x*200,y*200,(x+1)*200,(y+1)*200,fill=slovar[''])
        spisok[y][x].append(rect)
        text=kolst.create_text(x*200+100,y*200+100,text='',font=('times',20))
        spisok[y][x].append(text)
        spisok[y][x].append('')
ikran.bind('<KeyPress>',control)
setspawn()
setspawn()
t.mainloop()