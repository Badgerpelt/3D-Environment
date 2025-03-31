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

class CustomFunctions:

    # returns cartesian coordinates of a point given an angle on a unit circle
    
    def get_pos(angle):
  
        x = sideLength * math.cos(math.radians(angle))
        y = sideLength * math.sin(math.radians(angle))
        return x, y
    
    def pixel_dist_from_origin(x, y, z, origin):
        
        deg_inc = 15

    def shape(sides, currx, curry, ref):
        
        newcords = []
        CF = CustomFunctions

        # internal angle of a 2D shape given the number of sides
        angle = (180 * (sides - 2)) / sides
        dec = 180 - angle
        curr = 180 + ref
        pos_bank = []
        
        for i in range(sides):
            
            curr -= dec
            
            pos_bank.append([currx, curry, curr])
            """print(pos_bank)"""
            
            endx, endy = CF.get_pos(curr)
            endx += currx
            endy += curry
            
            newcords.append(lineOfDots([currx, curry,-math.tan(math.acos(math.tan(math.radians(30))/(math.sin(math.radians(60))*2))/2)*(math.tan(math.radians(30))*sideLength)/2.0], [endx, endy,-math.tan(math.acos(math.tan(math.radians(30))/(math.sin(math.radians(60))*2))/2)*(math.tan(math.radians(30))*sideLength)/2.0],8))
            currx,curry = endx, endy
            
        return pos_bank,newcords

# returns newY & newZ coords when y & z are rotated theta deg around the xAxis

def rotateAroundXAxis(y,z,theta,inRadians):
    
    if inRadians == False:
        
        theta = math.radians(theta)
    
    newY = math.cos(theta)*y - math.sin(theta)*z
    newZ = math.sin(theta)*y + math.cos(theta)*z
    return round(newY,6),round(newZ,6)

# returns newZ & newX coords when z & x are rotated theta deg around the yAxis

def rotateAroundYAxis(z,x,theta,inRadians):
    
    if inRadians == False:
        
        theta = math.radians(theta)
        
    newZ = math.cos(theta)*z - math.sin(theta)*x
    newX = math.sin(theta)*z + math.cos(theta)*x
    return round(newZ,6),round(newX,6)

# returns newX & newY coords when x & y are rotated theta deg around the zAxis

def rotateAroundZAxis(x,y,theta,inRadians):
    
    if inRadians == False:
        
        theta = math.radians(theta)
    
    newX = math.cos(theta)*x - math.sin(theta)*y
    newY = math.sin(theta)*x + math.cos(theta)*y
    return round(newX,6),round(newY,6)

def getRotation(cords1,cords2,cords3):

    print()

# displays static x, y, z axes to the window

def drawAxis():
    
    canvas.create_line(WINDOW_LENGTH/2, WINDOW_HEIGHT, WINDOW_LENGTH/2, 0, width=1, fill="blue")
    canvas.create_line(0, WINDOW_HEIGHT/2, WINDOW_LENGTH, WINDOW_HEIGHT/2, width=1, fill="blue")

# displays point(x, y) to the window relative to the x & y axes with shades of color representing z

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

