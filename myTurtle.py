import random
from tkinter.simpledialog import *

def getString():
    reStr=''
    reStr=askstring("문자열 입력","거북이가 쓸 문자열을 입력")
    return reStr

def getRGB():
    r,g,b=0,0,0
    r=random.random()
    g=random.random()
    b=random.random()
    return(r,g,b)

def getXYAS(swidth,sheight):
    x,y,angle,size=0,0,0,0
    x=random.randrange(-swidth//2,swidth//2)
    y=random.randrange(-sheight//2,sheight//2)
    angle=random.randrange(0,360)
    size=random.randrange(10,50)
    return [x,y,angle,size]