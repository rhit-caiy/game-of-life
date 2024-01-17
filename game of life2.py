from tkinter import Tk,Canvas
import time
# import random

window=Tk()
canvas=Canvas(window,bg="#E0E0E0",width=1300,height=900)
window.title('bicolour game of life')
n=100
side=8

grid=[[0 for i in range(n+1)] for i in range(n+1)]

# for i in range(n):
#     for j in range(n):
#         if random.random()>0.75:
#             if random.random()>0.5:#i<(n+1)/2:#
#                 grid[i][j]=1
#             else:
#                 grid[i][j]=2

for i in range(n):
    grid[0][i]=1
    grid[n-1][i]=2

generation=0

    
def start(arg):
    global generation,grid
    
    tstart=time.time()
    ignorable=[[0 for i in range(n+1)] for i in range(n+1)]
    addignore=[]
    removeignore=set()
    for g in range(1000):
        canvas.delete("all")
        # for i in range(0,side*(n+1),side):
        #     canvas.create_line(20,i+20,side*n+20,i+20)
        #     canvas.create_line(i+20,20,i+20,side*n+20)
        
        canvas.create_text(1100,300,text='generation:')
        canvas.create_oval(1100,400,1120,420,fill='red')
        canvas.create_oval(1100,500,1120,520,fill='blue')
        
        generation+=1
        print('generation',generation)
        t1=time.time()
        
        newgrid=[row.copy() for row in grid]
        
        addignore.clear()
        removeignore.clear()
        # totalred=totalblue=0
        # for x in range(n):
        #     for y in range(n):
        #         if grid[x][y]==1:
        #             totalred+=1
        #         elif grid[x][y]==2:
        #             totalblue+=1
                    
        for x in range(n):
            for y in range(n):
                if ignorable[x][y]:
                    continue
                red=blue=0
                gridxy=grid[x][y]
                for a,b in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                    neighborcolor=grid[x+a][y+b]
                    if neighborcolor:
                        if neighborcolor==1:
                            red+=1
                        elif neighborcolor==2:
                            blue+=1
                if red+blue<2:#not 2<=red+blue<=3:#
                    addignore.append((x,y))
                    
                if not gridxy and red+blue==3:
                    #birth
                    if red>blue:
                        newgrid[x][y]=1
                        canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='red',outline='')
                        # totalred+=1
                    else:
                        newgrid[x][y]=2
                        canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='blue',outline='')
                        # totalblue+=1
                    for c,d in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                        removeignore.add((x+c,y+d))
                elif gridxy:
                    if not 2<=red+blue<=3:
                        #die
                        newgrid[x][y]=0
                        
                        ##
                        # for c,d in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
                        #     removeignore.add((x+c,y+d))
                            
                        # if gridxy==1:
                        #     totalred-=1
                        # else:
                        #     totalblue-=1
                    else:
                        #keep
                        if gridxy==1:
                            canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='red',outline='')
                        else:
                            canvas.create_rectangle(side*x+20,side*y+20,side*(x+1)+20,side*(y+1)+20,fill='blue',outline='')
                    
        for x,y in addignore:
            ignorable[x][y]=1
        for x,y in removeignore:
            ignorable[x][y]=0
                
        grid=newgrid
        
        # print('red',totalred,'blue',totalblue)
        # canvas.create_text(1075,410,text=totalred)
        # canvas.create_text(1075,510,text=totalblue)
        canvas.create_text(1100,340,text=generation)
        canvas.update()
        
        t2=time.time()
        print(t2-t1)
        # for i in grid:
        #     print(i)
        # time.sleep(1)
        
    tend=time.time()
    print(tend-tstart,"s")


canvas.bind("<Button-1>",start)
canvas.pack()
window.mainloop()