def lineOfDots(start,end,nDots):

    x1,y1,z1 = start
    x2,y2,z2 = end
    result = []
    print(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
    xinc = (x2-x1)/(nDots-1)
    yinc = (y2-y1)/(nDots-1)
    zinc = (z2-z1)/(nDots-1)
    temp = [x1,y1,z1]
    
    for i in range(nDots):

        result.append(temp.copy())
        temp = [temp[0] + xinc, temp[1] + yinc, temp[2] + zinc]

    return result

def toggleLockButton(id,unlockedImage,lockedImage):
    
    try:
        
        lockButtonState = globals()[f"{id}LockButtonState"]
        
        if lockButtonState == "unlocked":
            
            globals()[f"{id}LockButtonState"] = "locked"
            globals()[f"{id}LockButton"].configure(image=lockedImage)
            
        else:
            
            globals()[f"{id}LockButtonState"] = "unlocked"
            globals()[f"{id}LockButton"].configure(image=unlockedImage)
            
    except KeyError:
        
        print("'id' variable is not of name 'up', 'down', 'left', or 'right'")

def makeShape(s1,s2):
    
    CF = CustomFunctions
    y,newcords = CF.shape(s1, -sideLength/2, -(math.tan(math.radians(30))*sideLength)/2.0, 0)

    for i in range(len(y)):
    
        x = y[i]
        newcords += CF.shape(s2, x[0], x[1], x[2])[1]
    
    return newcords

# returns coords of a cube

def cube(sideLength,nDots):
    
    newCords = []
    points = [

        [sideLength/2,sideLength/2,sideLength/2], #0
        [-sideLength/2,sideLength/2,sideLength/2], #1
        [sideLength/2,-sideLength/2,sideLength/2], #2
        [-sideLength/2,-sideLength/2,sideLength/2], #3
        [sideLength/2,sideLength/2,-sideLength/2], #4
        [-sideLength/2,sideLength/2,-sideLength/2], #5
        [sideLength/2,-sideLength/2,-sideLength/2], #6
        [-sideLength/2,-sideLength/2,-sideLength/2] #7

    ]
    #x-axis
    newCords.append(lineOfDots(points[5],points[4],nDots))
    newCords.append(lineOfDots(points[1],points[0],nDots))
    newCords.append(lineOfDots(points[3],points[2],nDots))
    newCords.append(lineOfDots(points[7],points[6],nDots))
    #y-axis
    newCords.append(lineOfDots(points[6],points[4],nDots))
    newCords.append(lineOfDots(points[2],points[0],nDots))
    newCords.append(lineOfDots(points[3],points[1],nDots))
    newCords.append(lineOfDots(points[7],points[5],nDots))
    #z-axis
    newCords.append(lineOfDots(points[6],points[2],nDots))
    newCords.append(lineOfDots(points[4],points[0],nDots))
    newCords.append(lineOfDots(points[5],points[1],nDots))
    newCords.append(lineOfDots(points[7],points[3],nDots))
    return newCords

# returns coords of a tetrahedron

def tetrahedron(sideLength,nDots):
    
    newCords = []
    temp = (math.tan(math.radians(30))*sideLength)/2.0
    temp2 = sideLength/(2*math.cos(math.radians(30)))
    
    # points = [
    #     [0, temp2, -temp*math.tan(math.radians(30))], #0
    #     [sideLength/2, -temp, -temp*math.tan(math.radians(30))], #1
    #     [-sideLength/2, -temp, -temp*math.tan(math.radians(30))], #2
    #     [0, 0, math.sqrt((math.sin(math.radians(60))*sideLength)**2 - temp**2) - temp*math.tan(math.radians(30))], #3
    # ]
    angle = math.acos(math.tan(math.radians(30))/(math.sin(math.radians(60))*2))
    print(math.tan(angle)*temp)
    print(math.sqrt(.75*(sideLength**2)-temp**2))
    temp3 = math.tan(angle/2)*temp
    print(temp3)

    points = [

        [0, temp2, -temp3], #0
        [sideLength/2, -temp, -temp3], #1
        [-sideLength/2, -temp, -temp3], #2
        [0, 0, math.sqrt(.75*(sideLength**2)-temp**2) - temp3], #3

    ]

    newCords.append(lineOfDots(points[0],points[1],nDots))
    newCords.append(lineOfDots(points[0],points[2],nDots))
    newCords.append(lineOfDots(points[0],points[3],nDots))
    newCords.append(lineOfDots(points[1],points[2],nDots))
    newCords.append(lineOfDots(points[1],points[3],nDots))
    newCords.append(lineOfDots(points[2],points[3],nDots))
    # newCords.append(lineOfDots(points[3],[0,0,-temp*math.tan(math.radians(30))],nDots))
    
    return newCords

# displays the 3D object made of cords on the screen allowing the user to rotate it

def animate(cords,xInc,yInc,zInc,xInitialRotationOffset,yInitialRotationOffset,zInitialRotationOffset):

    i,j,k= 0,0,0

    lockedImage = tk.PhotoImage(file=Paths.this_dir + "/locked.png")
    unlockedImage = tk.PhotoImage(file=Paths.this_dir + "/unlocked.png")    

    # def createButtons(id):
        
    #     image = tk.PhotoImage(file=Paths.this_dir + f"/{id}.png")
    #     button = tk.Button(master=canvas,highlightcolor="gray",activebackground="gray",name=f"{id}Button",image=image)
        
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

        time.sleep(.008)
        
        for item in range(len(cords)):
            
            newX,newY,newZ = cords[item]
            newY,newZ = rotateAroundXAxis(newY,newZ,xInc*i,False)
            newZ,newX = rotateAroundYAxis(newZ,newX,yInc*j,False)
            newX,newY = rotateAroundZAxis(newX,newY,zInc*k,False)
            cords[item] = newX,newY,newZ
            createPoint(newX,newY,newZ)
            
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
            
        canvas.create_text(WINDOW_LENGTH/3,7,text=f"Xr= {round(xNewRotationOffset,6)} deg",justify="left",tags="text")
        canvas.create_text(WINDOW_LENGTH/3,17,text=f"Yr= {round(yNewRotationOffset,6)} deg",justify="left",tags="text")
        canvas.create_text(WINDOW_LENGTH/3,27,text=f"Zr= {round(zNewRotationOffset,6)} deg",justify="left",tags="text")
        
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
    global sideLength
    sideLength = 200
    nDots = 13
    # newCords += cube(sideLength,nDots)
    newCords += tetrahedron(sideLength,nDots)
    newCords += makeShape(3,3)
    
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
        newY,newZ = rotateAroundXAxis(newY,newZ,xInitialRotationOffset,False)
        newZ,newX = rotateAroundYAxis(newZ,newX,yInitialRotationOffset,False)
        newX,newY = rotateAroundZAxis(newX,newY,zInitialRotationOffset,False)
        createPoint(newX,newY,newZ)
        
    canvas.update()
    window.after(0,lambda: animate(cords,xInc,yInc,zInc,xInitialRotationOffset,yInitialRotationOffset,zInitialRotationOffset))
    window.mainloop()
        
main()
