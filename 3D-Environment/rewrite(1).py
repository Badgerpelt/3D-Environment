import os.path as path
import sys
import math
import tkinter as tk
import time
import keyboard
class Paths:
    
    this_path = path.abspath(__file__)

    if getattr(sys, 'frozen', False):

        
        this_path = sys.executable
        
    this_dir = path.dirname(this_path)

# class CustomFunctions: 

def rotateAroundZAxis(x,y,theta,inRadians):
    
    if inRadians == False:

        theta = math.radians(theta)
    
    newX = math.cos(math.atan2(y,x) + theta) * math.sqrt(x**2 + y**2)
    newY = math.sin(math.atan2(y,x) + theta) * math.sqrt(x**2 + y**2)
    return round(newX,6),round(newY,6)

def rotateAroundXAxis(y,z,theta,inRadians):
    
    if inRadians == False:

        theta = math.radians(theta)
    
    newY = math.cos(math.atan2(z,y) + theta) * math.sqrt(y**2 + z**2)
    newZ = math.sin(math.atan2(z,y) + theta) * math.sqrt(y**2 + z**2)
    return round(newY,6),round(newZ,6)

def rotateAroundYAxis(z,x,theta,inRadians):
    
    if inRadians == False:

        theta = math.radians(theta)
    
    newZ = math.cos(math.atan2(x,z) + theta) * math.sqrt(z**2 + x**2)
    newX = math.sin(math.atan2(x,z) + theta) * math.sqrt(z**2 + x**2)
    return round(newZ,6),round(newX,6)

def drawAxis():
    
    canvas.create_line(WINDOW_LENGTH/2, WINDOW_HEIGHT, WINDOW_LENGTH/2, 0, width=1, fill="blue")
    canvas.create_line(0, WINDOW_HEIGHT/2, WINDOW_LENGTH, WINDOW_HEIGHT/2, width=1, fill="blue")

def createPoint(x,y,z):
    color = "mediumblue"
    if z < 75:

        color = "blue"
    if z < 50:

        color = "royalblue"
    if z < 25:

        color = "steelblue"
    if z < 0:

        color = "dodgerblue"
    if z < -25:

        color = "deepskyblue"
    if z < -50:

        color = "skyblue"
    if z < -75:

        color = "lightskyblue"
    
    canvas.create_rectangle(WINDOW_LENGTH/2 + x, WINDOW_HEIGHT/2 - y, WINDOW_LENGTH/2 + x+1, WINDOW_HEIGHT/2 - y+1, width=2, outline=color,tags="point")

def lineOfDots(x1,y1,z1,x2,y2,z2,nDots,axis):
    
    result = []
    hyp = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    inc = hyp/(nDots-1)
    temp = [x1,y1,z1]
    for i in range(nDots):

        
        result.append(temp.copy())
        temp[axis] += inc

    return result

def toggleLockButton(id,unlockedImage,lockedImage):
    upLockButtonState = globals()["upLockButtonState"]
    downLockButtonState = globals()["downLockButtonState"]
    leftLockButtonState = globals()["leftLockButtonState"]
    rightLockButtonState = globals()["rightLockButtonState"]
    print(upLockButtonState)
    if id == "up":

        if upLockButtonState == "unlocked":

            globals()["upLockButtonState"] = "locked"
            globals()["upLockButton"].configure(image=lockedImage)
        else:
            globals()["upLockButtonState"] = "unlocked"
            globals()["upLockButton"].configure(image=unlockedImage)
    elif id == "down":

        if downLockButtonState == "unlocked":

            globals()["downLockButtonState"] = "locked"
            globals()["downLockButton"].configure(image=lockedImage)
        else:
            globals()["downLockButtonState"] = "unlocked"
            globals()["downLockButton"].configure(image=unlockedImage)
    elif id == "left":

        if leftLockButtonState == "unlocked":

            globals()["leftLockButtonState"] = "locked"
            globals()["leftLockButton"].configure(image=lockedImage)
        else:
            globals()["leftLockButtonState"] = "unlocked"
            globals()["leftLockButton"].configure(image=unlockedImage)
    elif id == "right":

        if rightLockButtonState == "unlocked":

            globals()["rightLockButtonState"] = "locked"
            globals()["rightLockButton"].configure(image=lockedImage)
        else:
            globals()["rightLockButtonState"] = "unlocked"
            globals()["rightLockButton"].configure(image=unlockedImage)
    

