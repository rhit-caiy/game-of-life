#the bicolour cellular automata with the rule of Conway's game of life
from tkinter import *
window=Tk()
canvas=Canvas(window,bg="white",width=1350,height=760)
window.title('bicolour game of life')
for i in range(0,800,40):
    canvas.create_line(0,i,760,i)
    canvas.create_line(i,0,i,760)
#actual grid start from 1,1 to 19,19 below
grid=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
generation=0
canvas.create_text(1050,20, text='the game follows following rules:')
canvas.create_text(1050,40, text='the coloured cell is live and otherwise dead')
canvas.create_text(1050,60, text='each cell has 8 neighbours')
canvas.create_text(1050,80, text='if more than 3 neighbours alive, the cell would die due to too crowd')
canvas.create_text(1050,100, text='if less than 2 neighbour alive, the cell would die due to loneness')
canvas.create_text(1050,120, text='if a dead cell is arounded by 3 living cells, it would born')
canvas.create_text(1050,140, text='in bicolour rule, the cell would born with the neighbour colour which more than another')
canvas.create_text(1050,160, text='two gamer can put equal number of live cells initially')
canvas.create_text(1050,180, text='then after certain steps, the player with more own living cells can be considered winner')
canvas.create_text(1050,200, text='click the grid to create live cell, the colour would change from white to red to blue to white')
canvas.create_text(1050,250, text='click blank area to step')
canvas.create_text(1000,300, text='generation:')
canvas.create_oval(900,400,920,420,fill='red')
canvas.create_oval(900,500,920,520,fill='blue')
def count():
    global r,b
    r=0
    b=0
    for i in range(1,20):
        for j in range(1,20):
            if grid[i][j]==1:
                r+=1
            elif grid[i][j]==2:
                b+=1
    print('red',r,'blue',b)
    canvas.create_rectangle(950,400,1000,420,width=0,fill='white')
    canvas.create_text(975,410,text=r)
    canvas.create_rectangle(950,500,1000,520,width=0,fill='white')
    canvas.create_text(975,510,text=b)
def red(ax,ay):
    grid[ax][ay]=1
    canvas.create_rectangle(40*ax-40,40*ay-40,40*ax,40*ay,fill='red')
def blue(ax,ay):
    grid[ax][ay]=2
    canvas.create_rectangle(40*ax-40,40*ay-40,40*ax,40*ay,fill='blue')
def white(ax,ay):
    grid[ax][ay]=0
    canvas.create_rectangle(40*ax-40,40*ay-40,40*ax,40*ay,fill='white')
def position(p):
    global ax,ay
    click_x=p.x
    click_y=p.y
    ax=round((click_x+20)/40)
    ay=round((click_y+20)/40)
    if ax>19:
        start()
    elif ax<0 or ay<0 or ax>19 or ay>19:
        pass
    elif grid[ax][ay]==0:
        red(ax,ay)
    elif grid[ax][ay]==1:
        blue(ax,ay)
    elif grid[ax][ay]==2:
        white(ax,ay)
    else:
        pass
    count()
canvas.bind("<Button-1>",position)
def start():
    #19*19*2
    global generation
    generation+=1
    print('generation',generation)
    canvas.create_rectangle(1035,290,1065,310,width=0,fill='white')
    canvas.create_text(1050,300,text=generation)
    count=[[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
           [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
    #detect the colours around
    for x in range(1,20):
        for y in range(1,20):
            for a in range(-1,2):
                for b in range(-1,2):
                    if grid[x+a][y+b]==1:
                        count[x-1][y-1][0]+=1
                    elif grid[x+a][y+b]==2:
                        count[x-1][y-1][1]+=1
            if grid[x][y]==1:
                count[x-1][y-1][0]-=1
            elif grid[x][y]==2:
                count[x-1][y-1][1]-=1
    #birth,live and death
    for x in range(0,19):
        for y in range(0,19):
            #death while neighbour>3 or <2 
            if count[x][y][0]+count[x][y][1]>3 or count[x][y][0]+count[x][y][1]<2:
                white(x+1,y+1)
            #cell birth while neighbour=3 with the colour of neighbours which are more than another one
            if count[x][y][0]+count[x][y][1]==3 and grid[x+1][y+1]==0:
                if count[x][y][0]==3 or count[x][y][0]==2:
                    red(x+1,y+1)
                elif count[x][y][1]==3 or count[x][y][1]==2:
                    blue(x+1,y+1)
canvas.pack()
window.mainloop()