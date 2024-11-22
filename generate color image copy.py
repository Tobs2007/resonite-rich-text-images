import time
import clipboard
import numpy as np
from PIL import Image
size=int(17)
start=time.time()
global strings
strings=["","","","","","","",""]
xsize=128
ysize=128
img=Image.open("image.png")
imgres=img.resize((xsize,ysize))
ima= np.asarray(imgres)
imgres.save("output.png")



global colorold
colorold=[0,0,0]
def printcol(color,string):
    global strings
    global colorold
    if colorold==color :
        strings[string]=strings[string]+"█"
    else:
        colorold=color
        strings[string]=strings[string]+"<color=#"+color+">"+"█"



def printQuarant(xb,xe,y,string):
    global strings
    for x in range (xb,xe):
        for y in range(ysize):
            print(str(x)+"  "+str(y))
            try:
                R,G,B,A=ima[x][y]
                col=str(hex(int(R)))[2:4].zfill(2)+str(hex(int(G)))[2:4].zfill(2)+str(hex(int(B)))[2:4].zfill(2)#
                +str(hex(int(A)))[2:4].zfill(2)
                printcol(col,string)
            except:
                R,G,B=ima[x][y]
                # print(ima[x][y])
                col=str(hex(int(R)))[2:4].zfill(2)+str(hex(int(G)))[2:4].zfill(2)+str(hex(int(B)))[2:4].zfill(2)
                printcol(col,string)
        strings[string]=strings[string]+"<br>"

printQuarant(int((xsize/8)*0),int((xsize/8)*1),ysize,0)
printQuarant(int((xsize/8)*1),int((xsize/8)*2),ysize,1)
printQuarant(int((xsize/8)*2),int((xsize/8)*3),ysize,2)
printQuarant(int((xsize/8)*3),int((xsize/8)*4),ysize,3)
printQuarant(int((xsize/8)*4),int((xsize/8)*5),ysize,4)
printQuarant(int((xsize/8)*5),int((xsize/8)*6),ysize,5)
printQuarant(int((xsize/8)*6),int((xsize/8)*7),ysize,6)
printQuarant(int((xsize/8)*7),int((xsize/8)*8),ysize,7)

print("generated in "+str(time.time()-start))
num=0
for x in strings:
    inpu=input()
    print("coppied part "+str(num)+"!")
    num=num+1
    clipboard.copy(x)

