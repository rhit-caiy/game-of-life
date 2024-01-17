from tkinter import Tk,Canvas
import time
import random

window=Tk()
canvas=Canvas(window,bg="#E0E0E0",width=1200,height=1000)
window.title('more colour game of life')
n=750
side=1

seed=random.random()
# seed=
random.seed(seed)

colorname=["white","red","blue","green","purple","black","orange"]
colornum=len(colorname)-1
zeros=[0]*(colornum+1)

grid=[[0 for i in range(n+1)] for i in range(n+1)]

# for i in range(n):
#     for j in range(n):
#         # if i%3!=0 and j%3!=0 and (j<400 or j>600 or i<400 or i>600):
#         #     grid[i][j]=1 if i<(n+1)/2 else 2
#         # else:
#         #     grid[i][j]=0
#         if random.random()>0.75:
#             grid[i][j]=random.randint(1,5)

for i in range(n//3,n*2//3):
    for j in range(n//3,n*2//3):
        # if i%3!=0 and j%3!=0 and (j<400 or j>600 or i<400 or i>600):
        #     grid[i][j]=1 if i<(n+1)/2 else 2
        # else:
        #     grid[i][j]=0
        if random.random()>0.95:#0.9375:
            grid[i][j]=5

# for i in range(n):
#     grid[0][i]=1
#     grid[n-1][i]=2

generation=0
rectangles=[[0 for y in range(n)] for x in range(n)]

out=set()
out.update([(-1,i) for i in range(-1,n+1)],[(i,-1) for i in range(-1,n+1)],[(n,i) for i in range(-1,n+1)],[(i,n) for i in range(-1,n+1)])
running=0

canvas.create_text(1000,100,text="generation")
textgeneration=canvas.create_text(1000,120,text="0")
textnum=zeros.copy()
for i,c in enumerate(colorname):
    canvas.create_rectangle(1000,150+50*i,1020,170+50*i,fill=c)
    textnum[i]=canvas.create_text(1050,160+50*i,text="0")

def start(arg):
    global generation,grid,rectangles,running
    print(arg)
    if running:
        return
    else:
        running=1
    
    newrunable=set()
    for i in range(n):
        for j in range(n):
            canvas.delete(rectangles[i][j])
            rectangles[i][j]=0
    
    
    
    for x in range(n):
        for y in range(n):
            if color:=grid[x][y]:
                rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill=colorname[color],outline='')
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
    canvas.update()
    time.sleep(1)
    tstart=time.time()
    for g in range(1,100000+1):
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
            colors=zeros.copy()
            
            for a,b in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                colors[grid[x+a][y+b]]+=1
            
            neighbornum=8-colors[0]
            colors[0]=0
            
            if not (gridxy:=grid[x][y]) and neighbornum==3:
                #birth wih majority or random if equal
                if 3 in colors:
                    color=colors.index(3)
                elif 2 in colors:
                    color=colors.index(2)
                else:
                    target=[i for i in range(colornum+1) if colors[i]]
                    color=random.choice(target)
                
                newgrid[x][y]=color
                rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill=colorname[color],outline='')
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
            elif gridxy and not 2<=neighbornum<=3:
                #die
                newgrid[x][y]=0
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
                canvas.delete(rectangles[x][y])
        
        grid=newgrid
        t2=time.time()
        if generation%30==0:
            canvas.itemconfig(textgeneration,text=str(g)+", "+str(generation))
            
            colorsum=zeros.copy()
            for i in grid:
                for j in i:
                    colorsum[j]+=1
            for i,num in enumerate(textnum):
                canvas.itemconfig(num,text=int(colorsum[i]))
            canvas.update()
        t3=time.time()
        print(t2-t1,t3-t2)
    tend=time.time()
    print(tend-tstart,"s")
    running=0

def addGun(arg):
    global grid
    print(arg)
    if arg.char not in "1a" or running:
        return
    gunshape=[
        "000000000000000000000000000000000000000000",
        "000000000000000000000000000000000000000000",
        "000000000000000000000000000000000000000000",
        "000000000000000000000000010000000000000000",
        "000000000000000000000011110000000000000000",
        "000000000000010000000111100000000000000000",
        "000000000000101000000200100000000011000000",
        "000000000001000110000111100000000011000000",
        "110000000001000110000011110000000000000000",
        "110000000001000110000000010000000000000000",
        "000000000000101000000000000000000000000000",
        "000000000000010000000000000000000000000000",
        "000000000000000000000000000000000000000011",
        "000000000000000000000000000000000000000011",
        "000000000000000000000000000000000000000000",
        "000000000000000000000000000000000000000000",
        "000000110000011000000000000000000011000000",
        "000000110000011000000000000000000011000000",]
    
    for x in range(n//3):
        for y in range(n//3):
            grid[x][y]=0
            grid[n-x-1][y]=0
            grid[n-x-1][n-y-1]=0
            grid[x][n-y-1]=0
    
    for x in range(len(gunshape)):
        for y in range(len(gunshape[0])):
            if int(gunshape[x][y]):
                grid[y][x]=1
                grid[y][n-x-1]=2
                grid[n-y-1][x]=3
                grid[n-y-1][n-x-1]=4
    
    #blocks
    for i in range((n-50)//10):
        y=random.randint(25,n//2)
        x=y+10+int(10*random.random())
        if i%2==0:
            x-=20
        else:
            x+=10
        for x,y in (x,y),(x,n-y-1),(n-x-1,y),(n-x-1,n-y-1):
            for a,b in (0,0),(0,1),(1,0),(1,1):
                grid[x][y]=6
                grid[x+1][y]=6
                grid[x][y+1]=6
                grid[x+1][y+1]=6
            
            
            
# addGun(0)
    
canvas.bind_all("<KeyPress>",addGun)
canvas.bind("<Button-1>",start)
canvas.pack()
window.mainloop()
