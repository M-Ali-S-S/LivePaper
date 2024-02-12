from tkinter import *
import time, cv2, random
from PIL import Image, ImageTk
#..............................FUNCTIONS............................
def exit():
    window.destroy()
def drag(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
def move(obj,x,y):
    obj.getpo
# class Block:
#     def __init__(self,pic):
#         self.pic = 
# spawn_points=[100,200,300,400,500]
SPEEDS=[4,6,5]

class Actor:
    
    def __init__(self,pic):
        self.canvas= board
        self.pic = pic
        self.SpeedX=random.choice(SPEEDS)
        self.SpeedY=random.choice(SPEEDS)
        
    def Spawn(self):
        self.ActorPic=board.create_image(random.randint(100,WIDTH-100),random.randint(100,HEIGHT-100),image=self.pic)
        for i in range(200): 
            location = board.coords(self.ActorPic)
            if (location[0]+52 >= WIDTH) or (location[0]-52 <= 0):
                self.SpeedX = -self.SpeedX
            if (location[1]+85 >= HEIGHT) or (location[1]-60 <= 0):
                self.SpeedY = -self.SpeedY
            board.move(self.ActorPic,self.SpeedX,self.SpeedY)
            window.update()
            
            time.sleep(0.01)
            break
    def Kill(self):
        self.canvas.destroy(self)
    def GMove(self):
                
         
                location = self.canvas.coords(self.ActorPic)
                # print(location)
    
                if (location[0]+52 >= WIDTH) or (location[0]-52 <= 0):
                    self.SpeedX = -self.SpeedX
                if (location[1]+85 >= HEIGHT) or (location[1]-60 <= 0):
                    self.SpeedY = -self.SpeedY

                self.canvas.move(self.ActorPic,self.SpeedX,self.SpeedY)
                # location = self.canvas.coords(self.ActorPic)
                window.update()
                time.sleep(0.01)
        


window = Tk()
window.attributes("-fullscreen",True)
window.wm_attributes('-transparentcolor',"#de23de")
window.wm_attributes("-topmost", 1)
window.config(bg="#de23de")

window.update()
WIDTH = window.winfo_width()
HEIGHT = window.winfo_height()
spawn_points=[random.randint(0,HEIGHT),]

board = Canvas(highlightthickness=0)
board.pack(fill=BOTH, expand=True)
board.config(bg="#de23de",borderwidth=10,)
steve = PhotoImage(file="Phyton\\LivePaper\\steve.png")
ghast = PhotoImage(file="Phyton\\LivePaper\\ghast.png")
srcG="LivePaper\\ghast.png"
srcG2=cv2.imread(srcG)
# GhastL = board.create_image(53,61,image=ghast)

#_______________BUTTON__&__Char____________
exitB = Button(window,text="EXIT",command=exit,bg="yellow",fg="red")
exitB.pack()
exitB.bind("<Button-3>",drag)
exitB.bind("<B3-Motion>",motion)

SteveL = Label(board,image=steve,bg="white",borderwidth=0,anchor="se")
SteveL.pack()
SteveL.bind("<Button-3>",drag)
SteveL.bind("<B3-Motion>",motion)


#_____________________________________

ghost2 = Actor(ghast)
ghost3 = Actor(ghast)
ghost4 = Actor(ghast)
ghost5 = Actor(ghast)

ghost2.Spawn()
ghost3.Spawn()
ghost4.Spawn()
ghost5.Spawn()

while True:
    ghost3.GMove()
    ghost2.GMove()
    ghost4.GMove()
    ghost5.GMove()
    
window.mainloop()



#                  but useful
#                      \/
#______________Bullshit  code_______________

# window.overrideredirect(True)
# window.wm_attributes('-topmost',True)

# GhastL = Label(window,image=ghast,bg="white",borderwidth=0)
# GhastL.pack()
# GhastL.bind("<Button-3>",drag)
# GhastL.bind("<B3-Motion>",motion)



# def GMove():
#     SPEEDX=6
#     SPEEDY=1
#     while True: 
#         location = board.coords(GhastL)
#         if (location[0]+52 >= WIDTH) or (location[0]-52 <= 0):
#             SPEEDX = -SPEEDX
#         if (location[1]+85 >= HEIGHT) or (location[1]-60 <= 0):
#             SPEEDY = -SPEEDY
#         board.move(GhastL,SPEEDX,SPEEDY)
#         window.update()
#         time.sleep(0.01)
# GMove()
