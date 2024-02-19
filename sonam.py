from tkinter import *
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox




root = Tk()
root.geometry("%dx%d+%d+%d" % (root.winfo_screenwidth(), root.winfo_screenheight(), 0, 0))
# Frame 1 => Tools
frame1 = Frame(root, height=100, width=1100, relief=SUNKEN,borderwidth=3)
frame1.grid(row=0,column=0, sticky=NW)


# frame => tools inside frame 1
toolsFrame = Frame(frame1 , height=0 , width=0 )
toolsFrame.grid(row=0 , column=0)

# variables
stroke_size = IntVar()
stroke_size.set(1)
stroke_color = StringVar()
stroke_color.set("black")

def usePencil():
    stroke_color.set("black")
    canvas["cursor"] = "plus"

def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = "circle"

pencilButton = Button(toolsFrame , text="Pencil",width=10, command=usePencil)
pencilButton.grid(row=0 , column=0)

eraserButton = Button(toolsFrame , text="Eraser",width=10, command=useEraser)
eraserButton.grid(row=1 , column=0)




# Frame => sizeframe inside frame 1
sizeFrame = Frame(frame1 , height=100 , width=100,relief=SUNKEN,borderwidth=3 )
sizeFrame.grid(row=0 , column=1)

defaultButton = Button(sizeFrame , text="Default",width=10, command=useEraser)
defaultButton.grid(row=0 , column=0)

options = [1,2,3,4,5,8,10]

sizeList = OptionMenu(sizeFrame ,stroke_size, *options)
sizeList.grid(row=1 , column=0)

sizeLabel = Label(sizeFrame , text="size",width=10)
sizeLabel.grid(row=2 , column=0)



# Frame : COLORBOX inside FRame 1
colorBoxFrame = Frame(frame1 , height=100 , width=100 , relief=SUNKEN,borderwidth=3)
colorBoxFrame.grid(row=0 , column=2)

# variables
previousColor = StringVar()
previousColor.set("white")
previousColor2 = StringVar()
previousColor2.set("white")

def selectColor():
    selectedColor = colorchooser.askcolor("blue" , title="select Color")
    if selectedColor[1] == None:
        stroke_color.set("black")
    else:
        stroke_color.set(selectedColor[1])   
        previousColor2.set(previousColor.get())
        previousColor.set(selectedColor[1])

        previousColorButton["bg"] = previousColor.get()
        previousColor2Button["bg"] = previousColor2.get()


colorBoxButton = Button(colorBoxFrame , text="Select Color", width=10, command=selectColor)
colorBoxButton.grid(row=0, column=0)

previousColorButton = Button(colorBoxFrame , text="Previous", width=10, command=lambda:stroke_color.set(previousColor.get()))
previousColorButton.grid(row=1, column=0)

previousColor2Button = Button(colorBoxFrame , text="Previous2", width=10, command=lambda:stroke_color.set(previousColor2.get()))
previousColor2Button.grid(row=2, column=0)



# Frame => ColorsFrame inside frame 1
colorsFrame = Frame(frame1 , height=100 , width=100 , relief=SUNKEN,borderwidth=3)
colorsFrame.grid(row=0 , column=3)

redButton = Button(colorsFrame, text="red" ,width=10, bg="red", command=lambda:stroke_color.set("red"))
redButton.grid(row=0,column=0)

greenButton = Button(colorsFrame, text="green" ,width=10, bg="green", command=lambda:stroke_color.set("green"))
greenButton.grid(row=1,column=0)

blueButton = Button(colorsFrame, text="blue" ,width=10, bg="blue", command=lambda:stroke_color.set("blue"))
blueButton.grid(row=2,column=0)


cyanButton = Button(colorsFrame, text="cyan" ,width=10, bg="cyan", command=lambda:stroke_color.set("cyan"))
cyanButton.grid(row=0,column=1)

pinkButton = Button(colorsFrame, text="pink" ,width=10, bg="pink", command=lambda:stroke_color.set("pink"))
pinkButton.grid(row=1,column=1)

tanButton = Button(colorsFrame, text="tan" ,width=10, bg="tan", command=lambda:stroke_color.set("tan"))
tanButton.grid(row=2,column=1)


yellowButton = Button(colorsFrame, text="yellow" ,width=10, bg="yellow", command=lambda:stroke_color.set("yellow"))
yellowButton.grid(row=0,column=2)

orangeButton = Button(colorsFrame, text="orange" ,width=10, bg="orange", command=lambda:stroke_color.set("orange"))
orangeButton.grid(row=1,column=2)

PurpleButton = Button(colorsFrame, text="purple" ,width=10, bg="purple", command=lambda:stroke_color.set("purple"))
PurpleButton.grid(row=2,column=2)



# frame => save image Frame inside frame 1
saveImageFrame = Frame(frame1 , height=100 , width=100 , relief=SUNKEN,borderwidth=3)
saveImageFrame.grid(row=0,column=4)

def saveImage():
    try:
        fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")
        x = root.winfo_rootx()
        y = root.winfo_rooty()+100
        img = ImageGrab.grab(bbox=(x,y,x+1100,y+500))
        img.save(fileLocation)
        showImage = messagebox.askyesno("Paint App", "Do uh want to open image...?")
        if showImage:
            img.show()
    except Exception as e:
        messagebox.showinfo("Paint app:","Error occured")


saveImageButton = Button(saveImageFrame, text="save" ,width=10, bg="white", command=saveImage)
saveImageButton.grid(row=0,column=0)

def clear():
    if messagebox.askokcancel("Paint app", "Are uh sure ...?"):
        canvas.delete('all')

def createNew():
    if messagebox.askokcancel("Paint app", "Do uh want to save it before you clear ...?"):
        saveImage()
    clear()


newImageButton = Button(saveImageFrame, text="New" ,width=10, bg="white", command=createNew)
newImageButton.grid(row=1,column=0)

clearImageButton = Button(saveImageFrame, text="Clear" ,width=10, bg="white", command=clear)
clearImageButton.grid(row=2,column=0)



# Frame 2 = > Canvas
frame2 = Frame(root, height=500, width=500)
frame2.grid(row=1,column=0)

canvas = Canvas(frame2,height=1500,width=1200,bg="white")
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
