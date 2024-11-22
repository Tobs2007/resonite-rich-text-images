import time
import clipboard
import numpy as np
from PIL import Image
size=int(17)
start=time.time()
global stri1
stri1=""
global stri2
stri2=""
global stri3
stri3=""
global stri4
stri4=""
xsize=128
ysize=128
img=Image.open("AC.jpg")
imgres=img.resize((xsize,ysize))
ima= np.asarray(imgres)
imgres.save("output.png")



global colorold
colorold=[0,0,0]
def printcol(color,string):
    global stri1
    global stri2
    global stri3
    global stri4
    global colorold
    if string ==1:
        if colorold==color :
            stri1=stri1+"█"
        else:
            colorold=color
            stri1=stri1+"<color=#"+color+">"+"█"

    if string ==2:
        if colorold==color :
            stri2=stri2+"█"
        else:
            colorold=color
            stri2=stri2+"<color=#"+color+">"+"█"

    if string ==3:
        if colorold==color :
            stri3=stri3+"█"
        else:
            colorold=color
            stri3=stri3+"<color=#"+color+">"+"█"


    if string ==4:
        if colorold==color :
            stri4=stri4+"█"
        else:
            colorold=color
            stri4=stri4+"<color=#"+color+">"+"█"


def printQuarant(xb,xe,y,string):
    global stri1
    global stri2
    global stri3
    global stri4
    for x in range (xb,xe):
        for y in range(ysize):
            try:
                R,G,B,A=ima[x][y]
                
                print(ima[x][y])
                col=str(hex(int(R)))[2:4].zfill(2)+str(hex(int(G)))[2:4].zfill(2)+str(hex(int(B)))[2:4].zfill(2)+str(hex(int(A)))[2:4].zfill(2)
                printcol(col,string)
            except:
                R,G,B=ima[x][y]
                print(ima[x][y])
                col=str(hex(int(R)))[2:4].zfill(2)+str(hex(int(G)))[2:4].zfill(2)+str(hex(int(B)))[2:4].zfill(2)
                printcol(col,string)
        if string==1:
            stri1=stri1+"<br>"
        if string==2:
            stri2=stri2+"<br>"
        if string==3:
            stri3=stri3+"<br>"
        if string==4:
            stri4=stri4+"<br>"

printQuarant(int((xsize/4)*0),int((xsize/4)*1),ysize,1)
printQuarant(int((xsize/4)*1),int((xsize/4)*2),ysize,2)
printQuarant(int((xsize/4)*2),int((xsize/4)*3),ysize,3)
printQuarant(int((xsize/4)*3),int((xsize/4)*4),ysize,4)

print("generated in "+str(time.time()-start))
inpu=input()
print("coppied part 1!")
clipboard.copy(stri1)
inpu=input()
print("coppied part 2!")
clipboard.copy(stri2)
inpu=input()
print("coppied part 3!")
clipboard.copy(stri3)
inpu=input()
print("coppied part 4!")
clipboard.copy(stri4)

