from tkinter import *
root = Tk()
root.title("Paint application")
root.geometry("1100x600")



# Frame 1 => Tools
frame1 = Frame(root, height=100, width=1100)
frame1.grid(row=0,column=0, sticky=NW)

# frame => tools insize frame 1
toolsFrame = Frame(frame1 , height=100 , width=100)
toolsFrame.grid(row=0 , column=0)

stroke_size = IntVar()
stroke_size.set(1)
stroke_color = StringVar()
stroke_color.set("black")

def usePencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"

def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX

pencilButton = Button(toolsFrame , text="Pencil",width=10, command=usePencil)
pencilButton.grid(row=0 , column=0)

eraserButton = Button(toolsFrame , text="Eraser",width=10, command=useEraser)
eraserButton.grid(row=1 , column=0)

toolsLabel = Label(toolsFrame , text="Tools",width=10)
toolsLabel.grid(row=3 , column=0)


# Frame => sizeframe inside frame 1
sizeFrame = Frame(frame1 , height=100 , width=100 )
sizeFrame.grid(row=0 , column=1)

defaultButton = Button(sizeFrame , text="Default",width=10, command=useEraser)
defaultButton.grid(row=0 , column=0)



options = [1,2,3,4,5]

sizeList = OptionMenu(sizeFrame ,stroke_size, *options)
sizeList.grid(row=1 , column=0)

sizeLabel = Label(sizeFrame , text="size",width=10)
sizeLabel.grid(row=2 , column=0)



# Frame 2 = > Canvas
frame2 = Frame(root, height=500, width=1100, bg="yellow")
frame2.grid(row=1,column=0)

canvas = Canvas(frame2,height=500,width=1100,bg="white")
canvas.grid(row=0,column=0)




#variables for pencil
prevPoint =[0,0]
currentPoint = [0,0]

def paint(event):
  
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint = [x,y]
    #canvas.create_oval(x, y, x+5, y+5, fill="black")

    if prevPoint != [0,0]:
        canvas.create_polygon(prevPoint[0] , prevPoint[1] , currentPoint[0], currentPoint[1], fill=stroke_color.get(),outline=stroke_color.get(), width=stroke_size.get())
        # instead of writing line we are writing polygon to have ssmooth lines

    prevPoint = currentPoint

    if event.type == "5" :
        prevPoint = [0,0]

    
def paintRight(event):
    x = event.x
    y = event.y
    canvas.create_arc(x,y,x+stroke_size.get() , y+stroke_size.get() , fill=stroke_color.get() , outline=stroke_color.get() , width=stroke_size.get())
    

canvas.bind("<B1-Motion>" , paint)
canvas.bind("<ButtonRelease-1>",paint)

root.resizable(False,False)   
root.mainloop()