from tkinter import Tk,Canvas
import time
# import random

window=Tk()
canvas=Canvas(window,bg="#E0E0E0",width=1300,height=900)
window.title('game of life')
n=100
side=8

grid=[[0 for i in range(n+1)] for i in range(n+1)]

# for i in range(n):
#     for j in range(n):
#         if random.random()>0.75:
#             if random.random()>0.5:#i<(n+1)/2:#
#                 grid[i][j]=1
#             else:
#                 grid[i][j]=1

for i in range(n):
    grid[0][i]=1
    grid[n-1][i]=1

generation=0

    
def start(arg):
    global generation,grid
    
    tstart=time.time()
    ignorable=[[0 for i in range(n+1)] for i in range(n+1)]
    for g in range(1000):
        canvas.delete("all")
        # for i in range(0,side*(n+1),side):
        #     canvas.create_line(20,i+20,side*n+20,i+20)
        #     canvas.create_line(i+20,20,i+20,side*n+20)
        
        canvas.create_text(1100,300,text='generation:')
        canvas.create_oval(1100,400,1120,420,fill='black')
        
        generation+=1
        print('generation',generation)
        t1=time.time()
        
        newgrid=[row.copy() for row in grid]
        
        addignore=[]
        removeignore=set()
        
        for x in range(n):
            for y in range(n):
                if ignorable[x][y]:
                    continue
                neighbornum=0
                gridxy=grid[x][y]
                for a,b in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                    neighbornum+=grid[x+a][y+b]
                if neighbornum<2:
                    addignore.append((x,y))
                    
                if not gridxy and neighbornum==3:
                    #birth
                    newgrid[x][y]=1
                    canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='black',outline='')
                    for c,d in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                        removeignore.add((x+c,y+d))
                elif gridxy:
                    if not 2<=neighbornum<=3:
                        #die
                        newgrid[x][y]=0
                    else:
                        #keep
                        canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='black',outline='')
                    
        for x,y in addignore:
            ignorable[x][y]=1
        for x,y in removeignore:
            ignorable[x][y]=0
                
        grid=newgrid
        total=sum((sum(i) for i in grid))
        print('total',total)
        canvas.create_text(1075,410,text=total)
        canvas.create_text(1100,340,text=generation)
        canvas.update()
        
        t2=time.time()
        print(t2-t1)
        
    tend=time.time()
    print(tend-tstart,"s")


canvas.bind("<Button-1>",start)
canvas.pack()
window.mainloop()
