from tkinter import Tk,Canvas
import time
import random

window=Tk()
canvas=Canvas(window,bg="#E0E0E0",width=1200,height=1000)
window.title('bicolour game of life')
n=700
side=1

grid=[[0 for i in range(n+1)] for i in range(n+1)]

for i in range(n//3,n*2//3):
    for j in range(n//3,n*2//3):
        # if i%3!=0 and j%3!=0 and (j<400 or j>600 or i<400 or i>600):
        #     grid[i][j]=1 if i<(n+1)/2 else 2
        # else:
        #     grid[i][j]=0
        if random.random()>15/16:
            if i<(n+1)/2:#random.random()>0.5:#
                grid[i][j]=1
            else:
                grid[i][j]=2

# for i in range(n):
#     grid[0][i]=1
#     grid[n-1][i]=2

generation=0
rectangles=[[0 for y in range(n)] for x in range(n)]

out=set()
out.update([(-1,i) for i in range(-1,n+1)],[(i,-1) for i in range(-1,n+1)],[(n,i) for i in range(-1,n+1)],[(i,n) for i in range(-1,n+1)])

def start(arg):
    global generation,grid,rectangles
    print(arg)
    
    tstart=time.time()
    
    newrunable=set()
    rectangles=[[0 for y in range(n)] for x in range(n)]
    canvas.delete("all")
    for x in range(n):
        for y in range(n):
            # newrunable.add((x,y))
            if grid[x][y]==1:
                rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='red',outline='')
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
            elif grid[x][y]==2:
                rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='blue',outline='')
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
    canvas.update()
    time.sleep(1)
    
    for g in range(10000):
        #draw lines
        # for i in range(0,side*(n+1),side):
        #     canvas.create_line(20,i+20,side*n+20,i+20)
        #     canvas.create_line(i+20,20,i+20,side*n+20)
        
        t1=time.time()
        generation+=1
        print('generation',generation)
        
        newgrid=[row.copy() for row in grid]
        
        runable=newrunable-out
        newrunable.clear()
        
        for x,y in runable:
            red=blue=0
            for a,b in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                if neighborcolor:=grid[x+a][y+b]:
                    if neighborcolor==1:
                        red+=1
                    elif neighborcolor==2:
                        blue+=1
                        
            neighbornum=red+blue
            if not (gridxy:=grid[x][y]) and neighbornum==3:
                #birth
                if red>blue:
                    newgrid[x][y]=1
                    rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='red',outline='')
                else:
                    newgrid[x][y]=2
                    rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='blue',outline='')
                    
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
            elif gridxy and not 2<=neighbornum<=3:
                #die
                newgrid[x][y]=0
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
                canvas.delete(rectangles[x][y])
        
        grid=newgrid
        
        canvas.update()
        t2=time.time()
        print(t2-t1)
        
    tend=time.time()
    print(tend-tstart,"s")

def addGun(arg):
    global grid
    print(arg)
    if arg.char!="1":
        return
    gunshape=[
        "00000000000000000000000000000000000000000"]*3+["000000000000000000000000020000000000000000",
        "000000000000000000000022220000000000000000",
        "000000000000020000000222200000000000000000",
        "000000000000202000000200200000000012000000",
        "000000000001000220000222200000000012000000",
        "220000000002000220000022220000000000000000",
        "220000000001000220000000020000000000000000",
        "000000000000202000000000000000000000000000",
        "000000000000020000000000000000000000000000",
        "000000000000000000000000000000000000000000",
        "000000000000000000000000000000000000000000",]
    
    for x in range(n//3):
        for y in range(n//3):
            grid[x][y]=0
            grid[n-x-1][y]=0
            grid[n-x-1][n-y-1]=0
            grid[x][n-y-1]=0
    
    for x in range(len(gunshape)):
        for y in range(len(gunshape[0])):
            color=int(gunshape[x][y])
            grid[y][x]=color
            grid[y][n-x-1]=color
            grid[n-y-1][x]=3-color if color else color
            grid[n-y-1][n-x-1]=3-color if color else color
            
# addGun(0)
    
canvas.bind_all("<KeyPress>",addGun)
canvas.bind("<Button-1>",start)
canvas.pack()
window.mainloop()
