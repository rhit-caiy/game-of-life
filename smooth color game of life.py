from tkinter import Tk,Canvas
import time
import random

window=Tk()
canvas=Canvas(window,bg="#404040",width=1200,height=1000)
window.title('smooth colour game of life')
n=750
side=1
#equal about 5-8
generationperpaint=60

generationperclick=100000


seed=random.random()
# seed=0
random.seed(seed)

grid=[[0 for i in range(n+1)] for i in range(n+1)]

# for i in range(n):
#     for j in range(n):
#         # if i%3!=0 and j%3!=0 and (j<400 or j>600 or i<400 or i>600):
#         #     grid[i][j]=1 if i<(n+1)/2 else 2
#         # else:
#         #     grid[i][j]=0
#         if random.random()>0.75:
#             grid[i][j]=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

for i in range(n//3,n*2//3):
    for j in range(n//3,n*2//3):
        # if i%3!=0 and j%3!=0 and (j<400 or j>600 or i<400 or i>600):
        #     grid[i][j]=1 if i<(n+1)/2 else 2
        # else:
        #     grid[i][j]=0
        if random.random()>0.95:#0.9375:
            grid[i][j]=(192,192,192)#(random.randint(0,255),random.randint(0,255),random.randint(0,255))

# for i in range(n):
#     grid[0][i]=1
#     grid[n-1][i]=2

generation=0
rectangles=[[0 for y in range(n)] for x in range(n)]

out=set()
out.update([(-1,i) for i in range(-1,n+1)],[(i,-1) for i in range(-1,n+1)],[(n,i) for i in range(-1,n+1)],[(i,n) for i in range(-1,n+1)])
running=0


canvas.create_text(1000,100,text="generation")
textgeneration=canvas.create_text(1000,120,text=0)
canvas.create_rectangle(950,200,1000,250,fill="red")
canvas.create_rectangle(950,300,1000,350,fill="green")
canvas.create_rectangle(950,400,1000,450,fill="blue")
canvas.create_rectangle(950,500,1000,550,fill="#808080")
rgba=[canvas.create_text(1100,i,text=0) for i in (225,325,425,525)]
    
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
                rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill=f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}",outline='')
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
    canvas.update()
    times=[0,0]
    paintstore=[i.copy() for i in grid]
    time.sleep(1)
    tstart=time.time()
    for g in range(1,generationperclick+1):
        #draw lines
        # for i in range(0,side*(n+1),side):
        #     canvas.create_line(20,i+20,side*n+20,i+20)
        #     canvas.create_line(i+20,20,i+20,side*n+20)
        
        t1=time.time()
        generation+=1
        
        newgrid=[row.copy() for row in grid]
        
        runable=newrunable-out
        newrunable.clear()
        
        for x,y in runable:
            colors=[]
            for a,b in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                if color:=grid[x+a][y+b]:
                    colors.append(color)
            
            neighbornum=len(colors)
            if not (gridxy:=grid[x][y]) and neighbornum==3:
                #birth wih average color value
                color=((colors[0][0]+colors[1][0]+colors[2][0])//3,(colors[0][1]+colors[1][1]+colors[2][1])//3,(colors[0][2]+colors[1][2]+colors[2][2])//3)
                newgrid[x][y]=color
                #
                # rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill=f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}",outline='')
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
            elif gridxy and not 2<=neighbornum<=3:
                #die
                newgrid[x][y]=0
                newrunable.update(((x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)))
                #
                # canvas.delete(rectangles[x][y])
        
        grid=newgrid
        t2=time.time()
        if not generation%generationperpaint:
            #fast computation but longer paint
            for x in range(n):
                for y in range(n):
                    if grid[x][y]!=paintstore[x][y]:
                        if not (color:=grid[x][y]):
                            canvas.delete(rectangles[x][y])
                        elif not paintstore[x][y]:
                            rectangles[x][y]=canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill=f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}",outline='')
                        else:
                            canvas.itemconfig(rectangles[x][y],fill=f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
                        paintstore[x][y]=color
            
            rnum,gnum,bnum=0,0,0
            total=0
            for i in grid:
                for j in i:
                    if j:
                        total+=1
                        rnum+=j[0]
                        gnum+=j[1]
                        bnum+=j[2]
            for i,l in enumerate((rnum,gnum,bnum,(rnum+gnum+bnum)/3)):
                canvas.itemconfig(rgba[i],text=(l/total))
            canvas.itemconfig(textgeneration,text=str(g)+", "+str(generation))
            canvas.update()
            
        t3=time.time()
        times[0]+=t2-t1
        times[1]+=t3-t2
        if not generation%generationperpaint:
            print("generation",g,generation,times,"average",times[0]/g,times[1]/g)
    tend=time.time()
    print(times)
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
                grid[y][x]=(255,64,64)
                grid[y][n-x-1]=(255,255,255)
                grid[n-y-1][x]=(0,0,0)
                grid[n-y-1][n-x-1]=(64,64,255)
    
    #blocks
    for i in range((n-50)//15):
        y=random.randint(25,n//3)
        x=y+10+int(10*random.random())
        if i%2==0:
            x-=20
        else:
            x+=10
        for x,y in (x,y),(x,n-y-2),(n-x-2,y),(n-x-2,n-y-2):
            for a,b in (0,0),(0,1),(1,0),(1,1):
                grid[x][y]=(64,255,64)
                grid[x+1][y]=(64,255,64)
                grid[x][y+1]=(64,255,64)
                grid[x+1][y+1]=(64,255,64)


canvas.bind_all("<KeyPress>",addGun)
canvas.bind("<Button-1>",start)
canvas.pack()
window.mainloop()