def animate(cords,xInc,yInc,zInc,xInitialRotationOffset,yInitialRotationOffset,zInitialRotationOffset):

    i,j,k= 0,0,0

    lockedImage = tk.PhotoImage(file=Paths.this_dir + "/locked.png")
    unlockedImage = tk.PhotoImage(file=Paths.this_dir + "/unlocked.png")    

    upImage = tk.PhotoImage(file=Paths.this_dir + "/up.png")
    upButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="upButton",image=upImage)
    upButton.place(x=WINDOW_LENGTH/2-25,y=3*WINDOW_HEIGHT/4,width=50,height=50)
    global upLockButton
    upLockButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="upLockButton",image=unlockedImage,command=lambda:toggleLockButton("up",unlockedImage,lockedImage))
    upLockButton.place(x=WINDOW_LENGTH/2-25,y=3*WINDOW_HEIGHT/4-50,width=50,height=50)

    downImage = tk.PhotoImage(file=Paths.this_dir + "/down.png")
    downButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="downButton",image=downImage)
    downButton.place(x=WINDOW_LENGTH/2-25,y=6*WINDOW_HEIGHT/7,width=50,height=50)
    global downLockButton
    downLockButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="downLockButton",image=unlockedImage,command=lambda:toggleLockButton("down",unlockedImage,lockedImage))
    downLockButton.place(x=WINDOW_LENGTH/2-25,y=6*WINDOW_HEIGHT/7+50,width=50,height=50)

    leftImage = tk.PhotoImage(file=Paths.this_dir + "/left.png")
    leftButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="leftButton",image=leftImage)
    leftButton.place(x=2*WINDOW_LENGTH/5-25,y=6*WINDOW_HEIGHT/7,width=50,height=50)
    global leftLockButton
    leftLockButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="leftLockButton",image=unlockedImage,command=lambda:toggleLockButton("left",unlockedImage,lockedImage))
    leftLockButton.place(x=2*WINDOW_LENGTH/5-75,y=6*WINDOW_HEIGHT/7,width=50,height=50)

    rightImage = tk.PhotoImage(file=Paths.this_dir + "/right.png")
    rightButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="rightButton",image=rightImage)
    rightButton.place(x=3*WINDOW_LENGTH/5-25,y=6*WINDOW_HEIGHT/7,width=50,height=50)
    global rightLockButton
    rightLockButton = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name="rightLockButton",image=unlockedImage,command=lambda:toggleLockButton("right",unlockedImage,lockedImage))
    rightLockButton.place(x=3*WINDOW_LENGTH/5+25,y=6*WINDOW_HEIGHT/7,width=50,height=50)
    
    
    
    xNewRotationOffset = xInitialRotationOffset
    yNewRotationOffset = yInitialRotationOffset
    zNewRotationOffset = zInitialRotationOffset
    while True:
        
        xNewRotationOffset += xInc*i
        yNewRotationOffset += yInc*j
        zNewRotationOffset += zInc*k
        check = 0
        while True:
            
            if xNewRotationOffset >= 360:
 
                xNewRotationOffset -= 360
                check += 1
            elif xNewRotationOffset <= -360:
 
                xNewRotationOffset += 360
                check += 1
                
            if yNewRotationOffset >= 360:
 
                yNewRotationOffset -= 360
                check += 1
            elif yNewRotationOffset <= -360:
 
                yNewRotationOffset += 360
                check += 1
                
            if zNewRotationOffset >= 360:
 
                zNewRotationOffset -= 360
                check += 1
            elif zNewRotationOffset <= -360:
 
                zNewRotationOffset += 360
                check += 1
            
            if check == 0:

                break
            check = 0
        canvas.create_text(WINDOW_LENGTH/3,7,text="Xr= {} deg".format(round(xNewRotationOffset,6)),justify="left",tags="text")
        canvas.create_text(WINDOW_LENGTH/3,17,text="Yr= {} deg".format(round(yNewRotationOffset,6)),justify="left",tags="text")
        canvas.create_text(WINDOW_LENGTH/3,27,text="Zr= {} deg".format(round(zNewRotationOffset,6)),justify="left",tags="text")
        
        time.sleep(.008)
        for item in range(len(cords)):

            newX,newY,newZ = cords[item]
            newX,newY = rotateAroundZAxis(newX,newY,zInc*k,False)
            newY,newZ = rotateAroundXAxis(newY,newZ,xInc*i,False)
            newZ,newX = rotateAroundYAxis(newZ,newX,yInc*j,False)
            cords[item] = newX,newY,newZ
            createPoint(newX,newY,newZ)

        i,j,k = 0,0,0
        # for item in range(len(cords)):

        #     newX,newY,newZ = cords[item]
        #     newX,newY = rotateAroundZAxis(newX,newY,zNewRotationOffset,False)
        #     newY,newZ = rotateAroundXAxis(newY,newZ,xNewRotationOffset,False)
        #     newZ,newX = rotateAroundYAxis(newZ,newX,yNewRotationOffset,False)  

        canvas.update()
        canvas.delete("point","text")

        if keyboard.is_pressed("up") or upButton.cget("relief") == "sunken" or upLockButtonState == "locked":

            i -= 1
        if keyboard.is_pressed("down") or downButton.cget("relief") == "sunken" or downLockButtonState == "locked":

            i += 1
        if keyboard.is_pressed("left") or leftButton.cget("relief") == "sunken" or leftLockButtonState == "locked":

            j -= 1
        if keyboard.is_pressed("right") or rightButton.cget("relief") == "sunken" or rightLockButtonState == "locked":

            j += 1
        
        

