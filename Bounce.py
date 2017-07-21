#Import everything
from tkinter import*
import random
import time
tk = Tk()

# Make a ball class
class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1,2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y = 1
        if pos[3]>=self.canvas_height:
            self.y=-1
        if pos[0]<=0:
            self.x = 3
        if pos[2]>=self.canvas_width:
            self.x = -3

# Make a paddle class

class Paddle:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        pass
            
    
    

#Create the game
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",-1)
canvas = Canvas(tk, width=500,height=400,bd=0)
canvas.pack()
tk.update()
ball = Ball(canvas, 'orange')
paddle = Paddle(canvas, 'blue')

#aku is cutie pie
while 1:
    paddle.draw()
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