def main():
    global WINDOW_LENGTH
    global WINDOW_HEIGHT
    WINDOW_LENGTH = 1000
    WINDOW_HEIGHT = 800

    global window
    window = tk.Tk()
    window.title("Test")
    window.geometry("{}x{}".format(WINDOW_LENGTH, WINDOW_HEIGHT))
    
    global canvas
    canvas = tk.Canvas(window, width=WINDOW_LENGTH, height=WINDOW_HEIGHT)
    canvas.pack()

    global upLockButtonState
    global downLockButtonState
    global leftLockButtonState
    global rightLockButtonState    
    upLockButtonState = "unlocked"
    downLockButtonState ="unlocked"
    leftLockButtonState = "unlocked"
    rightLockButtonState = "unlocked"

    cords = []
    newCords = []
    sideLength = 200
    nDots = 13
    #x-axis
    newCords.append(lineOfDots(-sideLength/2,sideLength/2,-sideLength/2,sideLength/2,sideLength/2,-sideLength/2,nDots,0))
    newCords.append(lineOfDots(-sideLength/2,sideLength/2,sideLength/2,sideLength/2,sideLength/2,sideLength/2,nDots,0))
    newCords.append(lineOfDots(-sideLength/2,-sideLength/2,sideLength/2,sideLength/2,-sideLength/2,sideLength/2,nDots,0))
    newCords.append(lineOfDots(-sideLength/2,-sideLength/2,-sideLength/2,sideLength/2,-sideLength/2,-sideLength/2,nDots,0))
    #y-axis
    newCords.append(lineOfDots(sideLength/2,-sideLength/2,-sideLength/2,sideLength/2,sideLength/2,-sideLength/2,nDots,1))
    newCords.append(lineOfDots(sideLength/2,-sideLength/2,sideLength/2,sideLength/2,sideLength/2,sideLength/2,nDots,1))
    newCords.append(lineOfDots(-sideLength/2,-sideLength/2,sideLength/2,-sideLength/2,sideLength/2,sideLength/2,nDots,1))
    newCords.append(lineOfDots(-sideLength/2,-sideLength/2,-sideLength/2,-sideLength/2,sideLength/2,-sideLength/2,nDots,1))
    #z-axis
    newCords.append(lineOfDots(sideLength/2,-sideLength/2,-sideLength/2,sideLength/2,-sideLength/2,sideLength/2,nDots,2))
    newCords.append(lineOfDots(sideLength/2,sideLength/2,-sideLength/2,sideLength/2,sideLength/2,sideLength/2,nDots,2))
    newCords.append(lineOfDots(-sideLength/2,sideLength/2,-sideLength/2,-sideLength/2,sideLength/2,sideLength/2,nDots,2))
    newCords.append(lineOfDots(-sideLength/2,-sideLength/2,-sideLength/2,-sideLength/2,-sideLength/2,sideLength/2,nDots,2))
    
    for line in newCords:

        for cord in line:

            cords.append(cord)
    xInitialRotationOffset = 0
    yInitialRotationOffset = 0
    zInitialRotationOffset = 0
    speed = 1
    xInc = 1*speed
    yInc = 1*speed
    zInc = 1*speed
    drawAxis()
    # img = canvas.create_image(WINDOW_LENGTH/2,WINDOW_HEIGHT/2)
    
    
    for x,y,z in cords:

        
        newX,newY,newZ = x,y,z
        newX,newY = rotateAroundZAxis(newX,newY,zInitialRotationOffset,False)
        newY,newZ = rotateAroundXAxis(newY,newZ,xInitialRotationOffset,False)
        newZ,newX = rotateAroundYAxis(newZ,newX,yInitialRotationOffset,False)
        createPoint(newX,newY,newZ)
        
    canvas.update()
    window.after(0,lambda: animate(cords,xInc,yInc,zInc,xInitialRotationOffset,yInitialRotationOffset,zInitialRotationOffset))
    window.mainloop()
        
main()